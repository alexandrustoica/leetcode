import unittest
from typing import List


class TwoIndexesOfSum(list):
    def __init__(self, target: int, source: List[int]):
        accumulator = dict()
        for index, num in enumerate(source):
            if target - num in accumulator:
                super().__init__([accumulator[target - num], index])
            accumulator[num] = index


class TwoSumTest(unittest.TestCase):

    def test_when_getting_indexes_with_valid_nums_and_target_expect_correct_indexes(self):
        # given:
        subject, nums, target = [0, 1], [2, 7, 11, 15], 9
        # when:
        result = TwoIndexesOfSum(target, source=nums)
        # then:
        self.assertEqual(result, subject)

    def test_when_getting_indexes_expect_correct_indexes(self):
        # given:
        subject, nums, target = [1, 2], [3, 2, 4, 6], 6
        # when:
        result = TwoIndexesOfSum(target, source=nums)
        # then:
        self.assertEqual(result, subject)

    def test_when_getting_indexes_with_empty_nums_expect_correct_indexes(self):
        # given:
        subject, nums, target = [], [], 6
        # when:
        result = TwoIndexesOfSum(target, source=nums)
        # then:
        self.assertEqual(result, subject)


if __name__ == '__main__':
    unittest.main()
