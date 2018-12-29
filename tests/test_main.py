from unittest import TestCase
from unittest import mock

from src.main import Cell
from src.main import CellList
from src.main import CellValidator
from src import FULL_SET
from src.main import create_points_matrix
from src.main import get_border
from src.main import get_missing_values
from src.main import get_next_zero
from src.main import get_values_from_row, get_values_from_column, get_values_in_small_square
from src.main import trim_zeros

TEST_MATRIX = [
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

TEST_MATRIX2 = [
    [0, 3, 6, 0, 4, 7, 5, 2, 0],
    [0, 4, 0, 6, 2, 5, 0, 0, 8],
    [0, 0, 0, 3, 1, 0, 0, 7, 0],

    [0, 1, 0, 5, 0, 6, 7, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 5, 7, 0, 4, 0, 8, 0],

    [0, 2, 0, 0, 6, 8, 0, 0, 0],
    [4, 0, 0, 2, 5, 3, 0, 9, 0],
    [0, 5, 9, 4, 7, 0, 6, 3, 0]
]
CORRECT_MATRIX_2 = [
    [1, 3, 6, 8, 4, 7, 5, 2, 9],
    [9, 4, 7, 6, 2, 5, 3, 1, 8],
    [5, 8, 2, 3, 1, 9, 4, 7, 6],

    [2, 1, 8, 5, 9, 6, 7, 4, 3],
    [3, 7, 4, 1, 8, 2, 9, 6, 5],
    [6, 9, 5, 7, 3, 4, 2, 8, 1],

    [7, 2, 3, 9, 6, 8, 1, 5, 4],
    [4, 6, 1, 2, 5, 3, 8, 9, 7],
    [8, 5, 9, 4, 7, 1, 6, 3, 2]
]
WORKING_COPY = TEST_MATRIX2


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
        expected_results = [0, 3, 6, 0, 4, 0, 0, 0, 0]
        results = get_values_in_small_square(WORKING_COPY, 0, 0)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_fourth_small_square_indexes(self):
        expected_results = [5, 0, 6, 0, 0, 0, 7, 0, 4]
        results = get_values_in_small_square(WORKING_COPY, 4, 4)
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
        results = get_next_zero(TEST_MATRIX)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (1, 0)
        results = get_next_zero(TEST_MATRIX, (1, 0))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (3, 0)
        results = get_next_zero(TEST_MATRIX, (2, 0))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (1, 1)
        results = get_next_zero(TEST_MATRIX, (0, 1))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (5, 1)
        results = get_next_zero(TEST_MATRIX, (2, 1))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)
        expected_results = (7, 2)
        results = get_next_zero(TEST_MATRIX, (4, 2))
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)


class TestBaseConfiguration(TestCase):
    full_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_full_set(self):
        assert self.full_set == FULL_SET


class TestUtilities(TestCase):

    def test_drop_zeros(self):
        expected_results = [1, 9]
        results = trim_zeros(TEST_MATRIX[0])
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)


class TestCellValidator(TestCase):

    @mock.patch('src.main.Cell', autospec=True)
    def test_create_instance_valid(self, mock_cell):
        validator = CellValidator(mock_cell)
        self.assertIsInstance(validator, CellValidator, "validator = {}, CellValidator = {} ".format(validator, CellValidator))

    def test_create_instance_raise_exception(self):
        self.assertRaises(TypeError, CellValidator, 1)

    def test_validate_by_row(self):
        cell = Cell(0, 0, 0)
        validator = CellValidator(cell)
        validator._set_possible_values_by_row()
        self.assertListEqual(cell.value, [1, 8, 9])

    def test_validate_by_column(self):
        cell = Cell(0, 0, 0)
        validator = CellValidator(cell)
        validator._set_possible_values_by_column()
        self.assertListEqual(cell.value, [1, 2, 5, 6, 7, 8, 9])

    def test_validate_by_square(self):
        cell = Cell(0, 0, 0)
        validator = CellValidator(cell)
        validator._set_possible_values_by_square()
        self.assertListEqual(cell.value, [1, 2, 5, 7, 8, 9])

    def test_validate_by_three_dimenssions(self):
        cell = Cell(0, 0, 0)
        validator = CellValidator(cell)
        validator.run()
        self.assertListEqual(cell.value, [1, 8, 9])


class TestCellList(TestCase):

    @mock.patch('src.main.Cell', autospec=True)
    def test_list_stores_proper_values(self, mock_cell):
        cells = CellList([mock_cell, mock_cell, mock_cell])
        self.assertEqual(len(cells), 3, len(cells))

    def test_get_cell_by_cords(self):
        cell = Cell(2, 2, 5)
        cells = CellList([cell])
        cell_ = cells.get_cell_by_cords(2, 2)
        self.assertEqual(cell_.value, cell.value)

    def test_get_values_from_row(self):
        cell1 = Cell(0, 0, 1)
        cell2 = Cell(0, 1, 1)
        cell3 = Cell(0, 4, 1)
        cell4 = Cell(2, 4, 3)
        cells = CellList([cell1, cell2, cell3, cell4])
        self.assertListEqual(cells.get_values_by_row(0), [1, 1, 1])

    def test_status_check(self):
        cells = CellList(create_points_matrix(CORRECT_MATRIX_2))
        res = cells.isFinished()
        self.assertTrue(res)

        cells = CellList(create_points_matrix(TEST_MATRIX))
        cells.print()
        res = cells.isFinished()
        self.assertFalse(res, "res: " + str(res))


class TestCell(TestCase):

    def test_create_intsance(self):
        cell = Cell(1, 1, 1)
        self.assertIsInstance(cell, Cell)


class TestCheckInputMatrixes(TestCase):

    def test_compare_two_matrix(self):
        for i in range(9):
            for j in range(9):
                if TEST_MATRIX2[i][j] != 0:
                    self.assertEqual(TEST_MATRIX2[i][j], CORRECT_MATRIX_2[i][j], "i: {}, j {}".format(i, j))

    def test_general_validation(self):
        cells = CellList(create_points_matrix(WORKING_COPY))
        for i in range(3):
            result = cells.validate()

        for i in range(9):
            for j in range(9):
                self.assertEqual(result[i][j], CORRECT_MATRIX_2[i][j], "i= {}, j= {}".format(i, j))
