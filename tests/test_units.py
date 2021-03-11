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

if __name__ == '__main__':
    unittest.main()