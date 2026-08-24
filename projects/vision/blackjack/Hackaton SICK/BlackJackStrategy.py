
def get_card_value(card):
    """
    Returns the numeric value of a card.
    10, J, Q, K are 10. A is 11 (default for initial check).
    """
    card = str(card).upper().strip()
    if card in ['J', 'Q', 'K']:
        return 10
    if card in ['A', 'AS']:
        return 11
    if card.isdigit():
        val = int(card)
        if 2 <= val <= 10:
            return val
    return 0 # Invalid

def get_strategy_action(c1, c2, dealer_card):
    """
    Determines the action based on the chart provided.
    c1, c2: Player cards (str)
    dealer_card: Dealer card (str)
    
    Returns: "Tirer", "Rester", "Doubler", "Split", "Abandon"
    """
    v1 = get_card_value(c1)
    v2 = get_card_value(c2)
    d_val = get_card_value(dealer_card)
    
    if v1 == 0 or v2 == 0 or d_val == 0:
        return "Erreur: Carte invalide"
    
    # Check for Pair
    # Note: J and Q are both 10, so they are a pair of 10s technically.
    # However, standard strategies usually refer to rank pairs (J-J, 7-7).
    # But usually 10-J is treated as 20 value, not split.
    # The chart has "10-10", "9-9"...
    # We will assume strictly same rank for splitting 2-9 and A.
    # For 10s, any two value 10 cards make 20, usually treated as Stand.
    # Let's check if strictly same string or same value.
    # Chart says "10-10". It usually implies any 10-value cards.
    # But I'll stick to Value equality for pairs, since 10-K is never split anyway (it's 20, Stand).
    
    is_pair = (v1 == v2)
    
    # Dealer column index map for easier range checking
    # d_val: 2..10, 11(A)
    
    # === PAIRS ===
    if is_pair:
        # Pair of Aces
        if v1 == 11: 
            return "Split"
        
        # Pair of 10s (20)
        if v1 == 10:
            return "Rester"
            
        # Pair of 9s (18)
        if v1 == 9:
            # 2-6: S, 7: R, 8-9: S, 10-A: R
            if 2 <= d_val <= 6: return "Split"
            if d_val == 7: return "Rester"
            if 8 <= d_val <= 9: return "Split"
            return "Rester"
            
        # Pair of 8s (16)
        if v1 == 8:
            return "Split"
            
        # Pair of 7s (14)
        if v1 == 7:
            # 2-7: S, 8-A: T
            if 2 <= d_val <= 7: return "Split"
            return "Tirer"
            
        # Pair of 6s (12)
        if v1 == 6:
            # 2: T, 3-6: S, 7-A: T
            if d_val == 2: return "Tirer"
            if 3 <= d_val <= 6: return "Split"
            return "Tirer"
            
        # Pair of 5s (10)
        if v1 == 5:
            # 2-9: D, 10-A: T
            if 2 <= d_val <= 9: return "Doubler"
            return "Tirer"
            
        # Pair of 4s (8)
        if v1 == 4:
            # Chart reading: Looks like T everywhere?
            # Re-checking logic: 4-4 usually has splits/doubles in some rules, 
            # but user chart shows Line 4-4 as mostly Green (T).
            # Wait, let's look at 5 and 6 columns again on the crop.
            # Row 4-4: All Green.
            return "Tirer"
            
        # Pair of 3s (6) and 2s (4)
        if v1 == 3 or v1 == 2:
            # Row 3-3/2-2: 2-3: T, 4-7: S, 8-A: T
            if 2 <= d_val <= 3: return "Tirer"
            if 4 <= d_val <= 7: return "Split"
            return "Tirer"

    # === SOFT TOTALS ===
    # Has an Ace, and the other card is not an Ace (already handled in pairs).
    # Since we have only 2 cards, one is Ace(11) and other is X.
    # Total is 11 + X.
    if v1 == 11 or v2 == 11:
        other = v2 if v1 == 11 else v1
        # other is between 2 and 9 (if 10, it's Blackjack/21, usually Stand/Win, checked below)
        # Chart rows: "A2", "A3"... "A8-A9-A10"
        
        # A8 (19), A9 (20), A10 (21) -> Rester
        if other >= 8:
            return "Rester"
            
        # A7 (18)
        if other == 7:
            # 2: R, 3-6: D, 7-8: R, 9-A: T
            if d_val == 2: return "Rester"
            if 3 <= d_val <= 6: return "Doubler"
            if 7 <= d_val <= 8: return "Rester"
            return "Tirer"
            
        # A6 (17)
        if other == 6:
            # 2: T, 3-6: D, 7-A: T
            if d_val == 2: return "Tirer"
            if 3 <= d_val <= 6: return "Doubler"
            return "Tirer"
            
        # A5 (16) and A4 (15)
        if other == 5 or other == 4:
            # 2-3: T, 4-6: D, 7-A: T
            if 2 <= d_val <= 3: return "Tirer"
            if 4 <= d_val <= 6: return "Doubler"
            return "Tirer"
            
        # A3 (14) and A2 (13)
        if other == 3 or other == 2:
            # 2-4: T, 5-6: D, 7-A: T
            if 2 <= d_val <= 4: return "Tirer"
            if 5 <= d_val <= 6: return "Doubler"
            return "Tirer"

    # === HARD TOTALS ===
    total = v1 + v2
    
    # 17 or more
    if total >= 17:
        return "Rester"
        
    # 16
    if total == 16:
        # 2-6: R, 7-8: T, 9-A: Abandon
        if 2 <= d_val <= 6: return "Rester"
        if 7 <= d_val <= 8: return "Tirer"
        return "Abandon"
        
    # 15
    if total == 15:
        # 2-6: R, 7-9: T, 10: Abandon, A: T (Strange reading but obeying chart interpretation)
        # Correction: Row 15. Col 10 is Purple (A). Col A is Green (T).
        if 2 <= d_val <= 6: return "Rester"
        if 7 <= d_val <= 9: return "Tirer"
        if d_val == 10: return "Abandon"
        return "Tirer" # vs Ace
        
    # 13 and 14
    if total == 13 or total == 14:
        # 2-6: R, 7-A: T
        if 2 <= d_val <= 6: return "Rester"
        return "Tirer"
        
    # 12
    if total == 12:
        # 2-3: T, 4-6: R, 7-A: T
        if 2 <= d_val <= 3: return "Tirer"
        if 4 <= d_val <= 6: return "Rester"
        return "Tirer"
        
    # 11
    if total == 11:
        # 2-10: D, A: T
        if 2 <= d_val <= 10: return "Doubler"
        return "Tirer"
        
    # 10
    if total == 10:
        # 2-9: D, 10-A: T
        if 2 <= d_val <= 9: return "Doubler"
        return "Tirer"
        
    # 9
    if total == 9:
        # 2: T, 3-6: D, 7-A: T
        if d_val == 2: return "Tirer"
        if 3 <= d_val <= 6: return "Doubler"
        return "Tirer"
        
    # 8 or less
    if total <= 8:
        return "Tirer"
        

    
    return "Erreur inconnue"

