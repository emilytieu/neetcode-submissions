class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap) # O(n)

        for n in nums[k:]:
            if n > minheap[0]:
                heapq.heapreplace(minheap, n)
        return minheap[0]