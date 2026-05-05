class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for index, num in enumerate(nums):  # O(n) time
            indices[num] = index   # O(n) space
        
        for index, num in enumerate(nums):
            if target - num in indices and index != indices[target - num]:
                return [index, indices[target - num]]