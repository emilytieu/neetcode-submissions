class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt in dp:
                return dp[amt]

            res = 1e9
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + dfs(amt - coin))

            dp[amt] = res
            return res
            
        count = dfs(amount)
        return -1 if count >= 1e9 else count