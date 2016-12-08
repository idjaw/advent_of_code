from unittest import TestCase

from day_five.part_two import get_code


class TestGetCode(TestCase):
    def test_correct_code(self):
        self.assertEqual("05ace8e3", get_code("abc"))
