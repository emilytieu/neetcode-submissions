class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob, max_rob = 0, 0
        for n in nums:
            temp = max(n + prev_rob, max_rob)
            prev_rob = max_rob
            max_rob = temp
        return max_rob