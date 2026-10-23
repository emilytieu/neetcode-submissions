class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        return countS == countT