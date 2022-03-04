from enum import Enum, auto


class ChangeType(Enum):
    DEFINE = auto()
    CELL_SINGLETON = auto()
    EXCLUSIVE_ROW_IN_SQUARE = auto()
    EXCLUSIVE_COLUMN_IN_SQUARE = auto()
    ROW_SUB_SET = auto()
    COLUMN_SUB_SET = auto()
    SQUARE_SUB_SET = auto()
