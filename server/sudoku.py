from collections import namedtuple
from enum import Enum


Change = namedtuple('Change', ['type', 'data'])


class ChangeType(Enum):
    SINGLE = 'SINGLE'


class Sudoku:
    SIZE = 9
    BLOCK = 3
    START = 1

    def __init__(self):
        self._solved = False
        self._origin = None
        self._current = [[None for _ in range(Sudoku.SIZE)] for _ in range(Sudoku.SIZE)]
        self._options = [[
            [x for x in range(Sudoku.START, Sudoku.START + Sudoku.SIZE)]
            for _ in range(Sudoku.SIZE)] for _ in range(Sudoku.SIZE)]
        self._changes = []

    def __str__(self):
        separator = "+-------+-------+-------+\n"
        s = separator
        for r in range(Sudoku.SIZE):
            s += "|"
            for c in range(Sudoku.SIZE):
                if self._current[r][c] is None:
                    s += "  "
                else:
                    s += " "
                    s += str(self._current[r][c])
                if c % Sudoku.BLOCK == 2:
                    s += " |"
            s += "\n"
            if r % Sudoku.BLOCK == 2:
                s += separator
        return s

    @staticmethod
    def _cells_in_square(row, column):
        (top_row, top_column) = (row - row % Sudoku.BLOCK, column - column % Sudoku.BLOCK)
        return [(x, y)
                for x in range(top_row, top_row + Sudoku.BLOCK)
                for y in range(top_column, top_column + Sudoku.BLOCK)]

    def _set_origin(self):
        self._origin = [[self._current[r][c] for c in range(Sudoku.SIZE)] for r in range(Sudoku.SIZE)]

    def _define_cell(self, row, column, value):
        # Validity checks
        if row not in range(Sudoku.SIZE):
            raise ValueError(f'Row out of range')
        if column not in range(Sudoku.SIZE):
            raise ValueError(f'Column out of range')
        if self._current[row][column] is not None:
            raise ValueError(f'This cell already has a value')
        if value not in range(Sudoku.START, Sudoku.START + Sudoku.SIZE):
            print(value)
            raise ValueError(f'Value out of range')
        if value not in self._options[row][column]:
            raise ValueError(f'Value not compatible with other cells')

        self._current[row][column] = value
        self._reduce_options(row, column, value)
        if all([self._current[r][c] is not None for r in range(Sudoku.SIZE) for c in range(Sudoku.SIZE)]):
            self._solved = True

    def _reduce_options(self, row, column, value):
        # in row
        for c in range(Sudoku.SIZE):
            if c != column:
                try:
                    self._options[row][c].remove(value)
                except ValueError:
                    pass
        # in column
        for r in range(Sudoku.SIZE):
            if r != row:
                try:
                    self._options[r][column].remove(value)
                except ValueError:
                    pass
        # in square
        for (r, c) in Sudoku._cells_in_square(row, column):
            if r != row and c != column:
                try:
                    self._options[r][c].remove(value)
                except ValueError:
                    pass
        # remove options in cell
        self._options[row][column] = []

    def _find_single_option(self):
        for r in range(Sudoku.SIZE):
            for c in range(Sudoku.SIZE):
                if len(self._options[r][c]) == 1:
                    v = self._options[r][c][0]
                    self._define_cell(r, c, v)
                    self._reduce_options(r, c, v)
                    change = Change(ChangeType.SINGLE, {'row': r, 'column': c, 'value': v})
                    self._changes.append(change)
                    return change
        return None

    def _solve(self):
        while True:
            if self._find_single_option() is None:
                break


def play_sudoku():
    s = Sudoku()
    print('Enter your grid line by line, with space for empty cell')
    for r in range(Sudoku.SIZE):
        line = input(f'Line {r+1}:')
        for c in range(Sudoku.SIZE):
            if line[c] != ' ':
                s._define_cell(r, c, int(line[c]))
        print(s)
    s._set_origin()
    print('Input complete. Starting solving')
    while True:
        input('Press enter')
        print(s._find_single_option())
        print(s)
        if s._solved:
            break
    print('Solved!!')
    return s
