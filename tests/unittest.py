from unittest import mock, TestCase

from project import Calculating_System

@mock.patch('project.Calculating_System.check_out', return_value=b'We have enough 11 kgs to supply for your offer because we still have 41.0 kgs.')
class TestExamples(TestCase):
    def test_print_Find_amount(self, mock_check_output):
        actual_result = Calculating_System.Find_amount()

        expected_directory = b'We have enough 11 kgs to supply for your offer because we still have 41.0 kgs.'
        self.assertIn(expected_directory, actual_result)