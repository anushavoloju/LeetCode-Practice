class Solution:
    def eraseOverlapIntervals(self, intervals) -> int: 
        count = 0
        sorted_intervals = sorted(intervals, key = lambda x : x[1])
        curr_end = float('-inf')
        for start, end in sorted_intervals:
            if start >= curr_end:
                curr_end = end
            else:
                count += 1
        return count
        
s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))