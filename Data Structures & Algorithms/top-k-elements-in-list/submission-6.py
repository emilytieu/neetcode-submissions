class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # e.g. [1, 1, 1, 2, 2, 3]
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # list of n [] elements

        # {1: 3, 2: 2, 3: 1}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # [0, 3, 2, 1]
        for n, c in count.items():
            freq[c].append(n) # count of value n at index n
        
        result = []
        for i in range(len(freq) - 1, 0, -1): # start at last index, go backwards by 1 until reach index 0
            for n in freq[i]: # last index = highest count
                result.append(n)
                if len(result) == k:
                    return result
        
        