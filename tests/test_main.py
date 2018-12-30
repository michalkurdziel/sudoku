from unittest import TestCase
from unittest import mock

from src.consts import puzzle
from src.consts import puzzle_results
from src.main import Cell
from src.main import CellList
from src.main import get_border

FULL_SET = [x for x in range(1, 10)]

TEST_MATRIX = [
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

CORRECT_MATRIX = [
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


class TestGrubAllvalues(TestCase):

    def setUp(self):
        self.cells = CellList(TEST_MATRIX)

    def tearDown(self):
        self.cells = None

    def test_get_values_from_row(self):
        expected_results = [4, 6, 2, 5, 8]
        results = self.cells.get_values_from_row(1)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_values_from_column(self):
        expected_results = [6, 5, 9]
        results = self.cells.get_values_from_column(2)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_first_small_square_indexes(self):
        expected_results = [3, 6, 4]
        self.cells1 = CellList(TEST_MATRIX)

        values_in_square = self.cells1.get_values_in_small_square(0, 0)
        self.assertListEqual(values_in_square, expected_results)

    def test_get_fourth_small_square_indexes(self):
        expected_results = [5, 6, 7, 4]
        results = self.cells.get_values_in_small_square(4, 4)
        assert expected_results == results, 'Expected {} but results is {}'.format(expected_results, results)

    def test_get_border(self):
        self.assertListEqual([0, 1, 2], get_border(1))
        self.assertListEqual([0, 1, 2], get_border(2))
        self.assertListEqual([3, 4, 5], get_border(3))
        self.assertListEqual([3, 4, 5], get_border(4))
        self.assertListEqual([3, 4, 5], get_border(5))
        self.assertListEqual([6, 7, 8], get_border(6))
        self.assertListEqual([6, 7, 8], get_border(7))
        self.assertListEqual([6, 7, 8], get_border(8))


class TestBaseConfiguration(TestCase):
    full_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_full_set(self):
        assert self.full_set == FULL_SET


class TestCellValidator(TestCase):

    def setUp(self):
        self.cells = CellList(TEST_MATRIX)

    def test_validate_by_row(self):
        cell = Cell(0, 0, 0)
        self.cells._set_possible_values_by_row(cell, [3, 6, 4])
        self.assertListEqual(cell.value, [1, 2, 5, 7, 8, 9])

    def test_validate_by_column(self):
        cell = Cell(0, 0, 0)
        self.cells._set_possible_values_by_column(cell, [3, 4])
        self.assertListEqual(cell.value, [1, 2, 5, 6, 7, 8, 9])

    def test_validate_by_square(self):
        cell = Cell(0, 0, 0)
        self.cells._set_possible_values_by_square(cell, [3, 4, 6])
        self.assertListEqual(cell.value, [1, 2, 5, 7, 8, 9])

    def test_validate_by_three_dimenssions(self):
        cell = Cell(0, 0, 0)
        self.cells.run(cell)
        self.assertListEqual(cell.value, [1, 8, 9])


class TestCellList(TestCase):

    @mock.patch('src.main.Cell', autospec=True)
    def test_list_stores_proper_values(self, mock_cell):
        cells = CellList([[mock_cell, mock_cell, mock_cell]])
        self.assertEqual(len(cells), 3, len(cells))

    def test_status_check(self):
        cells = CellList(TEST_MATRIX)
        cells.print()
        res = cells.isFinished()
        self.assertFalse(res, "res: " + str(res))

        cells = CellList(CORRECT_MATRIX)
        res = cells.isFinished()
        self.assertTrue(res)



class TestCell(TestCase):

    def test_create_intsance(self):
        cell = Cell(1, 1, 1)
        self.assertIsInstance(cell, Cell)


class TestCheckInputMatrixes(TestCase):


    def test_compare_two_matrix(self):
        for i in range(9):
            for j in range(9):
                if TEST_MATRIX[i][j] != 0:
                    self.assertEqual(TEST_MATRIX[i][j], CORRECT_MATRIX[i][j], "i: {}, j {}".format(i, j))

    def test_general_validation_1(self):
        cells = CellList(TEST_MATRIX)

        while not cells.isFinished():
            cells.validate()

        matrix = cells.generate_matrix()

        for i in range(9):
            for j in range(9):
                self.assertEqual(matrix[i][j], CORRECT_MATRIX[i][j], "i= {}, j= {}".format(i, j))

    def test_general_validation_2(self):
        cells = CellList(puzzle)
        while not cells.isFinished():
            cells.validate()

        matrix = cells.generate_matrix()
        for i in range(9):
            for j in range(9):
                self.assertEqual(matrix[i][j], puzzle_results[i][j], "i= {}, j= {}".format(i, j))
