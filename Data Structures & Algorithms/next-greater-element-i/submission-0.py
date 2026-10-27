class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {num : i for i, num in enumerate(nums1)}
        res = [-1 for _ in nums1]

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                res[indices[stack.pop()]] = cur
            if cur in indices:
                stack.append(cur)
        return res
