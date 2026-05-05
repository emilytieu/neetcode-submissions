class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # num -> index

        for i, n in enumerate(nums): # enumerate() returns index, value starting at index 0 by default
            indices[n] = i
        
        for i, n in enumerate(nums): 
            # for each index i, check if its complement is in indices.
            if target - n in indices and indices[target - n] != i:
                return [i, indices[target - n]]
        
        