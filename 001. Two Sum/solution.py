import unittest
from typing import List


def get_indexes(nums: List[int], target: int) -> List[int]:
    accumulator = dict()
    for index, num in enumerate(nums):
        if target - num in accumulator:
            return [accumulator[target - num], index]
        accumulator[num] = index
    return []


class TwoSumTest(unittest.TestCase):
    def test_when_getting_indexes_with_valid_nums_and_target_expect_correct_indexes(self):
        # given:
        subject, nums, target = [0, 1], [2, 7, 11, 15], 9
        # when:
        result = get_indexes(nums, target)
        # then:
        self.assertEqual(result, subject)

    def test_when_getting_indexes_expect_correct_indexes(self):
        # given:
        subject, nums, target = [1, 2], [3, 2, 4, 6], 6
        # when:
        result = get_indexes(nums, target)
        # then:
        self.assertEqual(result, subject)


if __name__ == '__main__':
    unittest.main()
