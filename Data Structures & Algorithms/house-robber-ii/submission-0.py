class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev_rob, max_rob = 0, 0
            for i in range(len(nums)):
                temp = max(prev_rob + nums[i], max_rob)
                prev_rob = max_rob
                max_rob = temp
            return max_rob
        
        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))