class Solution:
            
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        accumulator = dict()
        for index, num in enumerate(nums):
            if target - num in accumulator:
                return [accumulator[target - num], index]
            accumulator[num] = index
        return None
