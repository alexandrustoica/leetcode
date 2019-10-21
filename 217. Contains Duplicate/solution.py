class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for item in nums:
            if item in elements:
                return True
            elements.add(item)
        return False
            
