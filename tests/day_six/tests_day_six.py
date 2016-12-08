from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from day_six.part_one import get_code

data = dedent("""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
""")


class TestGetCode(TestCase):
    @patch('builtins.open', mock_open(read_data=data))
    def test_get_code(self):
        self.assertEqual("easter", get_code('some_input'))

