from unittest import TestCase
from unittest.mock import patch, mock_open

from day_two.part_one import move, get_code

keypad = [
    '123',
    '456',
    '789'
]


class TestKeypadSolver(TestCase):

    def test_move_once_up(self):
        pos = move((1, 1), "U")
        self.assertEqual((0, 1), pos)

    def test_move_once_down(self):
        pos = move((1, 1), "D")
        self.assertEqual((2, 1), pos)

    def test_move_once_left(self):
        pos = move((1, 1), "L")
        self.assertEqual((1, 0), pos)

    def test_move_once_right(self):
        pos = move((1, 1), "R")
        self.assertEqual((1, 2), pos)

    def test_move_u_l_results_in_1(self):
        pos = move((1, 1), "UL")
        self.assertEqual((0, 0), pos)

    def test_move_u_u_u_u_l_d_u_results_in_0_0(self):
        pos = move((1, 1), "UUUULDU")
        self.assertEqual((0, 0), pos)

    def test_move_down_several_times_right_then_down_is_2_2(self):
        pos = move((1, 1), "RRRRRRRRRRRRRRRRRRRRRD")
        self.assertEqual((2, 2), pos)

    def test_sample_input(self):
        pos = move((1, 1), "DUURRDRRURUUUDLRUDDLLLU")
        self.assertEqual((1, 0), pos)


class TestGetCode(TestCase):

    @patch('builtins.open', mock_open(read_data="UUUULDU\nLRDLRDLLLDUDDU"))
    def test_send_two_sequences_returns_proper_code(self):
        code = get_code((1, 1), 'some_file')

        self.assertEqual("14", code)
