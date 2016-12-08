from unittest import TestCase

from day_five.part_one import get_code


class TestGetCode(TestCase):
    def test_correct_code(self):
        self.assertEqual("18f", get_code("abc"))
