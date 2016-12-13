from unittest import TestCase

from day_nine.part_two import text_decompression


class TestDecompression(TestCase):

    def test_decompression_is_successful_a(self):
        self.assertEqual(9, text_decompression('(3x3)XYZ'))

    def test_decompression_is_successful_b(self):
        self.assertEqual(20, text_decompression('X(8x2)(3x3)ABCY'))

    def test_decompression_is_successful_c(self):
        self.assertEqual(
            241920,
            text_decompression('(27x12)(20x12)(13x14)(7x10)(1x12)A')
        )

    def test_decompression_is_successful_g(self):
        self.assertEqual(
            445,
            text_decompression(
                '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
            )
        )
