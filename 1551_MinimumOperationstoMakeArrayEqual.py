class Solution:
    def minOperations(self, n: int) -> int:
        mid = n
        res = 0
        if mid % 2 == 1:
            mid = mid - 2
        else:
            mid = mid - 1
        while mid > 0:
            res = res + n - mid
            mid = mid - 2
        return res
        
s = Solution()
print(s.minOperations(3))
print(s.minOperations(6))
