class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        i = 0
        while i < len(arr)-2:
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
            i = i + 1
        return False

        
s = Solution()
print(s.threeConsecutiveOdds([2,6,4,1]))
print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))