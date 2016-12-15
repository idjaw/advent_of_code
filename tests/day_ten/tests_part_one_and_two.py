from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch, mock_open

from collections import defaultdict

from day_ten import part_one

mock_data = dedent("""value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
""")


mock_data_list = [
    "value 5 goes to bot 2",
    "bot 2 gives low to bot 1 and high to bot 0",
    "value 3 goes to bot 1",
    "bot 1 gives low to output 1 and high to bot 0",
    "bot 0 gives low to output 2 and high to output 0",
    "value 2 goes to bot 2"
]


class TestData(TestCase):

    def test_get_bot_creation_data(self):
        part_one.create_all_bot_data_and_get_instructions(mock_data_list)

        # test one
        self.assertEqual("1", part_one.devices.get('1').bot_id)
        self.assertEqual("output 1", part_one.devices.get('1').low)
        self.assertEqual("bot 0", part_one.devices.get('1').high)

    def test_create_all_bot_data_works_as_expected(self):
        part_one.create_all_bot_data_and_get_instructions(mock_data_list)

        self.assertEqual("output 1", part_one.devices["1"].low)
        self.assertEqual("bot 1", part_one.devices["2"].low)
        self.assertEqual("bot 0", part_one.devices["2"].high)

    @patch('builtins.open', mock_open(read_data=mock_data))
    @patch('day_ten.part_one.output_bot')
    def test_add_chips_works_as_expected(self, mock_output_bot):
        input_data = part_one.get_data('inputs.txt')
        instructions = part_one.create_all_bot_data_and_get_instructions(
            input_data
        )
        part_one.move_chips(instructions)

        mock_output_bot.assert_called_with(
            '{"bot_id": 2, "low": bot 1, "high": bot 0, "chips": [5, 2]}'
        )

    def test_send_low_sends_to_output_bin(self):

        part_one.devices = {
            "1": part_one.Bot(bot_id=1, low="output 0", high="bot 2")
        }

        part_one.devices["1"].chips = [1, 2]
        part_one.devices["1"].send_low()

        self.assertEqual({"0": [1]}, part_one.output_bins)

    def test_send_high_sends_to_output_bin(self):

        part_one.devices = {
            "1": part_one.Bot(bot_id=1, low="output 0", high="output 1")
        }

        part_one.devices["1"].chips = [1, 2]
        part_one.devices["1"].send_high()

        self.assertEqual({"1": [2]}, part_one.output_bins)

    def test_send_low_high_sends_to_correct_place(self):

        part_one.devices = {
            "1": part_one.Bot(bot_id=1, low="bot 2", high="output 1"),
            "2": part_one.Bot(bot_id=2, low="output 1", high="output 0")
        }

        part_one.devices["1"].chips = [1, 2]

        part_one.devices["1"].send_low()
        part_one.devices["1"].send_high()

        self.assertEqual([1], part_one.devices["2"].chips)
        self.assertEqual({"1": [2]}, part_one.output_bins)

    def tearDown(self):
        part_one.devices = {}
        part_one.output_bins = defaultdict(list)
