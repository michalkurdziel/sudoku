from unittest import TestCase
from src.main import get_missing_values
from src.main import FULL_SET
from src.main import get_values_from_row, get_values_from_column, get_values_in_small_square
from src.main import get_border
from src.main import trim_zeros
from src.main import get_next_zero
from src.main import create_point_list

VALID_MATRIX = [
    [0, 0, 1, 0, 0, 9, 0, 0, 0],
    [4, 0, 9, 1, 7, 0, 0, 0, 2],
    [0, 3, 5, 0, 4, 8, 1, 0, 0],

    [9, 0, 6, 0, 0, 0, 3, 7, 0],
    [1, 0, 0, 7, 3, 6, 4, 0, 9],
    [3, 0, 0, 9, 8, 2, 0, 0, 0],

    [0, 0, 0, 0, 2, 7, 0, 0, 4],
    [6, 9, 4, 0, 1, 3, 0, 5, 7],
    [0, 7, 2, 0, 0, 0, 0, 0, 0],
]


class TestReturningValues(TestCase):

    def test_return_missing_values(self):
        expected_result = [8, 9]
        values = [x for x in range(1, 8)]
        results = get_missing_values(values)
        assert expected_result == results, 'Expected {} but results is {}'.format(expected_result, results)

    def test_return_missing_value_when_no_entry(self):
        expected_result = FULL_SET
        results = get_missing_values([])
        assert expected_result == results, 'Expected {} but results is {}'.format(expected_result, results)

    def test_return_missing_values_when_all_entries_exists(self):
        expected_result = []
        results = get_missing_values(FULL_SET)
        assert expected_result == results, 'Expected {} but results is {}'.format(expected_result, results)


class TestGrubAllvalues(TestCase):

    def test_proper_values(self):
        self.assertRaises(AttributeError, get_values_from_row, [], -1)
        self.assertRaises(AttributeError, get_values_from_row, [], 10)

    def test_get_values_from_row(self):
        input_matrix = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 4, 5, 6, 7, 8, 0],
        ]
        expected_results = [1, 0, 0, 4, 5, 6, 7, 8, 0]
        row_number = 1
        results = get_values_from_row(input_matrix, row_number)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_values_from_column(self):
        input_matrix = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 4, 5, 6, 7, 8, 0],
        ]
        expected_results = [3, 0]
        col_number = 2
        results = get_values_from_column(input_matrix, col_number)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)


    def test_get_first_small_square_indexes(self):
        expected_results = [0, 0, 1, 4, 0, 9, 0, 3, 5]
        results = get_values_in_small_square(VALID_MATRIX, 0, 0)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_fourth_small_square_indexes(self):
        expected_results = [0, 0, 0, 7, 3, 6, 9, 8, 2]
        results = get_values_in_small_square(VALID_MATRIX, 4, 4)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_border(self):
        assert [0, 2] == get_border(0), 'Expected {} but results is {}'.format(expected_results, results)
        assert [0, 2] == get_border(1), 'Expected {} but results is {}'.format(expected_results, results)
        assert [0, 2] == get_border(2), 'Expected {} but results is {}'.format(expected_results, results)
        assert [3, 5] == get_border(3), 'Expected {} but results is {}'.format(expected_results, results)
        assert [3, 5] == get_border(4), 'Expected {} but results is {}'.format(expected_results, results)
        assert [3, 5] == get_border(5), 'Expected {} but results is {}'.format(expected_results, results)
        assert [6, 8] == get_border(6), 'Expected {} but results is {}'.format(expected_results, results)
        assert [6, 8] == get_border(7), 'Expected {} but results is {}'.format(expected_results, results)
        assert [6, 8] == get_border(8), 'Expected {} but results is {}'.format(expected_results, results)


    def test_get_next_zero(self):
        expected_results = (0, 0)
        results = get_next_zero(VALID_MATRIX)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (1, 0)
        results = get_next_zero(VALID_MATRIX, (1, 0))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (3, 0)
        results = get_next_zero(VALID_MATRIX, (2, 0))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (1, 1)
        results = get_next_zero(VALID_MATRIX, (0, 1))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (5, 1)
        results = get_next_zero(VALID_MATRIX, (2, 1))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (7, 2)
        results = get_next_zero(VALID_MATRIX, (4, 2))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)


class TestBaseConfiguration(TestCase):
    full_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def test_full_set(self):
        assert self.full_set == FULL_SET


class TestUtilities(TestCase):

    def test_drop_zeros(self):
        expected_results = [1, 9]
        results = trim_zeros(VALID_MATRIX[0])
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)


class TestCreatePointList(TestCase):

    def test_create_point_list(self):
        create_point_list()