from collections import namedtuple
from enum import Enum, auto
from typing import List, Union


Change = namedtuple('Change', ['type', 'data', 'removed'])


class ChangeType(Enum):
    DEFINE = auto()
    CELL_SINGLETON = auto()


class Sudoku:
    SIZE = 9
    BLOCK = 3
    START = 1

    def __init__(self):
        self._cell: List[List[Union[int, None]]] = [
            [None for _ in range(Sudoku.SIZE)] for _ in range(Sudoku.SIZE)
        ]
        self._options: List[List[List[int]]] = [
            [
                [x for x in range(Sudoku.START, Sudoku.START + Sudoku.SIZE)]
                for _ in range(Sudoku.SIZE)
            ]
            for _ in range(Sudoku.SIZE)
        ]
        self._changes: List[Change] = []

    def __str__(self):
        separator = "+-------+-------+-------+\n"
        s = separator
        for r in range(Sudoku.SIZE):
            s += "|"
            for c in range(Sudoku.SIZE):
                if self._cell[r][c] is None:
                    s += "  "
                else:
                    s += " "
                    s += str(self._cell[r][c])
                if c % Sudoku.BLOCK == 2:
                    s += " |"
            s += "\n"
            if r % Sudoku.BLOCK == 2:
                s += separator
        return s

    @staticmethod
    def _cells_in_square(row, column):
        (top_row, top_column) = (row - row % Sudoku.BLOCK, column - column % Sudoku.BLOCK)
        return [
            (x, y)
            for x in range(top_row, top_row + Sudoku.BLOCK)
            for y in range(top_column, top_column + Sudoku.BLOCK)
        ]

    def solved(self) -> bool:
        return all([self._cell[r][c] is not None for r in range(Sudoku.SIZE) for c in range(Sudoku.SIZE)])

    def define_cell(self, row, column, value):
        # Validity checks
        if row not in range(Sudoku.SIZE):
            raise ValueError(f'Row out of range')
        if column not in range(Sudoku.SIZE):
            raise ValueError(f'Column out of range')
        if self._cell[row][column] is not None:
            raise ValueError(f'This cell already has a value')
        if value not in range(Sudoku.START, Sudoku.START + Sudoku.SIZE):
            print(value)
            raise ValueError(f'Value out of range')
        if value not in self._options[row][column]:
            raise ValueError(f'Value not compatible with other cells')

        # Define cell
        self._cell[row][column] = value
        removed = self._remove_options(row, column, value)
        change = Change(ChangeType.DEFINE, {'row': row, 'column': column, 'value': value}, removed)
        self._changes.append(change)

    def _remove_options(self, row, column, value):
        removed = 0
        # in row
        for c in range(Sudoku.SIZE):
            if c != column:
                try:
                    self._options[row][c].remove(value)
                    removed += 1
                except ValueError:
                    pass
        # in column
        for r in range(Sudoku.SIZE):
            if r != row:
                try:
                    self._options[r][column].remove(value)
                    removed += 1
                except ValueError:
                    pass
        # in square
        for (r, c) in Sudoku._cells_in_square(row, column):
            if r != row and c != column:
                try:
                    self._options[r][c].remove(value)
                    removed += 1
                except ValueError:
                    pass
        # remove options in cell
        removed += len(self._options[row][column])
        self._options[row][column] = []
        return removed

    def _check_cell_singleton(self):
        for r in range(Sudoku.SIZE):
            for c in range(Sudoku.SIZE):
                if len(self._options[r][c]) == 1:
                    v = self._options[r][c][0]
                    self._cell[r][c] = v
                    removed = self._remove_options(r, c, v)
                    change = Change(ChangeType.CELL_SINGLETON, {'row': r, 'column': c, 'value': v}, removed)
                    self._changes.append(change)
                    return change
        return None

    def change_summary(self):
        summary = {t: {'count': 0, 'removed': 0} for t in ChangeType}
        for c in self._changes:
            summary[c.type]['count'] += 1
            summary[c.type]['removed'] += c.removed
        return summary

    def solve(self):
        while True:
            if self._check_cell_singleton() is None:
                break


def play_sudoku():
    s = Sudoku()
    print('Enter your grid line by line, with space for empty cell')
    for r in range(Sudoku.SIZE):
        line = input(f'Line {r+1}:')
        for c in range(Sudoku.SIZE):
            if line[c] != ' ':
                s.define_cell(r, c, int(line[c]))
        print(s)
    print('Input complete. Starting solving')
    while True:
        input('Press enter')
        print(s._check_cell_singleton())
        print(s)
        if s.solved():
            break
    print('Solved!!')
    return s
