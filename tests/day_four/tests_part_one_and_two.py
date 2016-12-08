from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from day_four.part_one_and_two import get_data, get_most_common,\
    sum_of_valid_sector_ids

from day_four.part_one_and_two import shift_cipher

mock_inputs = """
vxupkizork-sgmtkzoi-pkrrehkgt-zxgototm-644[kotgr]
mbiyqoxsm-pvygob-nocsqx-900[obmqs]
"""


class TestGetData(TestCase):

    @patch('builtins.open', mock_open(read_data=mock_inputs))
    def test_get_data(self):
        self.assertEqual(
            [
                ("vxupkizorksgmtkzoipkrrehkgtzxgototm", 644, "kotgr"),
                ("mbiyqoxsmpvygobnocsqx", 900, "obmqs")
            ],
            get_data('some_file')

        )


class TestGetMostCommon(TestCase):
    def test_get_most_common(self):
        test_input = "aaaaabbbzyx"
        res = get_most_common(test_input)
        self.assertEqual('abxyz', res)

    def test_get_most_common_2(self):
        test_input = "totallyrealroom"
        res = get_most_common(test_input)
        self.assertEqual('loart', res)

mock_data = dedent("""
        aaaa-bbb-z-y-x-123[abxyz]
        a-b-c-d-e-f-g-h-987[abcde]
        not-a-real-room-404[oarel]
        totally-real-room-200[decoy]
        """)


class TestDecoding(TestCase):
    def test_is_real(self):
        self.assertTrue(get_most_common("aaaaabbbzyx") == "abxyz")
        self.assertTrue(get_most_common("abcdefgh") == "abcde")
        self.assertTrue(get_most_common("notarealroom") == "oarel")
        self.assertFalse(get_most_common("totallyrealroom") == "decoy")

    @patch('builtins.open', mock_open(read_data=mock_data))
    def test_1(self):
        self.assertEqual(sum_of_valid_sector_ids('meh'), 1514)


class TestShiftCipher(TestCase):
    def test_works(self):
        self.assertEqual(
            shift_cipher('qzmtzixmtkozyivhz', 343), "veryencryptedname"
        )
