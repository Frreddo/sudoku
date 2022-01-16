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
                {'count': 3, 'removed': 16}
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
                {'count': 45, 'removed': 127}
        }
    },
}
