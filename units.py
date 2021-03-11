class MatchUnit:
    NUM_OF_PLAYER = 2

    def __init__(self):
        self._initiate_scores_recorder()
        self._start_new_unit()
        self.winner = None

    def _start_new_unit(self):
        return

    def _initiate_scores_recorder(self):
        self.scores_recorder = {player_id:0 for player_id in range(1, MatchUnit.NUM_OF_PLAYER+1)}

    def get_winner(self):
        return self.winner

    def get_score_recorder(self):
        return self.scores_recorder

class Match(MatchUnit):
    WIN_CONDITION = 3

    def _start_new_unit(self):
        self.current_set = Set()
        self.sets_history = [self.current_set]

    def get_current_set(self):
        return self.current_set

    def get_sets_history(self):
        return self.sets_history

class Set(MatchUnit):
    WIN_CONDITION = 6

    def _start_new_unit(self):
        self.current_game = Game()
        self.games_history = [self.current_game]

    def get_current_game(self):
        return self.current_game

    def get_games_history(self):
        return self.games_history

class Game(MatchUnit):
    WIN_CONDITION = 5