from bowling_game_exceptions import *

class Game:
    def __init__(self, frames_scores: list = []):
        self.frames_scores = frames_scores
   
    def validate_frames(self) -> None:
        if len(self.frames_scores) < 20:
            raise SmallInputException
        elif len(self.frames_scores) > 21:
            raise LargeInputException
        
    def roll(self, first_roll, second_roll):
        if first_roll < 0 or second_roll < 0:
            raise NegtaiveInputException
        elif first_roll == 10:
            if second_roll != 0:
                raise InvalidStrikeException
            else:
                return "X"
        elif first_roll + second_roll > 10:
            raise InvalidScoreException
        
        result = first_roll + second_roll
        return result if result != 10 else "/"
