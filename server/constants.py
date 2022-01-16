from enum import Enum, auto


class ChangeType(Enum):
    DEFINE = auto()
    CELL_SINGLETON = auto()
    SQUARE_SUB_ROW = auto()
