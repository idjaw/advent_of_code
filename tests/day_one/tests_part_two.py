from unittest import TestCase

from day_one.part_two import get_location


class TestTrackPath(TestCase):
    def test_track_path(self):
        current_orientation = 0, 1
        current_position = 0, 0
        directions = [('R', 8), ('R', 4), ('R', 4), ('R', 8)]
        self.assertEqual(
            (4, 0),
            get_location(current_orientation, current_position, directions)
        )
