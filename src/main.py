FULL_SET = [x for x in range(1, 10)]
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


def get_missing_values(values):
    missing_values = set(FULL_SET) - set(values)
    return list(missing_values)


def get_values_from_row(matrix, row_no):
    if row_no < 0 or row_no > 8:
        raise AttributeError('Wrong row number')
    return matrix[row_no]


def get_values_from_column(matrix, col_no):
    return [row[col_no] for row in matrix]


def get_values_in_small_square(matrix, x, y):
    result = []
    border_x = get_border(x)
    border_y = get_border(y)
    for i in matrix[border_y[0]:border_y[1]+1]:
        for j in i[border_x[0]:border_x[1]+1]:
            result.append(j)
    return result


def get_border(x):
    if x <= 2:
        return [0, 2]
    elif x >= 3 and x <= 5:
        return [3, 5]
    else:
        return [6, 8]


def trim_zeros(table):
    return [x for x in table if x != 0]


def get_next_zero(matrix, cords=(0, 0)):
    for i, row in enumerate(matrix[cords[1]:9]):
        try:
            return row.index(0, cords[0]), cords[1]+i
        except AttributeError:
            pass
    return -1


def minus_two_sets(first_set, second_set):
    return list(set(first_set)-set(second_set))


class Point:
    _value = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = VALID_MATRIX[y][x]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value == 0:
            self._value = minus_two_sets(self._value,
                                                  get_values_from_row(VALID_MATRIX, self.x))

            self._value = minus_two_sets(self._value,
                                                  get_values_from_column(VALID_MATRIX, self.y))

            self._value = minus_two_sets(self._value,
                                                get_values_in_small_square(VALID_MATRIX, self.x, self.y))
        else:
            self._value = value

    def __str__(self):
        return '{}. {}: {}'.format(self.x, self.y, self.value)

def create_point_list():
    points = []
    for i, row in enumerate(VALID_MATRIX):
        for j, column in enumerate(row):
            points.append(Point(j, i))
    return points


