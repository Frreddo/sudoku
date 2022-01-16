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
        'solved': False,
        'summary': {
            ChangeType.DEFINE:
                {'count': 28, 'removed': 546},
            ChangeType.CELL_SINGLETON:
                {'count': 7, 'removed': 30},
            ChangeType.SQUARE_SUB_ROW:
                {'count': 4, 'removed': 6},
            ChangeType.SQUARE_SUB_COLUMN:
                {'count': 1, 'removed': 1},
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
            ChangeType.SQUARE_SUB_ROW:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_COLUMN:
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
        'solved': False,
        'summary': {
            ChangeType.DEFINE:
                {'count': 25, 'removed': 514},
            ChangeType.CELL_SINGLETON:
                {'count': 6, 'removed': 45},
            ChangeType.SQUARE_SUB_ROW:
                {'count': 4, 'removed': 9},
            ChangeType.SQUARE_SUB_COLUMN:
                {'count': 6, 'removed': 14},
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
            ChangeType.SQUARE_SUB_ROW:
                {'count': 0, 'removed': 0},
            ChangeType.SQUARE_SUB_COLUMN:
                {'count': 0, 'removed': 0},
        }
    },
}
