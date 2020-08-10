class Solution:
    def orangesRotting(self, grid) -> int:
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        rotten_indices = set()
        fresh_indices = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_indices.add((i,j))
                if grid[i][j] == 1:
                    fresh_indices.add((i,j))
        while len(fresh_indices) > 0:
            if len(rotten_indices) == 0:
                return -1
            new_rotten = set()
            for (i,j) in rotten_indices:
                if (i+1,j) in fresh_indices:
                    new_rotten.add((i+1,j))
                    fresh_indices.remove((i+1,j))
                if (i-1,j) in fresh_indices:
                    new_rotten.add((i-1,j))
                    fresh_indices.remove((i-1,j))
                if (i,j+1) in fresh_indices:
                    new_rotten.add((i,j+1))
                    fresh_indices.remove((i,j+1))
                if (i,j-1) in fresh_indices:
                    new_rotten.add((i,j-1))
                    fresh_indices.remove((i,j-1))
            rotten_indices = new_rotten
            minutes = minutes + 1
        return minutes

        
s = Solution()
#print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
#print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
#print(s.orangesRotting([[0],[2]]))
print(s.orangesRotting([[1,2,1,1,2,1,1]]))