class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        initial_matrix = [[0]*m]*n
        count = 0
        for index in indices:
            for r in range(0,n):
                initial_matrix[r][index[1]] += 1
            for c in range(0,m):
                initial_matrix[index[0]][c] += 1
        for i in range(n):
            for j in range(m):
                if (initial_matrix[i][j]) % 2 != 0:
                    count = count + 1
        #print(initial_matrix)
        return count
    
    def oddCells2(self, n: int, m: int, indices) -> int:
        rows = [0]*n
        cols = [0]*m
        count = 0
        for r,c in indices:
            rows[r] += 1
            cols[c] += 1
        for i in range(n):
            for j in range(m):
                if (rows[i] + cols[j]) % 2 == 1:
                    count = count + 1
        #print(initial_matrix)
        return count

s = Solution()
print(s.oddCells2(2,3,[[0,1],[1,1]]))
print(s.oddCells2(2,2,[[1,1],[0,0]]))
print(s.oddCells2(48, 37, [[40,5]]))