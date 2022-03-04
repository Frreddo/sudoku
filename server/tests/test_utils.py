from collections import namedtuple
from unittest import TestCase

from utils import exclusive_sub_list


TestData = namedtuple('TestData', ['input', 'result'])


class ExclusiveSubListTestCase(TestCase):
    def test_valid_results(self):
        data = [
            TestData({'containers': [[1, 2], [1, 3], [1, 2]]}, {'set': {1, 2}, 'indexes': (0, 2)}),
            TestData(
                {'containers': [[1, 2, 4], [3, 4, 7], [3, 4, 7], [1, 2, 3, 4, 7], [3, 7]]},
                {'set': {3, 4, 7}, 'indexes': (1, 2, 4)}
            ),
        ]
        for x in data:
            sub_set, indexes = exclusive_sub_list(x.input['containers'])
            self.assertEqual(x.result['set'], sub_set)
            self.assertEqual(x.result['indexes'], indexes)

    def test_invalid_results(self):
        data = [
            TestData({'containers': [[1, 2], [1, 3], [1, 2, 3]]}, None),
        ]
        for x in data:
            self.assertEqual(x.result, exclusive_sub_list(x.input['containers']))

    def test_short_member_lists_are_rejected(self):
        with self.assertRaises(ValueError):
            exclusive_sub_list([[1, 2, 4], [2, 3, 4]])
