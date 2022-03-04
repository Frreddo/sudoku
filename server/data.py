from enum import Enum, auto

from constants import ChangeType


class Difficulty(Enum):
    FACILE = auto()
    MOYEN = auto()
    DIFFICILE = auto()
    DIABOLIQUE = auto()
    DEMONIAQUE = auto()


grids = {
    327085: {
        'grid': "  1 7 9  "
                "7  4 1 2 "
                "     6 73"
                "    43  7"
                "1       4"
                "4  18    "
                "39 6     "
                " 6 5 8  1"
                "  5 2 7  ",
        'difficulty': Difficulty.DIFFICILE,
        'solved': True,
        'summary': {
            ChangeType.DEFINE:
                {'count': 28, 'removed': 546},
            ChangeType.CELL_SINGLETON:
                {'count': 53, 'removed': 168},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 5, 'removed': 8},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 2, 'removed': 3},
            ChangeType.ROW_SUB_SET:
                {'count': 1, 'removed': 4},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },
    125602: {
        'grid': "    6 5  "
                " 153   9 "
                "2  459681"
                " 6  3    "
                "7 41 53 8"
                "    4  1 "
                "178526  4"
                " 4   382 "
                "  2 7    ",
        'difficulty': Difficulty.FACILE,
        'solved': True,
        'summary': {
            ChangeType.DEFINE:
                {'count': 36, 'removed': 602},
            ChangeType.CELL_SINGLETON:
                {'count': 45, 'removed': 127},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 0, 'removed': 0},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 0, 'removed': 0},
            ChangeType.ROW_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },
    313921: {
        'grid': "  16  3  "
                " 8 94    "
                "  7  34  "
                " 1       "
                " 9 486 5 "
                "       8 "
                "  42  1  "
                "    57 9 "
                "  9  47  ",
        'difficulty': Difficulty.DIFFICILE,
        'solved': True,
        'summary': {
            ChangeType.DEFINE:
                {'count': 25, 'removed': 514},
            ChangeType.CELL_SINGLETON:
                {'count': 56, 'removed': 179},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 4, 'removed': 9},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 8, 'removed': 18},
            ChangeType.ROW_SUB_SET:
                {'count': 2, 'removed': 9},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },

    227698: {
        'grid': "   692   "
                "     4  3"
                " 9137  2 "
                "6 3     5"
                " 7  4  8 "
                "2     1 9"
                " 1  3527 "
                "5  4     "
                "   967   ",
        'difficulty': Difficulty.MOYEN,
        'solved': True,
        'summary': {
            ChangeType.DEFINE:
                {'count': 29, 'removed': 566},
            ChangeType.CELL_SINGLETON:
                {'count': 52, 'removed': 163},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 0, 'removed': 0},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 0, 'removed': 0},
            ChangeType.ROW_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },

    41430: {
        'grid': "  5 4   3"
                "72   6   "
                "      8 1"
                "  386  7 "
                "8       6"
                " 9  513  "
                "5 7      "
                "   6   14"
                "4   8 9  ",
        'difficulty': Difficulty.DIABOLIQUE,
        'solved': True,
        'summary': {
            ChangeType.DEFINE:
                {'count': 26, 'removed': 539},
            ChangeType.CELL_SINGLETON:
                {'count': 55, 'removed': 127},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 15, 'removed': 25},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 8, 'removed': 13},
            ChangeType.ROW_SUB_SET:
                {'count': 10, 'removed': 25},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },

    513089: {
        'grid': " 13 6   9"
                " 2 8     "
                "4     2  "
                "  95  6 3"
                "         "
                "7 5  69  "
                "  6     1"
                "     5 2 "
                "2   3 78 ",
        'difficulty': Difficulty.DEMONIAQUE,
        'solved': False,
        'summary': {
            ChangeType.DEFINE:
                {'count': 24, 'removed': 509},
            ChangeType.CELL_SINGLETON:
                {'count': 20, 'removed': 81},
            ChangeType.EXCLUSIVE_ROW_IN_SQUARE:
                {'count': 5, 'removed': 17},
            ChangeType.EXCLUSIVE_COLUMN_IN_SQUARE:
                {'count': 5, 'removed': 9},
            ChangeType.ROW_SUB_SET:
                {'count': 6, 'removed': 11},
            ChangeType.COLUMN_SUB_SET:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_SET:
                {'count': 0, 'removed': 0},
        }
    },
}
