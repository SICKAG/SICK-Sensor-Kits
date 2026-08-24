import tkinter as tk
from tkinter import scrolledtext
import threading
import socket
import os
import platform
import pyttsx3
from datetime import datetime

# =================================================================================
# 1. ARTIFICIAL INTELLIGENCE ENGINE (Minimax Algorithm)
# =================================================================================
# This section handles the game logic. It uses a recursive Minimax algorithm
# to determine the optimal move for the AI ("O"), making it impossible to beat.
# =================================================================================

def check_win(board, player):
    """
    Checks if the specified player has won the game.
    Returns True if a winning line (row, column, or diagonal) is found.
    """
    for i in range(3):
        # Check rows and columns
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    return (board[0][0] == board[1][1] == board[2][2] == player) or \
           (board[0][2] == board[1][1] == board[2][0] == player)

def get_possible_moves(board, player):
    """
    Generates all valid moves.
    - Phase 1 (Placement): If < 3 pieces, can place anywhere empty.
    - Phase 2 (Movement): If 3 pieces, must move an existing piece to an adjacent empty spot.
    """
    pions = [(r, c) for r in range(3) for c in range(3) if board[r][c] == player]
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    if len(pions) < 3: return [(None, v) for v in empty] # Placement phase
    return [(p, v) for p in pions for v in empty] # Movement phase

def minimax(board, depth, alpha, beta, is_max, ia_player):
    """
    Recursive Minimax function with Alpha-Beta pruning for optimization.
    Evaluates all possible future game states to find the best outcome.
    """
    opp = "X" if ia_player == "O" else "O"
    if check_win(board, ia_player): return 100 - depth # AI wins
    if check_win(board, opp): return depth - 100       # Opponent wins
    if depth >= 8: return 0 # Depth limit to prevent infinite recursion
    
    moves = get_possible_moves(board, ia_player if is_max else opp)
    if not moves: return 0

    if is_max: # Maximizing player (AI)
        v = -float('inf')
        for s, e in moves:
            svg = board[e[0]][e[1]]
            if s: board[s[0]][s[1]] = " "
            board[e[0]][e[1]] = ia_player
            v = max(v, minimax(board, depth + 1, alpha, beta, False, ia_player))
            # Backtrack
            board[e[0]][e[1]] = svg
            if s: board[s[0]][s[1]] = ia_player
            alpha = max(alpha, v)
            if beta <= alpha: break
        return v
    else: # Minimizing player (Human)
        v = float('inf')
        for s, e in moves:
            svg = board[e[0]][e[1]]
            if s: board[s[0]][s[1]] = " "
            board[e[0]][e[1]] = opp
            v = min(v, minimax(board, depth + 1, alpha, beta, True, ia_player))
            # Backtrack
            board[e[0]][e[1]] = svg
            if s: board[s[0]][s[1]] = opp
            beta = min(beta, v)
            if beta <= alpha: break
        return v

def get_best_move(board, ia_player):
    """
    Root function for the AI. Iterates through all immediate moves 
    and calls minimax() to score them. Returns the best (start, end) tuple.
    """
    moves = get_possible_moves(board, ia_player)
    # Immediate win check for speed optimization
    for s, e in moves:
        temp = [r[:] for r in board]
        if s: temp[s[0]][s[1]] = " "
        temp[e[0]][e[1]] = ia_player
        if check_win(temp, ia_player): return (s, e)
    
    best_v, choice = -float('inf'), moves[0]
    for s, e in moves:
        svg = board[e[0]][e[1]]
        if s: board[s[0]][s[1]] = " "
        board[e[0]][e[1]] = ia_player
        v = minimax(board, 0, -float('inf'), float('inf'), False, ia_player)
        board[e[0]][e[1]] = svg
        if s: board[s[0]][s[1]] = ia_player
        if v > best_v: best_v, choice = v, (s, e)
    return choice

