import unittest

from units import Match, Set, Game

class TesMatchUnit(unittest.TestCase):
    def test_game_constructor(self):
        game = Game()
        self.assertIsNotNone(game)

        score_recorder = game.get_score_recorder()
        for k in score_recorder.keys():
            self.assertTrue(k in range(1, 3))
        for v in score_recorder.values():
            self.assertEqual(v, 0)

    def test_set_constructor(self):
        s = Set()
        self.assertIsNotNone(s)
        self.assertIsNotNone(s.get_current_game())

        score_recorder = s.get_score_recorder()
        for k in score_recorder.keys():
            self.assertTrue(k in range(1, 3))
        for v in score_recorder.values():
            self.assertEqual(v, 0)

    def test_match_constructor(self):
        match = Match()
        self.assertIsNotNone(match)
        self.assertIsNotNone(match.get_current_set())

        score_recorder = match.get_score_recorder()
        self.assertIsNotNone(score_recorder)
        for k in score_recorder.keys():
            self.assertTrue(k in range(1, 3))
        for v in score_recorder.values():
            self.assertEqual(v, 0)

    def test_score_win_point(self):
        match = Match()
        score_recorder = match.get_score_recorder()
        current_set = match.get_current_set()
        current_game = current_set.get_current_game()

        match.win_score(1)
        self.assertEqual(current_game.get_score_recorder()[1], 1)

    def test_score_win_set(self):
        match = Match()
        score_recorder = match.get_score_recorder()
        current_set = match.get_current_set()
        current_game = current_set.get_current_game()

        for _ in range(5):
            match.win_score(1)
        self.assertEqual(current_set.get_score_recorder()[1], 1)
        current_new_game = current_set.get_current_game()
        self.assertNotEqual(current_new_game, current_game)
        self.assertEqual(current_new_game.get_score_recorder()[1], 0)

    def test_score_win_match(self):
        match = Match()
        score_recorder = match.get_score_recorder()
        current_set = match.get_current_set()
        current_game = current_set.get_current_game()

        for _ in range(5*6):
            match.win_score(1)

        self.assertEqual(match.get_score_recorder()[1], 1)

        current_new_set = match.get_current_set()
        self.assertNotEqual(current_new_set, current_set)
        self.assertEqual(current_new_set.get_score_recorder()[1], 0)

        current_new_game = current_set.get_current_game()
        self.assertNotEqual(current_new_game, current_game)
        self.assertEqual(current_new_game.get_score_recorder()[1], 0)


if __name__ == '__main__':
    unittest.main()