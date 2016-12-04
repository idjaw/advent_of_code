from unittest.mock import mock_open
from unittest.mock import patch
from unittest import TestCase

from day_one.common import get_directions, move, new_orientation
from day_one.part_one import get_final_position, get_blocks_from_destination, \
    main


class TestGetDirections(TestCase):
    @patch('builtins.open', mock_open(read_data='L1, L2, R345'))
    def test_read_input(self):
        data = get_directions('some_file')

        self.assertEqual(data, [('L', 1), ('L', 2), ('R', 345)])


class TestMove(TestCase):

    def test_move_in_a_direction(self):
        current_direction = (-1, 0)
        current_coordinates = (4, 2)

        current_coordinate = move(current_direction, current_coordinates, 5)

        self.assertEqual(current_coordinate, (-1, 2))

    def test_move_twice(self):
        current_direction = (0, 1)
        current_coordinates = (0, 0)

        current_coordinates = move(
            current_direction, current_coordinates, 2
        )

        self.assertEqual(current_coordinates, (0, 2))

        current_direction = (1, 0)

        current_coordinates = move(
            current_direction, current_coordinates, 3
        )

        self.assertEqual(current_coordinates, (3, 2))


class TestOrientation(TestCase):
    def test_set_correct_direction_when_moving_north_to_west(self):
        currently_facing = new_orientation((0, 1), 'L')

        self.assertEqual(currently_facing, (-1, 0))

    def test_set_correct_direction_when_moving_north_to_east(self):
        currently_facing = new_orientation((0, 1), 'L')

        self.assertEqual(currently_facing, (-1, 0))

    def test_set_correct_direction_when_moving_west_to_north(self):
            currently_facing = new_orientation((-1, 0), 'R')

            self.assertEqual(currently_facing, (0, 1))

    def test_set_correct_direction_when_moving_west_to_south(self):
            currently_facing = new_orientation((-1, 0), 'L')

            self.assertEqual(currently_facing, (0, -1))

    def test_set_correct_direction_when_moving_south_to_west(self):
            currently_facing = new_orientation((0, -1), 'R')

            self.assertEqual(currently_facing, (-1, 0))

    def test_set_correct_direction_when_moving_south_to_east(self):
            currently_facing = new_orientation((0, -1), 'L')

            self.assertEqual(currently_facing, (1, 0))

    def test_set_correct_direction_when_moving_east_to_south(self):
            currently_facing = new_orientation((1, 0), 'R')

            self.assertEqual(currently_facing, (0, -1))

    def test_set_correct_direction_when_moving_east_to_north(self):
            currently_facing = new_orientation((1, 0), 'L')

            self.assertEqual(currently_facing, (0, 1))

    def test_set_correct_direction_after_several_moves(self):
        movements = ['L', 'R', 'R', 'L', 'L', 'L']
        current_orientation = (0, 1)
        expected_orientation = [
            (-1, 0), (0, 1), (1, 0), (0, 1), (-1, 0), (0, -1)
        ]
        for i, movement in enumerate(movements):
            current_orientation = new_orientation(current_orientation, movement)
            self.assertEqual(current_orientation, expected_orientation[i])


class TestGettingFinalDestination(TestCase):
    def test_get_final_position_scenario_one(self):
        directions = [('R', 2), ('L', 3)]

        final_position = get_final_position(
            (0, 1), (0, 0), directions
        )

        self.assertEqual(final_position, (2, 3))

    def test_get_final_position_scenario_two(self):
        directions = [('R', 2), ('R', 2), ('R', 2)]
        final_position = get_final_position(
            (0, 1), (0, 0), directions
        )

        self.assertEqual(final_position, (0, -2))

    def test_get_final_position_scenario_three(self):
        directions = [('R', 5), ('L', 5), ('R', 5), ('R', 3)]
        final_position = get_final_position(
            (0, 1), (0, 0), directions
        )

        self.assertEqual(final_position, (10, 2))


class TestGetBlocksFromDestination(TestCase):
    @patch('day_one.part_one.get_final_position')
    def test_get_blocks_from_destination(self, mock_get_final_position):
        mock_get_final_position.return_value = (10, 2)

        blocks = get_blocks_from_destination(
            'some_coordinate', 'some_direction', 'some_series_of_directions'
        )
        self.assertEqual(blocks, 12)


class TestMain(TestCase):
    @patch('day_one.part_one.get_directions')
    def test_moving_sets_proper_new_coordinates(self, mock_get_directions):
        mock_get_directions.return_value = [('R', 2), ('L', 3)]

        blocks = main()

        self.assertEqual(blocks, 5)
