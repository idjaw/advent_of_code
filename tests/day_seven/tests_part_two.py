from textwrap import dedent
from unittest import TestCase
from unittest.mock import mock_open, patch

from day_seven.part_two import supports_ssl, valid_accumulator


class TestSupportsSSL(TestCase):
    def test_valid_case_a(self):
        self.assertTrue(supports_ssl('aba[bab]xyz'))

    def test_invalid_case_a(self):
        self.assertFalse(supports_ssl('xyx[xyx]xyx'))

    def test_valid_case_b(self):
        self.assertTrue(supports_ssl('aaa[kek]eke'))

    def test_valid_case_c(self):
        self.assertTrue(supports_ssl('zazbz[bzb]cdb'))


mock_data = dedent("""aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
""")


class TestValidSSLCount(TestCase):
    @patch('builtins.open', mock_open(read_data=mock_data))
    def test_total_count_is_valid(self):
        self.assertEqual(3, valid_accumulator('some_file'))
