class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count, l = 0, 0

        for c in range(len(s)):
            while s[c] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[c])
            count = max(count, c - l + 1)
        
        return count