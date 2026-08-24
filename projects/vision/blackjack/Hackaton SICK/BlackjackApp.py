import tkinter as tk
from tkinter import messagebox
import time
from Connection import BlackjackClient
from GameState import GameState
from BlackJackStrategy import get_optimal_move

class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vision Blackjack & AI")
        self.root.geometry("1024x768")
        self.root.configure(bg="#2E8B57") 

        self.client = BlackjackClient()
        self.state = GameState()
        
        self.canvas = tk.Canvas(root, bg="#2E8B57", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self._setup_ui()
        
        self.update_ui_state(initial=True)

    def _setup_ui(self):
        # Table Decoration
        self.canvas.create_arc(200, 100, 824, 600, start=0, extent=-180, style=tk.ARC, outline="#3CB371", width=5)
        self.canvas.create_text(512, 350, text="BLACKJACK", fill="#FFD700", font=("Arial", 36, "bold"))
        self.canvas.create_text(512, 390, text="Dealer must stand on 17 and draw to 16", fill="#F0E68C", font=("Arial", 12))

        # Control Panel
        img_panel = tk.Frame(self.root, bg="#1E5B37", height=80)
        img_panel.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        
        self.btn_start = tk.Button(img_panel, text="START GAME", command=self.start_game, 
                                   bg="#006400", fg="white", font=("Arial", 14, "bold"), padx=20, pady=5)
        self.btn_start.pack(side=tk.LEFT, padx=30, pady=10)

        self.btn_hit = tk.Button(img_panel, text="HIT", command=self.hit, 
                                 bg="#FF8C00", fg="white", font=("Arial", 14, "bold"), width=10)
        self.btn_hit.pack(side=tk.LEFT, padx=10, pady=10)

        self.btn_stay = tk.Button(img_panel, text="STAY", command=self.stay, 
                                  bg="#DC143C", fg="white", font=("Arial", 14, "bold"), width=10)
        self.btn_stay.pack(side=tk.LEFT, padx=10, pady=10)

        self.status_label = tk.Label(img_panel, text="Status: Ready", bg="#1E5B37", fg="white", font=("Arial", 12))
        self.status_label.pack(side=tk.RIGHT, padx=30)

    def draw_card(self, x, y, value, is_dealer=False):
        cw, ch = 80, 120
        
        self.canvas.create_rectangle(x+2, y+2, x+cw+2, y+ch+2, fill="#222", outline="")
        self.canvas.create_rectangle(x, y, x+cw, y+ch, fill="white", outline="black", width=2)
        
        color = "black"
        
        self.canvas.create_text(x+cw/2, y+ch/2, text=str(value), fill=color, font=("Times New Roman", 24, "bold"))
        self.canvas.create_text(x+15, y+20, text=str(value), fill=color, font=("Arial", 12))
        self.canvas.create_text(x+cw-15, y+ch-20, text=str(value), fill=color, font=("Arial", 12))

    def update_ui_state(self, initial=False):
        self.canvas.delete("dynamic")
        
        status = self.state.get_status()
        cur = status['current']

        self.canvas.delete("all")
        self._setup_ui() 
        
        # Dealer Area
        self.canvas.create_text(512, 30, text=f"DEALER - Score: {status['dealer']['score']}", fill="white", font=("Arial", 16, "bold"))
        
        dealer_cards = [c for c in status['dealer']['cards'] if "No class" not in str(c)]
        for i, card in enumerate(dealer_cards):
             self.draw_card(472 + (i*90) - (len(dealer_cards)*45) + 45, 60, card)

        # Player 1 Area
        p1_color = "#FFD700" if cur == 'player1' else "white"
        self.canvas.create_text(200, 550, text="PLAYER 1", fill=p1_color, font=("Arial", 16, "bold"))
        self.canvas.create_text(200, 580, text=f"Score: {status['p1']['score']}", fill="white", font=("Arial", 14))
        
        if cur == 'player1':
            d_card = self.state.dealer_cards[0] if self.state.dealer_cards else "10"
            advice = get_optimal_move(status['p1']['cards'], d_card)
        else:
            advice = ""
        if advice:
            self.canvas.create_text(200, 480, text=f"Strategy: {advice}", fill="#00FF00", font=("Arial", 14, "bold"))

        p1_cards = [c for c in status['p1']['cards'] if "No class" not in str(c)]
        for i, card in enumerate(p1_cards):
             self.draw_card(100 + (i*50), 600, card)

        # Player 2 Area
        p2_color = "#FFD700" if cur == 'player2' else "white"
        self.canvas.create_text(824, 550, text="PLAYER 2", fill=p2_color, font=("Arial", 16, "bold"))
        self.canvas.create_text(824, 580, text=f"Score: {status['p2']['score']}", fill="white", font=("Arial", 14))

        if cur == 'player2':
            d_card = self.state.dealer_cards[0] if self.state.dealer_cards else "10"
            advice = get_optimal_move(status['p2']['cards'], d_card)
        else:
            advice = ""
        if advice:
            self.canvas.create_text(824, 480, text=f"Strategy: {advice}", fill="#00FF00", font=("Arial", 14, "bold"))

        p2_cards = [c for c in status['p2']['cards'] if "No class" not in str(c)]
        for i, card in enumerate(p2_cards):
             self.draw_card(724 + (i*50), 600, card)

        # Game Status
        if self.state.game_over:
            self.canvas.create_text(512, 300, text=f"WINNER: {self.state.winner}", fill="#00FF7F", font=("Arial", 40, "bold"))
            self.status_label.config(text=f"Game Over!")
            self.btn_hit.config(state=tk.DISABLED)
            self.btn_stay.config(state=tk.DISABLED)
        else:
            self.status_label.config(text=f"Turn: {cur}")
            if cur in ['player1', 'player2']:
                self.btn_hit.config(state=tk.NORMAL)
                self.btn_stay.config(state=tk.NORMAL)
            else:
                self.btn_hit.config(state=tk.DISABLED)
                self.btn_stay.config(state=tk.DISABLED)

    def start_game(self):
        self.client.connect()
        resp = self.client.trigger_and_receive()
        if resp:
            d, p1, p2 = resp[0], resp[1], resp[2]
            self.state.reset()
            self.state.set_initial_cards(d, p1, p2)
            self.update_ui_state()
        else:
            messagebox.showerror("Error", "Failed to receive initial cards.")
    def check_blackjack_start(self):
        # Check natural blackjack for P1/P2
        pass # Implemented in end_game logic or immediate win could be added here

    def hit(self):
        cur = self.state.current_player
        resp = self.client.trigger_and_receive()
        if resp:
            new_card = None
            if cur == 'player1': new_card = resp[1]
            elif cur == 'player2': new_card = resp[2]
            
            # Valider la carte
            if new_card and self.state._get_card_value(new_card) > 0:
                self.state.add_card(cur, new_card)
                
                score, _ = self.state.calculate_score(self.state.p1_cards if cur == 'player1' else self.state.p2_cards)
                
                self.update_ui_state()
                
                if score == 21:
                    self.animate_blackjack()
                    self.root.after(1500, self.stay) 
                elif score > 21:
                    messagebox.showinfo("Bust", f"{cur} Busted!")
                    self.stay()
            else:
                messagebox.showwarning("Erreur", "Aucune nouvelle carte détectée. Veuillez réessayer.")
        else:
            messagebox.showerror("Erreur", "Erreur de communication.")

    def animate_blackjack(self):
        self.canvas.create_text(512, 400, text="BLACKJACK!", fill="yellow", font=("Arial", 50, "bold"), tags="anim")
        self.root.update()
        
    def stay(self):
        cur = self.state.current_player
        if cur == 'player1':
            self.state.current_player = 'player2'
            self.update_ui_state()
        elif cur == 'player2':
            self.state.current_player = 'dealer'
            self.update_ui_state()
            self.run_dealer_turn()

    def run_dealer_turn(self):
        d_score, _ = self.state.calculate_score(self.state.dealer_cards)
        self.update_ui_state()
        
        if d_score >= 17:
             self.end_game(d_score)
             return

        if messagebox.askokcancel("Dealer Turn", "Prochaine carte du dealer !"):
            resp = self.client.trigger_and_receive()
            if resp:
                new_card = resp[0]
                # Check valid
                if self.state._get_card_value(new_card) > 0:
                    self.state.add_card('dealer', new_card)
                    self.update_ui_state()
                    self.root.after(800, self.run_dealer_turn)
                else:
                    messagebox.showwarning("Erreur", "Aucune carte détectée pour le dealer. Réessayez.")
                    self.run_dealer_turn() # Retry loop
        else:
            pass

    def end_game(self, dealer_score):
        self.state.game_over = True
        
        p1_score, _ = self.state.calculate_score(self.state.p1_cards)
        p2_score, _ = self.state.calculate_score(self.state.p2_cards)
        
        winners = []
        d_bj = self.state.is_blackjack(self.state.dealer_cards)
        
        # Helper to decide winner
        def check_winner(p_score, p_cards, name):
            if p_score > 21: return False
            p_bj = self.state.is_blackjack(p_cards)
            
            if dealer_score > 21: return True
            
            if p_bj and not d_bj: return True # BJ beats 21
            if not p_bj and d_bj: return False # Dealer BJ beats 21
            
            if p_score > dealer_score: return True
            if p_score == dealer_score: return False # Push (Dealer wins ties in this simple logic? Or push? Usually push. User just said "Winners")
            # If Push is not a "Win", return False.
            
            return False

        if check_winner(p1_score, self.state.p1_cards, "Player 1"):
            winners.append("Player 1")
        
        # Check if Push? For now strict win listing.
        
        if check_winner(p2_score, self.state.p2_cards, "Player 2"):
            winners.append("Player 2")
                
        if not winners:
            # Check for Pushes? Or just declare Dealer win?
            # User prompt imples we want to see who won.
            self.state.winner = "Dealer"
        else:
            self.state.winner = " & ".join(winners)
            
        self.update_ui_state()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()
