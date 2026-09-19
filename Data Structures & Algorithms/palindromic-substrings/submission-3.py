class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    count += 1
        return count