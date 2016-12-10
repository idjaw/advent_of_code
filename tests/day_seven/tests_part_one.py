from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from day_seven.part_one import is_valid_tls, valid_accumulator

mock_data = dedent("""abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
""")


class TestValidTLS(TestCase):
    def test_abba_outside_brackes_supports_tls(self):
        self.assertTrue(is_valid_tls('abba[mnop]qrst'))
        self.assertTrue(is_valid_tls('abcd[abcd]xyyx'))

    def test_is_valid_tls(self):
        self.assertTrue(is_valid_tls("abba[mnop]qrst"))

    def test_is_invalid_tls_d(self):
        self.assertFalse(is_valid_tls("ab[mnop]bast"))

    def test_is_invalid_tls_a(self):
        self.assertFalse(is_valid_tls("abcd[bddb]xyyx"))

    def test_is_invalid_tls_b(self):
        self.assertFalse(is_valid_tls("aaaa[qwer]tyui"))

    def test_is_invalid_tls_c(self):
        self.assertFalse(is_valid_tls("abcd[abddbgg]xyyx"))

    def test_is_valid_tls_b(self):
        self.assertTrue(is_valid_tls("ioxxoj[asdfgh]zxcvbn"))

    def test_is_invalid_tls(self):
        self.assertFalse(is_valid_tls("abba[mnop]a[qeabbars]xysd"))

    def test_is_valid_tls_c(self):
        self.assertTrue(is_valid_tls("aabbaa[mnop]a[cftr]xysd"))

    def test_some_invalid_test(self):
        self.assertFalse(is_valid_tls("ioxxoj[asdfgh]jocv[blojjo]abbn"))

    def test_some_other_invalid_test(self):
        self.assertFalse(is_valid_tls("tjwhvzwmhppijorvm[egqxqiycnbtxrii]ojmqyikithgouyu[lrllrgezaulugvlj]jdsrysawxkpglgg[mpvkikuabwucwlpqf]cmzkcdnrhwjmfgbmlq"))

    def test_the_valid_test_to_fix_things_finally(self):
        self.assertTrue(is_valid_tls("bcbwbvyvqpozfig[twwsbwyhvfaddwo]jogvkczzowocmkwwlla[yedsazzkeklftvohfqz]tghtcjemmehumuyxar"))


class GetTotalValidTLS(TestCase):
    @patch('builtins.open', mock_open(read_data=mock_data))
    def test_get_total_valid_tls(self):
        self.assertEqual(2, valid_accumulator('some_file'))