def get_decision_from_score(score, is_soft, dealer_card_val):
    """
    Derived logic from the 2-card strategy but applied to current total score.
    Used for Hitting/Staying after the first 2 cards.
    """
    # Dealer value should be int (2-11)
    d_val = dealer_card_val
    if d_val == 1: d_val = 11 # Treat Ace as 11 for lookup

    if is_soft:
        # Soft Totals (Ace counted as 11)
        # Score is 13 (A,2) to 21 (A,10) - technically 12(A,A) is treated as 12 soft? No, 12 is 2 or 12.
        # Let's map score to actions based on the chart logic
        
        if score >= 19: # A8, A9, A10 -> Rester
            return "Rester"
        
        if score == 18:
            # A7
            # 2: R, 3-6: D(->H/S?), 7-8: R, 9-A: T
            # Mapping pure Hit/Stay:
            # Double usually means good hand -> Hit (to get more money) or Stay?
            # Actually Double on Soft 18 (vs 3-6) means you expect a high card (10) -> 18 becomes 18? No.
            # You double soft 18 because you might get A, 2, 3, 10...
            # Standard Basic Strategy: Soft 18 vs 2,7,8 -> Stay. vs 3-6 -> Double (treat as Hit if no double). vs 9,10,A -> Hit.
            # For this project "Hit or Stay" only:
            # vs 3-6 (Double): We should probably STAY if we can't double? 
            # Or HIT? 
            # Actually, standard rule: If cannot double, Soft 18 vs 3-6 -> STAND.
            # So:
            if 2 <= d_val <= 8: return "Rester"
            return "Tirer"
            
        if score == 17:
             # A6. Double 3-6. Otherwise Hit.
             # If no double: Hit.
             return "Tirer"
             
        if score <= 16:
            # A2-A5. Double 4-6 (or 5-6). Otherwise Hit.
            # If no double: Hit.
            return "Tirer"
            
    else:
        # Hard Totals
        if score >= 17:
            return "Rester"
            
        if score == 16:
            # 2-6: R, 7-A: T
            if 2 <= d_val <= 6: return "Rester"
            # Special surrender logic in chart? 16 vs 9/10/A -> Abandon.
            # Abandon -> Hit (try to save it) or Stay (surrender)?
            # Surrender means you give up. Equivalent to "I think I will lose".
            # If forced to play: Hit (statistically slightly better than standing on 16 vs 10, though you bust often).
            return "Tirer"
            
        if score == 15:
            # 2-6: R, 7-A: T
            if 2 <= d_val <= 6: return "Rester"
            return "Tirer"
            
        if score == 13 or score == 14:
            # 2-6: R, 7-A: T
            if 2 <= d_val <= 6: return "Rester"
            return "Tirer"
            
        if score == 12:
            # 2-3: T, 4-6: R, 7-A: T
            if 4 <= d_val <= 6: return "Rester"
            return "Tirer"
            
        if score <= 11:
            # Always hit (or double)
            return "Tirer"
            
    return "Rester" # Default fallback


