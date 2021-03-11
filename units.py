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

    def update_winner(self):
        winner = list(filter(lambda item: item[1] == Match.WIN_CONDITION, self.scores_recorder.items()))
        if winner:
            self.winner = winner[0][0]

    # A player scores a set
    def win_set(self, player_id):
        self.scores_recorder[player_id]+=1
        self._start_new_unit()
        self.update_winner()

    # A player scores a point in a game
    def win_score(self, player_id):
        self.current_set.win_score(player_id)
        set_winner = self.current_set.winner # can be None
        if set_winner:
            self.win_set(set_winner)

    def get_current_set(self):
        return self.current_set

    def get_sets_history(self):
        return self.sets_history

class Set(MatchUnit):
    WIN_CONDITION = 6

    def _start_new_unit(self):
        self.current_game = Game()
        self.games_history = [self.current_game]

    def update_winner(self):
        records = list(self.scores_recorder.items())
        max_score_item = max(records, key=lambda x: x[1])
        if max_score_item[1] >= Set.WIN_CONDITION and abs(records[0][1] - records[1][1]) >= 2:
            self.winner = max_score_item[0]
            
    # A player scores a game
    def win_game(self, player_id):
        self.scores_recorder[player_id]+=1
        self._start_new_unit()
        self.update_winner()

    # A player scores a point in a game
    def win_score(self, player_id):
        self.current_game.win_score(player_id)
        game_winner = self.current_game.winner # can be None
        if game_winner:
            self.win_game(game_winner)

    def get_current_game(self):
        return self.current_game

    def get_games_history(self):
        return self.games_history

class Game(MatchUnit):
    WIN_CONDITION = 5

    def update_winner(self):
        records = list(self.scores_recorder.items())
        max_score_item = max(records, key=lambda x: x[1])
        if records[0][1] == records[1][1] == Game.WIN_CONDITION-1:
            for player_id in self.scores_recorder.keys():
                self.scores_recorder[player_id]-=1
        elif max_score_item[1] == Game.WIN_CONDITION:
            self.winner = max_score_item[0]

    # A player scores a point
    def win_score(self, player_id):
        self.scores_recorder[player_id]+=1
        self.update_winner()