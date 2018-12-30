from src.consts import puzzle

FULL_SET = [x for x in range(1, 10)]


def get_border(value):
    if value <= 2:
        return [0, 1, 2]
    elif 3 <= value <= 5:
        return [3, 4, 5]
    else:
        return [6, 7, 8]


class Cell:
    _value = None

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        if self.value == 0:
            self.value = FULL_SET

    def __str__(self):
        return "row: {} col: {} value: {}".format(self.row, self.col, self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, list):
            if len(value) == 1:
                self._value = value[0]
            elif len(value) > 1:
                self._value = sorted(value)
        else:
            self._value = value


class CellList(list):
    CELL_TYPE = Cell

    def __init__(self, input_data):
        self.matrix = input_data

        for row_no, row in enumerate(self.matrix):
            for column_no, cell in enumerate(row):
                self.append(Cell(row_no, column_no, cell))

    def append(self, item):
        if not isinstance(item, self.CELL_TYPE):
            raise TypeError('item is not of type {}'.format(self.CELL_TYPE))
        super(CellList, self).append(item)

    def validate(self):
        for cell in self:
            self.run(cell)

    def print(self):
        for i in self:
            print(i)

    def check_state(self):
        if self.isFinished():
            print("That's ok!")
        else:
            print("Still missing values")

    def isFinished(self):
        for item in self:
            if item.value == 0 or isinstance(item.value, list):
                return False
        return True

    def update_matrix(self):
        for cell in self:
            if isinstance(cell.value, int) or len(cell.value) == 1:
                self.matrix[cell.row][cell.col] = cell.value

    def get_values_from_row(self, row):
        return [cell.value for cell in self if cell.row == row and isinstance(cell.value, int)]

    def get_values_from_column(self, col):
        return [cell.value for cell in self if cell.col == col and isinstance(cell.value, int)]

    def get_values_in_small_square(self, row, col):
        rows_numbers = get_border(row)
        cols_numbers = get_border(col)
        return [cell.value for cell in self if cell.row in rows_numbers and cell.col in cols_numbers and isinstance(cell.value, int)]

    def _set_possible_values_by_row(self, cell, set_to_compare):
        cell.value = self.minus_two_sets(cell.value, set_to_compare)

    def _set_possible_values_by_column(self, cell, set_to_compare):
        cell.value = self.minus_two_sets(cell.value, set_to_compare)

    def _set_possible_values_by_square(self, cell, set_to_compare):
        cell.value = self.minus_two_sets(cell.value, set_to_compare)

    def minus_two_sets(self, first_set, second_set):
        if isinstance(first_set, int):
            first_set = [first_set]
        return list(set(first_set) - set(second_set))

    def run(self, cell):
        if not isinstance(cell.value, int):
            self._set_possible_values_by_row(cell, self.get_values_from_row(cell.row))
            self._set_possible_values_by_column(cell, self.get_values_from_column(cell.col))
            self._set_possible_values_by_square(cell, self.get_values_in_small_square(cell.row, cell.col))

    def generate_matrix(self):
        matrix = [[0 for i in range(9)] for j in range(9)]
        for cell in self:
            matrix[cell.row][cell.col] = cell.value
        return matrix


if __name__ == '__main__':
    cells = CellList(puzzle)

    while not cells.isFinished():
        cells.validate()
        cells.check_state()

    cells.print()
    print(cells.generate_matrix())
