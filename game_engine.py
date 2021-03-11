from units import Match
from score_board import ScoreBoard

class MatchEngine:
    def __init__(self):
        self.scoreboard = ScoreBoard()
        self.is_end = False
        self.match = None

    def run(self, verbose=False):
        self.match = Match()
        
        if verbose:
            print("Match starts!!!")

        while (not self.is_end):
            if verbose:
                print(f"Which player scores the next point? (Options: {list(range(1,Match.NUM_OF_PLAYER+1))})\n")
            
            user_input = input()
            self.match.win_score(int(user_input))

            if verbose:
                self.print_score_records() # TODO: print scoreboard

            winner = self.match.get_winner()
            if winner:
                self.end(winner)

        if verbose:
            print(f"{'-'*10}\nEND!!! Winner is player {winner}.")
        else:
            print(winner)

    def end(self, winner):
        self.is_end = True
        
    def print_score_records(self):
        print(f"Match scores: {self.match.get_score_recorder()}")
        current_set = self.match.get_current_set()
        print(f"Set scores: {current_set.get_score_recorder()}")
        current_game = current_set.get_current_game()
        print(f"Game scores: {current_game.get_score_recorder()}")
