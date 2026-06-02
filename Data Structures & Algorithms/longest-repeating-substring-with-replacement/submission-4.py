class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, length, max_freq = 0, 0, 0
        freq = defaultdict(int)

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length
            
