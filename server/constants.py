from enum import Enum, auto


class ChangeType(Enum):
    DEFINE = auto()
    CELL_SINGLETON = auto()
    SQUARE_SUB_ROW = auto()
    SQUARE_SUB_COLUMN = auto()
    LINE_SUB_SET = auto()
