class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        count = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev:
                prev = end
            else:
                prev = min(prev, end)
                count += 1
        
        return count