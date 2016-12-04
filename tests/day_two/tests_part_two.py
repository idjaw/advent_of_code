from unittest import TestCase

from day_two.part_two import move

keypad = [
    '**1**',
    '*234*',
    '56789',
    '*ABC*',
    '**D**'
]


class TestKeypadSolver(TestCase):

    def test_move_once_up(self):
        pos = move((2, 0), "U")
        self.assertEqual((2, 0), pos)

    def test_move_once_down(self):
        pos = move((2, 0), "D")
        self.assertEqual((2, 0), pos)

    def test_move_once_left(self):
        pos = move((2, 0), "L")
        self.assertEqual((2, 0), pos)

    def test_move_once_right(self):
        pos = move((2, 0), "R")
        self.assertEqual((2, 1), pos)

    def test_move_r_r_r_r_r_u_u_u_results_in_9(self):
        pos = move((2, 0), "RRRRRUUU")
        self.assertEqual((2, 4), pos)
