class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n  > 0:
            res += n % 2    # will give 1 or 0
            n = n >> 1      # shift to right by 1
        return res    

        # O(1) b/c 32 bit integer is constant