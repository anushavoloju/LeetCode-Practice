class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        i = 1
        min_time = 0
        while i < len(points):
            first = points[i-1]
            second = points[i]
            diff = max(abs(second[0]-first[0]), abs(second[1]-first[1]))
            min_time = min_time + diff
            i = i + 1
        return min_time

        
s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
print(s.minTimeToVisitAllPoints([[3,2],[-2,2]]))