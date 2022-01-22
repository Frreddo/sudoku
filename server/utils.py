from itertools import combinations
from typing import List

MIN_MEMBERS = 3


def get_sub_set(members: List[List[any]]):
    if len(members) < MIN_MEMBERS:
        raise ValueError('List of members must contain at least 3 elements')
    positions = [p for p in range(len(members))]
    for size in range(2, len(members)):
        for c in combinations(positions, size):
            c_set = set()
            for member in [members[pos] for pos in c]:
                for i in range(len(member)):
                    c_set.add(member[i])
            if len(c_set) == size:
                return c_set, c
    return None

