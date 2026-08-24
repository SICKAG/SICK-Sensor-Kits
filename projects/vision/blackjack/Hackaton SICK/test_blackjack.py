import unittest
from GameState import GameState
from BlackJackStrategy import get_card_value, get_optimal_move

class TestBlackjack(unittest.TestCase):
    def test_card_values(self):
        self.assertEqual(get_card_value("10"), 10)
        self.assertEqual(get_card_value("As"), 11)
        self.assertEqual(get_card_value("A"), 11)
        self.assertEqual(get_card_value("AS"), 11)
        self.assertEqual(get_card_value("K"), 10)
        self.assertEqual(get_card_value("2"), 2)

    def test_gamestate_scores(self):
        state = GameState()
        # Test Soft 21 (Blackjack)
        score, soft = state.calculate_score(["As", "K"])
        self.assertEqual(score, 21)
        self.assertTrue(soft)
        
        # Test Hard 21
        score, soft = state.calculate_score(["10", "5", "6"])
        self.assertEqual(score, 21)
        self.assertFalse(soft)
        
        # Test Bust with Aces
        # A + A + 9 = 11 + 1 + 9 = 21
        score, soft = state.calculate_score(["As", "As", "9"])
        self.assertEqual(score, 21)
        self.assertTrue(soft) # One Ace is 11, one is 1. (11+1+9=21). Correct.
        
        # A + A + A = 13 (11+1+1) or 3? 13.
        score, soft = state.calculate_score(["As", "AS", "A"])
        self.assertEqual(score, 13)
        self.assertTrue(soft) # 11+1+1

        # A + A + A + 9 = 12 (1+1+1+9) -> 12
        score, soft = state.calculate_score(["As", "As", "As", "9"])
        self.assertEqual(score, 12)
        self.assertFalse(soft) # All aces are 1

    def test_strategy(self):
        # Test optimal move mapping
        
        # Hard 10 vs 5 -> Double -> Hit
        self.assertEqual(get_optimal_move(["5", "5"], "5"), "Hit") # Strategy says Double -> Hit
        
        # Hard 17 vs 6 -> Stay
        self.assertEqual(get_optimal_move(["10", "7"], "6"), "Stay")
        
        # Hard 16 vs 7 -> Hit
        self.assertEqual(get_optimal_move(["10", "6"], "7"), "Hit")
        
        # Soft 18 (A,7) vs 9 -> Hit
        self.assertEqual(get_optimal_move(["As", "7"], "9"), "Hit")
        
        # Soft 18 (A,7) vs 2 -> Stay
        self.assertEqual(get_optimal_move(["As", "7"], "2"), "Stay")

if __name__ == '__main__':
    unittest.main()
