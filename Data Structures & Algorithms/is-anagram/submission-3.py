class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if s and t are the same length
        if len(s) != len(t):
            return False

        countS, countT = {}, {} # Initialize 2 hash maps

        for i in range(len(s)): # s and t are same len
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT # s and t hash maps are the same