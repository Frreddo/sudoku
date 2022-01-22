from collections import namedtuple
from unittest import TestCase

from utils import get_sub_set


TestData = namedtuple('TestData', ['input', 'result'])


class SubSetTestCase(TestCase):
    def test_valid_results(self):
        data = [
            TestData({'members': [[1, 2], [1, 3], [1, 2]]}, {'sub_set': {1, 2}, 'indexes': (0, 2)}),
            TestData(
                {'members': [[1, 2, 4], [3, 4, 7], [3, 4, 7], [1, 2, 3, 4, 7], [3, 7]]},
                {'sub_set': {3, 4, 7}, 'indexes': (1, 2, 4)}
            ),
        ]
        for x in data:
            sub_set, indexes = get_sub_set(x.input['members'])
            self.assertEqual(x.result['sub_set'], sub_set)
            self.assertEqual(x.result['indexes'], indexes)

    def test_invalid_results(self):
        data = [
            TestData({'members': [[1, 2], [1, 3], [1, 2, 3]]}, None),
        ]
        for x in data:
            self.assertEqual(x.result, get_sub_set(x.input['members']))

    def test_short_member_lists_are_rejected(self):
        with self.assertRaises(ValueError):
            get_sub_set([[1, 2, 4], [2, 3, 4]])
