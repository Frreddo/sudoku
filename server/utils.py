from itertools import combinations
from typing import List

MIN_NB_OF_CONTAINERS = 3


def exclusive_sub_list(containers_list: List[List[any]]):
    """Returns an exclusive sub-list from a list of containers, or None if no exclusive sub-list is found.

    An exclusive sub-list is found when the set formed with the content of containers in the sub-list
    has the same length as the sub-list (as many elements in the set as elements in the sub-list)."""
    if len(containers_list) < MIN_NB_OF_CONTAINERS:
        raise ValueError("Containers' list must contain at least 3 elements")

    # Iterate through all possible sub-lists
    container_indexes = [x for x in range(len(containers_list))]
    for sub_list_size in range(2, len(containers_list)):
        for sub_list_indexes in combinations(container_indexes, sub_list_size):
            # Create the set with content from containers in sub-list
            sub_list_content_set = set()
            for container in [containers_list[pos] for pos in sub_list_indexes]:
                for i in range(len(container)):
                    sub_list_content_set.add(container[i])

            if len(sub_list_content_set) == sub_list_size:
                # If sub-list is exclusive, return it
                return sub_list_content_set, sub_list_indexes
    return None

