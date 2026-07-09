class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # curr = [2, 2]

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # add next val to curr
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # BACKTRACK
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res