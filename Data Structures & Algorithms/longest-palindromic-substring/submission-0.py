class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest, pal = 1, s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i-j <= 2 or dp[i-1][j+1]):
                    dp[i][j] = True
                    if i-j+1 > longest:
                        longest = i-j+1
                        pal = s[j:i+1]
        
        return pal