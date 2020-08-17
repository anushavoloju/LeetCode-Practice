class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        for row in grid:
            while len(row) > 0:
                last = row.pop()
                if last < 0:
                    count = count + 1
        return count


 
s = Solution()
print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(s.countNegatives([[3,2],[1,0]]))
print(s.countNegatives([[1,-1],[-1,-1]]))
print(s.countNegatives([[-1]]))