# =================================================================================
# 2. AUDIO FEEDBACK SYSTEM (Text-to-Speech)
# =================================================================================
# Provides asynchronous voice commands to guide the operator without freezing the UI.
# Supports macOS (native 'say' command) and Windows/Linux (pyttsx3).
# =================================================================================

def speak_async(text):
    def run():
        try:
            if platform.system() == "Darwin": os.system(f'say -v Samantha "{text}"')
            else:
                eng = pyttsx3.init()
                eng.setProperty('rate', 150) # Set speech speed
                eng.say(text); eng.runAndWait()
        except: pass
    threading.Thread(target=run, daemon=True).start()

# =================================================================================
# 3. MODERN USER INTERFACE (Tkinter)
# =================================================================================
# The main application class handling the GUI, TCP server, and game state.
# Features a modern dark theme and real-time status monitoring.
# =================================================================================

class ProVisionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Window configuration
        self.title("SICK Assistant Pro v2.0")
        self.geometry("500x750")
        self.configure(bg="#0F172A") # Deep Navy Blue theme
        
        # Game State Initialization
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.highlighted = []
        self.logs_visible = False
        
        # Coordinate mapping for voice instructions
        self.coord_names = {
            (0,0):"top left",(0,1):"top center",(0,2):"top right",
            (1,0):"middle left",(1,1):"center",(1,2):"middle right",
            (2,0):"bottom left",(2,1):"bottom center",(2,2):"bottom right"
        }
        
        self.setup_ui()
        
        # Start TCP Server in a separate thread to prevent UI blocking
        threading.Thread(target=self.tcp_server, daemon=True).start()
        
        # Start the GUI refresh loop
        self.refresh_gui_loop()

    def setup_ui(self):
        """Constructs the visual elements of the application."""
        # Header Section
        header = tk.Frame(self, bg="#1E293B", height=80)
        header.pack(fill=tk.X)
        tk.Label(header, text="SYSTEM STATUS", font=("Helvetica", 9, "bold"), bg="#1E293B", fg="#94A3B8").pack(pady=(15,0))
        self.status = tk.Label(header, text="LIVE MONITORING", fg="#10B981", bg="#1E293B", font=("Helvetica", 14, "bold"))
        self.status.pack(pady=(0,15))

        # Main Game Grid Container
        container = tk.Frame(self, bg="#0F172A", pady=20)
        container.pack()

        grid_frame = tk.Frame(container, bg="#334155", padx=4, pady=4)
        grid_frame.pack(pady=10)

        # Initialize Grid Buttons (Labels used as display units)
        for r in range(3):
            for c in range(3):
                l = tk.Label(grid_frame, text=" ", font=("Helvetica", 32, "bold"), 
                             width=4, height=2, bg="#1E293B", fg="white", 
                             relief="flat")
                l.grid(row=r, column=c, padx=3, pady=3)
                self.buttons[r][c] = l

        # Control Panel Section
        controls = tk.Frame(self, bg="#0F172A")
        controls.pack(fill=tk.X, padx=40, pady=20)

        # AI Advice Trigger Button
        self.ai_button = tk.Button(controls, text="GET ADVICE", font=("Helvetica", 11, "bold"), 
                                   bg="#3B82F6", fg="white", activebackground="#2563EB", 
                                   activeforeground="white", relief="flat", command=self.process_ai, 
                                   cursor="hand2", pady=12)
        self.ai_button.pack(fill=tk.X, pady=5)

        # Log Toggle Button
        self.log_toggle_btn = tk.Button(controls, text="SHOW LOGS", font=("Helvetica", 9), 
                                       bg="#1E293B", fg="#94A3B8", relief="flat", 
                                       command=self.toggle_logs, cursor="hand2")
        self.log_toggle_btn.pack(pady=5)

        # Hidden Log Console (ScrolledText)
        self.debug_console = scrolledtext.ScrolledText(self, height=8, bg="#020617", 
                                                      fg="#38BDF8", font=("Consolas", 9), 
                                                      borderwidth=0, state='disabled')

    def toggle_logs(self):
        """Show/Hide the TCP debug console."""
        if not self.logs_visible:
            self.debug_console.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
            self.log_toggle_btn.config(text="HIDE LOGS")
        else:
            self.debug_console.forget()
            self.log_toggle_btn.config(text="SHOW LOGS")
        self.logs_visible = not self.logs_visible

    def log_debug(self, message):
        """Appends timestamped messages to the debug console."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.debug_console.config(state='normal')
        self.debug_console.insert(tk.END, f"[{timestamp}] {message}\n")
        self.debug_console.see(tk.END)
        self.debug_console.config(state='disabled')

    def tcp_server(self):
        """
        Runs the TCP/IP server listening on port 5000.
        Receives raw string data from the SICK Camera.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', 5000))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    data = conn.recv(2048).decode('utf-8')
                    if data:
                        self.log_debug(f"Input from camera: {addr[0]}")
                        self.parse_nova_data(data)

    def parse_nova_data(self, raw_str):
        """
        Parses the raw CSV string from SICK Nova.
        Expected format: "Label, X, Y, Label, X, Y..."
        Sorts objects by X/Y coordinates to map them to the 3x3 grid.
        """
        try:
            # Clean string prefix if necessary
            clean_str = raw_str.split(":", 1)[1].strip() if ":" in raw_str else raw_str
            items = [i.strip() for i in clean_str.split(',')]
            
            # Validation: Ensure we have exactly 27 items (9 cells * 3 attributes)
            if len(items) != 27: return

            objs = []
            for i in range(0, len(items), 3):
                lbl = items[i].replace(" ", "")
                val = "X" if lbl == "Croix" else ("O" if lbl == "Rond" else " ")
                objs.append({'v': val, 'x': float(items[i+1]), 'y': float(items[i+2])})
            
            # Spatial sorting: Sort by Y (rows), then by X (columns)
            objs.sort(key=lambda o: o['y'])
            r1, r2, r3 = sorted(objs[0:3], key=lambda o: o['x']), sorted(objs[3:6], key=lambda o: o['x']), sorted(objs[6:9], key=lambda o: o['x'])
            self.board = [[c['v'] for c in r1], [c['v'] for c in r2], [c['v'] for c in r3]]
        except: pass

    def refresh_gui_loop(self):
        """Periodically refreshes the UI to match the internal board state."""
        for r in range(3):
            for c in range(3):
                if (r,c) not in self.highlighted:
                    char = self.board[r][c]
                    self.buttons[r][c].config(text=char, bg="#1E293B")
                    # Color coding for players
                    if char == "X": self.buttons[r][c].config(fg="#F43F5E") # Rose-Red
                    elif char == "O": self.buttons[r][c].config(fg="#38BDF8") # Light Blue
        self.after(200, self.refresh_gui_loop)

    def process_ai(self):
        """
        Triggered by user. Calculates best move and provides audio/visual guidance.
        """
        res = get_best_move(self.board, "O")
        start, end = res if isinstance(res, tuple) else (None, res)
        self.highlighted = [end]
        
        # Generate Voice Command
        if start:
            self.highlighted.append(start)
            msg = f"Take the piece from {self.coord_names[start]} and move it to the {self.coord_names[end]}."
        else:
            msg = f"Place a new piece in the {self.coord_names[end]}."
        
        speak_async(msg)
        self.status.config(text="ADVICE SENT", fg="#F59E0B") # Orange warning status
        self.log_debug(f"AI Decision: {msg}")
        self.blink()

    def blink(self, count=0):
        """Recursive function to blink the suggested move cells."""
        if count < 8:
            # Toggle color: Emerald Green / Dark Blue
            color = "#10B981" if count % 2 == 0 else "#1E293B"
            for r, c in self.highlighted:
                self.buttons[r][c].config(bg=color)
            self.after(250, lambda: self.blink(count + 1))
        else:
            self.highlighted = []
            self.status.config(text="LIVE MONITORING", fg="#10B981")

if __name__ == "__main__":
    App = ProVisionApp()
    App.mainloop()