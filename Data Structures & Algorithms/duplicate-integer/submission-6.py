class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            if nums[i] in nums[i + 1:]:
                return True
            i+=1
        return False