def get_optimal_move(player_cards_list, dealer_card_str):
    """
    Main entry point for the Application.
    Returns strictly "Hit" or "Stay" (or "Tirer"/"Rester").
    """
    # 1. Calculate Score
    # We can't easily reuse GameState logic here without circular imports or code duplication.
    # I'll implement a lightweight scorer here or rely on the caller to pass score.
    # But the prompt asks for this file to determine the decision.
    
    # Let's use the local get_card_value
    total = 0
    aces = 0
    for c in player_cards_list:
        v = get_card_value(c)
        if v == 11:
            aces += 1
        total += v
        
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
        
    is_soft = (aces > 0)
    
    # 2. Get Dealer Value
    d_val = get_card_value(dealer_card_str)
    
    # 3. Get Decision
    # If 2 cards, use the chart logic (handles Pairs)
    # If >2 cards, use Score logic
    
    action = ""
    if len(player_cards_list) == 2:
        action = get_strategy_action(player_cards_list[0], player_cards_list[1], dealer_card_str)
    else:
        action = get_decision_from_score(total, is_soft, d_val)
        
    # 4. Filter to Hit/Stay
    # Mapping:
    # Tirer -> Hit
    # Rester -> Stay
    # Doubler -> Hit (since we can't double, hitting is usually the alternative for value generation, though sometimes Strategy varies. But usually Double means "Good hand, want more money", so hitting is correct).
    # Split -> (This is tricky. If we "ignore" split, we play the hand as a hard total or soft total).
    # Abandon -> Hit (Fighting chance).
    
    if action in ["Tirer", "Doubler"]:
        return "Hit"
    if action == "Rester":
        return "Stay"
    if action == "Split":
        # Check total as hard/soft
        # e.g. 8,8 -> 16. 
        # e.g. A,A -> 12 (Soft).
        # Fallback to score logic
        fallback = get_decision_from_score(total, is_soft, d_val)
        if fallback in ["Tirer", "Doubler"]: return "Hit"
        return "Stay"
        
    if action == "Abandon":
        return "Hit" # Or Stay? 16 vs 10. Book says Hit if Surrender not allowed.
        
    return "Stay" # Default


