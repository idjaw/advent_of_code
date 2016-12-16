from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from day_three.common import is_valid_triangle, valid_triangle_count
from day_three.part_one import get_data


class TestGetData(TestCase):
    mock_inputs = dedent("""775  785  361
    622  375  125""")

    @patch('builtins.open', mock_open(read_data=mock_inputs))
    def test_read_input(self):
        data = get_data('some_file')

        self.assertEqual(data, [[775,  785,  361], [622,  375,  125]])


class TestTriangles(TestCase):
    def test_is_a_valid_triangle(self):
        self.assertTrue(is_valid_triangle([4, 5, 6]))

    def test_3_3_5_is_a_valid_triangle(self):
        self.assertTrue(is_valid_triangle([3, 3, 5]))

    def test_3_3_6_is_an_invalid_triangle(self):
        self.assertFalse(is_valid_triangle([3, 6, 3]))

    def test_3_3_7_is_an_invalid_triangle(self):
        self.assertFalse(is_valid_triangle([3, 7, 3]))

    def test_is_a_invalid_triangle(self):
        self.assertFalse(is_valid_triangle([5, 25, 10]))


class TestFilterValidTriangles(TestCase):

    def test_only_valid_triangles_are_kept(self):
        triangles = [[6,  4,  5], [25,  5,  10]]
        filtered_triangles = valid_triangle_count(triangles)

        self.assertEqual(1, filtered_triangles)
