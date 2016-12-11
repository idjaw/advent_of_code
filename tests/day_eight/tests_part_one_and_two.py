from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from day_eight.part_one_and_two import Display, get_data


class TestDisplay(TestCase):
    def setUp(self):
        self.display = Display(7, 3)

    def test_pixel_count_is_correct(self):
        self.display.enable_pixels(row=2, col=3)

        self.display.rotation('column', 1, 1)

        self.display.rotation('row', 0, 4)

        self.display.rotation('column', 1, 1)

        self.assertEqual(6, self.display.enabled_pixel_count())


mock_data = dedent("""rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=3 by 2
rect 3x2
rotate row y=0 by 3
rotate column x=1 by 6
""")

expected_structure = [
    {
        'rect': (1, 1),
        'ops': [{
            'rc': 'row',
            'pos': 0,
            'rot': 5
        }]
    },
    {
        'rect': (1, 1),
        'ops': [{
            'rc': 'row',
            'pos': 3,
            'rot': 2
        }]
    },
    {
        'rect': (3, 2),
        'ops': [
            {
                'rc': 'row',
                'pos': 0,
                'rot': 3
            },
            {
                'rc': 'column',
                'pos': 1,
                'rot': 6
            },
        ]
    }

]


class TestGetData(TestCase):
    @patch('builtins.open', mock_open(read_data=mock_data))
    def test_get_data(self):
        actual_data = get_data('some_input')

        for i, expected_data in enumerate(expected_structure):
            self.assertEqual(
                expected_data['rect'],
                actual_data[i]['rect']
            )
            for j, expected_ops in enumerate(expected_data['ops']):
                self.assertDictEqual(
                    expected_ops,
                    actual_data[i]['ops'][j]
                )
