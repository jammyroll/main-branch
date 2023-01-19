import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_score

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    # Test latest score (the last thing in the list)
    def test_latest_score_is_right(self):
        self.assertEqual(6,latest(high_score))
    # Test personal best (the highest score in the list)
    def test_check_and_return_high_score(self):
        self.assertEqual(6,personal_best(high_score))
    # Test top three from list of scores
    def test_top_three_score(self):
        self.assertEqual([6,5,4],personal_top_three(high_score))
    # Test ordered from highest tp lowest
    
    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
