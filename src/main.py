from src.consts import FULL_SET, WORKING_COPY


def get_missing_values(values):
    missing_values = set(FULL_SET) - set(values)
    return list(missing_values)


def get_values_from_row(matrix, row_no):
    if row_no < 0 or row_no > 8:
        raise AttributeError('Wrong row number')
    return matrix[row_no]


def get_values_from_column(matrix, col_no):
    return [row[col_no] for row in matrix]


def get_values_in_small_square(matrix, row, col):
    result = []
    rows_numbers = get_border(row)
    cols_numbers = get_border(col)
    for i in matrix[rows_numbers[0]:rows_numbers[1] + 1]:
        for j in i[cols_numbers[0]:cols_numbers[1] + 1]:
            result.append(j)
    return result


def get_border(value):
    if value <= 2:
        return [0, 2]
    elif 3 <= value <= 5:
        return [3, 5]
    else:
        return [6, 8]


def trim_zeros(table):
    return [value for value in table if value != 0]


def get_next_zero(matrix, cords=(0, 0)):
    for i, row in enumerate(matrix[cords[1]:9]):
        try:
            return row.index(0, cords[0]), cords[1] + i
        except AttributeError:
            pass
    return -1


def minus_two_sets(first_set, second_set):
    if isinstance(first_set, int):
        first_set = [first_set]
    return list(set(first_set) - set(second_set))


def create_points_matrix(matrix):
    points = []
    for row_no, row in enumerate(matrix):
        for column_no, cell in enumerate(row):
            points.append(Cell(row_no, column_no, cell))
    return points


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


class CellValidator:
    cell_type = Cell

    def __init__(self, cell):
        if not isinstance(cell, self.cell_type):
            raise TypeError("Wrong Type")
        self.cell = cell

    def _set_possible_values_by_row(self):
        self.cell.value = minus_two_sets(self.cell.value,
                                         get_values_from_row(WORKING_COPY, self.cell.row))
        self.update_matrix()

    def _set_possible_values_by_column(self):
        self.cell.value = minus_two_sets(self.cell.value,
                                         get_values_from_column(WORKING_COPY, self.cell.col))
        self.update_matrix()

    def _set_possible_values_by_square(self):
        self.cell.value = minus_two_sets(self.cell.value,
                                         get_values_in_small_square(WORKING_COPY, self.cell.row, self.cell.col))
        self.update_matrix()

    def run(self):
        if not isinstance(self.cell.value, int):
            self._set_possible_values_by_row()
            self._set_possible_values_by_column()
            self._set_possible_values_by_square()

    def update_matrix(self):
        if isinstance(self.cell.value, int) or len(self.cell.value) == 1:
            WORKING_COPY[self.cell.row][self.cell.col] = self.cell.value


class CellList(list):
    CELL_TYPE = Cell

    def __init__(self, items):
        for item in items:
            self.append(item)

    def append(self, item):
        if not isinstance(item, self.CELL_TYPE):
            raise TypeError('item is not of type {}'.format(self.CELL_TYPE))
        super(CellList, self).append(item)

    def validate(self):
        for cell in self:
            CellValidator(cell).run()
            print(cell)

        return WORKING_COPY

    def print(self):
        for i in self:
            print(i)

    def check_state(self):
        if self.isFinished():
            print("still missing values")
        print("That's ok!")

    def get_cell_by_cords(self, row, col):
        return [cell for cell in self if cell.row == row and cell.col == col][0]

    def get_values_by_row(self, row):
        return [cell.value for cell in self if cell.row == row]

    def get_values_from_column(self, col):
        return [row[col] for row in self]

    def isFinished(self):
        for item in self:
            if item.value == 0 or isinstance(item.value, list):
                return False
        return True


if __name__ == '__main__':
    for i in WORKING_COPY:
        print(i)
    cells = CellList(create_points_matrix(WORKING_COPY))
    while not cells.isFinished():
        print("Before validation: " + str(cells.check_state()))
        cells.validate()
        print("After validation: " + str(cells.check_state()))

    print("results:")
    for i in WORKING_COPY:
        print(i)
