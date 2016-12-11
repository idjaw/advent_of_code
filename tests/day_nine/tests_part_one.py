from unittest import TestCase

from day_nine.part_one import text_decompression


class TestDecompression(TestCase):

    def test_decompression_is_successful_a(self):
        self.assertEqual('ADVENT', text_decompression('ADVENT'))

    def test_decompression_is_successful_b(self):
        self.assertEqual('ABBBBBC', text_decompression('A(1x5)BC'))

    def test_decompression_is_successful_c(self):
        self.assertEqual('XYZXYZXYZ', text_decompression('(3x3)XYZ'))

    def test_decompression_is_successful_d(self):
        self.assertEqual('ABCBCDEFEFG', text_decompression('A(2x2)BCD(2x2)EFG'))

    def test_decompression_is_successful_e(self):
        self.assertEqual(
            'X(3x3)ABC(3x3)ABCY',
            text_decompression('X(8x2)(3x3)ABCY')
        )



