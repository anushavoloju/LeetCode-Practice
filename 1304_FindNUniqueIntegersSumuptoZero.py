class Solution:
    def sumZero(self, n: int):
        right = 1
        left = -1
        res = [0]
        while len(res) < n - 1:
            res.append(right)
            res.insert(0,left)
            right = right + 1
            left = left - 1
        if len(res) == n:
            return res
        else:
            res.remove(0)
            res.insert(0,left)
            res.append(right)
            return res
        
s = Solution()
print(s.sumZero(5))
print(s.sumZero(2))
print(s.sumZero(1))