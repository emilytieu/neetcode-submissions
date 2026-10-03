class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in range(len(nums)-2, -1, -1):
            while nums[i] > 0:
                if (i + nums[i]) < len(nums) and dp[i + nums[i]]:
                    dp[i] = True
                    break
                nums[i] -= 1
        
        return dp[0]
