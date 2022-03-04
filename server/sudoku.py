from collections import namedtuple
from typing import List, Union

from constants import ChangeType
from data import grids
from utils import exclusive_sub_list, MIN_NB_OF_CONTAINERS


Change = namedtuple('Change', ['type', 'data', 'removed'])


class Sudoku:
    SIZE = 9
    BLOCK = 3
    VALUE_RANGE = range(1, 1 + SIZE)

    def __init__(self):
        self._cell: List[List[Union[int, None]]] = [
            [None for _ in range(Sudoku.SIZE)] for _ in range(Sudoku.SIZE)
        ]
        self._options: List[List[List[int]]] = [
            [
                [x for x in Sudoku.VALUE_RANGE]
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
                    s += f" {str(self._cell[r][c])}"
                if c % Sudoku.BLOCK == 2:
                    s += " |"
            s += "\n"
            if r % Sudoku.BLOCK == 2:
                s += separator
        return s

    def print_options(self):
        simple_separator = '++-------+-------+-------++-------+-------+-------++-------+-------+-------++\n'
        double_separator = '++=======+=======+=======++=======+=======+=======++=======+=======+=======++\n'
        s = double_separator
        for r in range(Sudoku.SIZE):
            for sub_r in range(Sudoku.BLOCK):
                s += '||'
                for c in range(Sudoku.SIZE):
                    value = self._cell[r][c]
                    options = self._options[r][c]
                    if value is not None:
                        if sub_r == 0:
                            s += ' \\   /'
                        elif sub_r == 1:
                            s += f'   {str(value)}  '
                        else:
                            s += ' /   \\'
                    else:
                        pos1 = str(sub_r * 3 + 1) if (sub_r * 3 + 1) in options else ' '
                        pos2 = str(sub_r * 3 + 2) if (sub_r * 3 + 2) in options else ' '
                        pos3 = str(sub_r * 3 + 3) if (sub_r * 3 + 3) in options else ' '
                        s += f' {pos1} {pos2} {pos3}'

                    s += " |"
                    if c % Sudoku.BLOCK == 2:
                        s += "|"
                s += '\n'
            if r % Sudoku.BLOCK == 2:
                s += double_separator
            else:
                s += simple_separator
        print(s)

    @staticmethod
    def _cells_in_square(row, column):
        (top_row, top_column) = (row - row % Sudoku.BLOCK, column - column % Sudoku.BLOCK)
        return [
            (x, y)
            for x in range(top_row, top_row + Sudoku.BLOCK)
            for y in range(top_column, top_column + Sudoku.BLOCK)
        ]

    def load_grid(self, index):
        g = grids[index]['grid']
        pos = 0
        for r in range(Sudoku.SIZE):
            for c in range(Sudoku.SIZE):
                v = g[pos]
                pos += 1
                if v != ' ':
                    self.define_cell(r, c, int(v))

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
        if value not in Sudoku.VALUE_RANGE:
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

    def _find_value_in_square(self, square_row, square_column, value):
        for r in range(square_row, square_row + Sudoku.BLOCK):
            for c in range(square_column, square_column + Sudoku.BLOCK):
                if self._cell[r][c] == value:
                    return r, c
        return None

    def _check_exclusive_row_in_square(self):
        # Iterate on all squares
        for square_row in range(0, Sudoku.SIZE, Sudoku.BLOCK):
            for square_column in range(0, Sudoku.SIZE, Sudoku.BLOCK):
                for value in Sudoku.VALUE_RANGE:
                    # Check that no cell in the square has this value
                    if self._find_value_in_square(square_row, square_column, value) is None:
                        # Check if value is present in options in one row only
                        rows_with_value = []
                        for row in range(square_row, square_row + Sudoku.BLOCK):
                            if any(
                                [value in self._options[row][col]
                                 for col in range(square_column, square_column + Sudoku.BLOCK)]
                            ):
                                rows_with_value.append(row)
                        if len(rows_with_value) == 1:
                            exclusive_row = rows_with_value[0]
                            # Check if value is contained in options in other squares on same row
                            removables = []
                            for column in range(Sudoku.SIZE):
                                if (column // Sudoku.BLOCK) != (square_column // Sudoku.BLOCK):
                                    if value in self._options[exclusive_row][column]:
                                        removables.append(column)
                            if len(removables) > 0:
                                # Remove value from these options and return the changes performed
                                for column in removables:
                                    self._options[exclusive_row][column].remove(value)
                                change = Change(
                                    ChangeType.EXCLUSIVE_ROW_IN_SQUARE,
                                    {'square': (square_row, square_column), 'value': value,
                                     'exclusive row': exclusive_row, 'removed': removables},
                                    len(removables)
                                )
                                self._changes.append(change)
                                return change
        return None

    def _check_exclusive_column_in_square(self):
        # Iterate on all squares
        for square_row in range(0, Sudoku.SIZE, Sudoku.BLOCK):
            for square_column in range(0, Sudoku.SIZE, Sudoku.BLOCK):
                for value in Sudoku.VALUE_RANGE:
                    # Check that no cell in the square has this value
                    if self._find_value_in_square(square_row, square_column, value) is None:
                        # Check if value is present in options in one column only
                        columns_with_value = []
                        for column in range(square_column, square_column + Sudoku.BLOCK):
                            if any(
                                [value in self._options[row][column]
                                 for row in range(square_row, square_row + Sudoku.BLOCK)]
                            ):
                                columns_with_value.append(column)
                        if len(columns_with_value) == 1:
                            exclusive_column = columns_with_value[0]
                            # Check if value is contained in options in other squares on same column
                            removables = []
                            for row in range(Sudoku.SIZE):
                                if (row // Sudoku.BLOCK) != (square_row // Sudoku.BLOCK):
                                    if value in self._options[row][exclusive_column]:
                                        removables.append(row)
                            if len(removables) > 0:
                                # Remove value from these options and return the changes performed
                                for row in removables:
                                    self._options[row][exclusive_column].remove(value)
                                change = Change(
                                    ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE,
                                    {'square': (square_row, square_column), 'value': value,
                                     'exclusive column': exclusive_column, 'removed': removables},
                                    len(removables)
                                )
                                self._changes.append(change)
                                return change
        return None

    def _check_row_sub_set(self):
        for row in range(Sudoku.SIZE):
            options = []
            for column in range(Sudoku.SIZE):
                if self._cell[row][column] is None:
                    options.append((column, self._options[row][column]))
            if len(options) >= MIN_NB_OF_CONTAINERS:
                result = exclusive_sub_list([o for _, o in options])
                if result is not None:
                    options_sub_set, members_indexes = result
                    members_columns = [options[index][0] for index in members_indexes]
                    removed = []
                    for column in range(Sudoku.SIZE):
                        if column not in members_columns:
                            for value in options_sub_set:
                                try:
                                    self._options[row][column].remove(value)
                                    removed.append((column, value))
                                except ValueError:
                                    pass
                    if len(removed) > 0:
                        change = Change(
                            ChangeType.ROW_SUB_SET,
                            {'row': row, 'sub_set': options_sub_set, 'removed': removed},
                            len(removed)
                        )
                        self._changes.append(change)
                        return change
        return None

    def _check_column_sub_set(self):
        for column in range(Sudoku.SIZE):
            options = []
            for row in range(Sudoku.SIZE):
                if self._cell[row][column] is None:
                    options.append((row, self._options[row][column]))
            if len(options) >= MIN_NB_OF_CONTAINERS:
                result = exclusive_sub_list([o for _, o in options])
                if result is not None:
                    options_sub_set, members_indexes = result
                    members_rows = [options[index][0] for index in members_indexes]
                    removed = []
                    for row in range(Sudoku.SIZE):
                        if row not in members_rows:
                            for value in options_sub_set:
                                try:
                                    self._options[row][column].remove(value)
                                    removed.append((row, value))
                                except ValueError:
                                    pass
                    if len(removed) > 0:
                        change = Change(
                            ChangeType.COLUMN_SUB_SET,
                            {'column': column, 'sub_set': options_sub_set, 'removed': removed},
                            len(removed)
                        )
                        self._changes.append(change)
                        return change
        return None

    def _check_square_sub_set(self):
        for block_row in range(0, Sudoku.SIZE, Sudoku.BLOCK):
            for block_column in range(0, Sudoku.SIZE, Sudoku.BLOCK):
                options = []
                for row, column in self._cells_in_square(block_row, block_column):
                    if self._cell[row][column] is None:
                        options.append(((row, column), self._options[row][column]))
                if len(options) >= MIN_NB_OF_CONTAINERS:
                    result = exclusive_sub_list([o for _, o in options])
                    if result is not None:
                        options_sub_set, members_indexes = result
                        sub_set_cells = [options[index][0] for index in members_indexes]
                        removed = []
                        for row, column in self._cells_in_square(block_row, block_column):
                            if (row, column) not in sub_set_cells:
                                for value in options_sub_set:
                                    try:
                                        self._options[row][column].remove(value)
                                        removed.append((row, column, value))
                                    except ValueError:
                                        pass
                        if len(removed) > 0:
                            change = Change(
                                ChangeType.SQUARE_SUB_SET,
                                {'square': (block_row, block_column), 'sub_set': options_sub_set, 'removed': removed},
                                len(removed)
                            )
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
            if self._check_cell_singleton() is not None:
                continue
            elif self._check_exclusive_row_in_square() is not None:
                continue
            elif self._check_exclusive_column_in_square() is not None:
                continue
            elif self._check_row_sub_set() is not None:
                continue
            elif self._check_column_sub_set() is not None:
                continue
            elif self._check_square_sub_set() is not None:
                continue
            else:
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
