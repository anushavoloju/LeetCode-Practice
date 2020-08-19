class Solution:
    def flipAndInvertImage(self, A):
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1
        return A



        
s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))