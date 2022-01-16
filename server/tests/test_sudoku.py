from unittest import TestCase

from constants import ChangeType
from data import grids
from sudoku import Sudoku, Change


class SudokuTestCase(TestCase):
    def test_init(self):
        s = Sudoku()
        self.assertEqual(9, len(s._cell))
        self.assertEqual(9, len(s._cell[5]))
        self.assertEqual(9, len(s._options[6][7]))
        self.assertEqual([], s._changes)

    def test_string(self):
        s = Sudoku()
        s.define_cell(4, 6, 7)
        self.assertEqual(
            "+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|       |       |       |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|       |       | 7     |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n"
            "|       |       |       |\n"
            "|       |       |       |\n"
            "|       |       |       |\n"
            "+-------+-------+-------+\n",
            str(s))

    def test_cells_in_square(self):
        cells = Sudoku._cells_in_square(4, 6)
        self.assertEqual(
            [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
            cells
        )

    def test_load_grid(self):
        s = Sudoku()
        s.load_grid(327085)
        self.assertEqual(7, s._cell[1][0])
        summary = s.change_summary()
        self.assertEqual(28, summary[ChangeType.DEFINE]['count'])
        self.assertEqual(546, summary[ChangeType.DEFINE]['removed'])

    def test_define_cell(self):
        s = Sudoku()
        self.assertEqual(None, s._cell[2][1])
        s.define_cell(2, 1, 3)
        self.assertEqual(3, s._cell[2][1])
        self.assertEqual(None, s._cell[2][2])
        self.assertEqual(
            [Change(ChangeType.DEFINE, {'row': 2, 'column': 1, 'value': 3}, 29)],
            s._changes
        )

    def test_define_cell_errors(self):
        s = Sudoku()
        s.define_cell(0, 0, 1)

        with self.assertRaises(ValueError) as e:
            s.define_cell(0, 0, 3)
        self.assertEqual('This cell already has a value', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            s.define_cell(9, 5, 5)
        self.assertEqual('Row out of range', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            s.define_cell(5, 12.4, 3)
        self.assertEqual('Column out of range', e.exception.args[0])

        with self.assertRaises(ValueError) as e:
            s.define_cell(1, 1, 1)
        self.assertEqual('Value not compatible with other cells', e.exception.args[0])

    def test_remove_options(self):
        s = Sudoku()
        full = [x for x in range(1, 10)]
        reduced = [x for x in range(1, 10) if x != 5]
        removed = s._remove_options(3, 4, 5)
        self.assertEqual(full, s._options[1][1])
        self.assertEqual(full, s._options[4][8])
        self.assertEqual(full, s._options[7][7])
        self.assertEqual(reduced, s._options[3][1])
        self.assertEqual(reduced, s._options[8][4])
        self.assertEqual(reduced, s._options[5][3])
        self.assertEqual(reduced, s._options[5][5])
        self.assertEqual([], s._options[3][4])
        self.assertEqual(29, removed)

    def test_check_cell_singleton(self):
        s = Sudoku()
        for x in range(7):
            s.define_cell(0, x, x + 1)
        self.assertEqual(None, s._check_cell_singleton())
        s.define_cell(0, 8, 9)
        r = s._check_cell_singleton()
        self.assertEqual(ChangeType.CELL_SINGLETON, r.type)
        self.assertEqual({'row': 0, 'column': 7, 'value': 8}, r.data)
        self.assertEqual(13, r.removed)
        self.assertEqual(8, s._cell[0][7])
        self.assertEqual([1, 2, 3, 4, 5, 6], s._options[1][8])

    def test_summary(self):
        s = Sudoku()
        s.define_cell(3, 3, 3)
        s.define_cell(6, 6, 3)
        summary = s.change_summary()
        self.assertEqual(
            {
                ChangeType.DEFINE: {'count': 2, 'removed': 56},
                ChangeType.CELL_SINGLETON: {'count': 0, 'removed': 0}
            },
            summary
        )

    def test_solve(self):
        s = Sudoku()
        indexes = [
            125602,
            327085,
        ]
        for index in indexes:
            s = Sudoku()
            s.load_grid(index)
            s.solve()
            summary = s.change_summary()
            self.assertEqual(grids[index]['solved'], s.solved())
            self.assertEqual(grids[index]['summary'], summary)
