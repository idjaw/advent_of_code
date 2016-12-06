from unittest import TestCase
from unittest.mock import patch, mock_open

from day_three.part_two import get_data


class TestGetData(TestCase):
    mock_inputs = """
  775  785  361
  622  375  125
  275  485  661
  422  575  145
  945  785  391
  122  975  105
"""

    @patch('builtins.open', mock_open(read_data=mock_inputs))
    def test_get_data(self):
        self.assertEqual(
            sorted([
                [775, 622, 275], [422, 945, 122],
                [785, 375, 485], [575, 785, 975],
                [361, 125, 661], [145, 391, 105]
            ]),
            sorted(get_data('some_file'))
        )
