class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tempMax = curMax
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * tempMax, n * curMin)
            res = max(res, curMax)
        
        return res