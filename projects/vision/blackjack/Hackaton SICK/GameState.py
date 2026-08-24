class GameState:
    def __init__(self):
        self.dealer_cards = []
        self.p1_cards = []
        self.p2_cards = []
        
        # 'player1', 'player2', 'dealer', or None/GameOver
        self.current_player = 'player1' 
        self.game_over = False
        self.winner = None

    def reset(self):
        self.dealer_cards = []
        self.p1_cards = []
        self.p2_cards = []
        self.current_player = 'player1'
        self.game_over = False
        self.winner = None

    def set_initial_cards(self, dealer, p1, p2):
        """
        Sets the initial cards from the first trigger.
        Note: The camera sends 3 cards. Dealer, P1, P2.
        """
        self.dealer_cards = [dealer] if dealer else []
        self.p1_cards = [p1] if p1 else []
        self.p2_cards = [p2] if p2 else []

    def add_card(self, player, card):
        if player == 'player1':
            self.p1_cards.append(card)
        elif player == 'player2':
            self.p2_cards.append(card)
        elif player == 'dealer':
            self.dealer_cards.append(card)

    def calculate_score(self, cards):
        """
        Calculates score and returns (score, is_soft).
        'is_soft' is True if there is an Ace being counted as 11.
        """
        total = 0
        aces = 0
        
        for card in cards:
            val = self._get_card_value(card)
            total += val
            if val == 11:
                aces += 1
        
        # Adjust for Aces
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
            
        is_soft = (aces > 0)
        return total, is_soft

    def is_blackjack(self, cards):
        if len(cards) != 2:
            return False
        score, _ = self.calculate_score(cards)
        return score == 21

    def _get_card_value(self, card_str):
        """
        Parses card string to value.
        2-10 -> int
        J, Q, K -> 10
        As (or A) -> 11
        """
        c = card_str.upper().strip()
        if "NO CLASS" in c:
            return 0
        if c in ['J', 'Q', 'K']:
            return 10
        if c in ['AS', 'A']: # Handle both 'As' (French) and 'A'
            return 11
        
        if c.isdigit():
            val = int(c)
            # Just in case 1 is sent for Ace (though prompt says As=11 default)
            # or data is dirty.
            return val
        
        # Fallback
        return 0

    def get_status(self):
        p1_score, p1_soft = self.calculate_score(self.p1_cards)
        p2_score, p2_soft = self.calculate_score(self.p2_cards)
        d_score, d_soft = self.calculate_score(self.dealer_cards)
        
        return {
            "p1": {"cards": self.p1_cards, "score": p1_score, "soft": p1_soft},
            "p2": {"cards": self.p2_cards, "score": p2_score, "soft": p2_soft},
            "dealer": {"cards": self.dealer_cards, "score": d_score, "soft": d_soft},
            "current": self.current_player
        }
