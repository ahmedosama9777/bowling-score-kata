import unittest
from bowling_game import Game
from bowling_game_exceptions import *


class TestBowlingScore(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game()

    def test_create_game(self):
        frame_scores = [1, 2, 3]
        game = Game(frame_scores)
        self.assertEqual(game.frames_scores, frame_scores)

    def test_input_smaller_than_ten_frames(self):
        input = [1, 2, 3]
        self.game.frames_scores = input
        with self.assertRaises(SmallInputException):
            self.game.validate_frames()

    def test_input_larger_than_ten_frames(self):
        input = [x for x in range(22)]
        self.game.frames_scores = input
        with self.assertRaises(LargeInputException):
            self.game.validate_frames()

    def test_input_has_negative_numbers(self):
        with self.assertRaises(NegtaiveInputException):
            self.game.roll(-1, 1)
    
    def test_strike_not_followed_by_zero(self):
        with self.assertRaises(InvalidStrikeException):
            self.game.roll(10, 1)
    
    def test_frame_score_more_than_ten(self):
        with self.assertRaises(InvalidStrikeException):
            self.game.roll(10, 1)
    
    def test_roll_non_strike_non_stribe(self):
        result = self.game.roll(4, 5)
        self.assertEqual(result, 9)
    
    def test_stribe_score(self):
        result = self.game.roll(1, 9)
        self.assertEqual(result, "/")
    
    def test_strke_score(self):
        result = self.game.roll(10, 0)
        self.assertEqual(result, "X")
    
