class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        if len(arr) < 1:
            return k
        res = 0
        count = 0
        missing = []
        if arr[0] != 1:
            for s in range(1,arr[0]):
                missing.append(s)
                count = count + 1
                if count == k:
                    res = missing.pop()
                    return res
        for i in range(1,len(arr)):
            start = arr[i-1]
            end = arr[i]
            for j in range(start+1,end):
                missing.append(j)
                count = count + 1
                if count == k:
                    res = missing.pop()
                    return res
        if count != k:
            last = arr.pop()
            for c in range(last+1,last+1+k-count):
                missing.append(c)
            res = missing.pop()
        return res







        
s = Solution()
print(s.findKthPositive([2,3,4,7,11], 5))
print(s.findKthPositive([1,2,3,4], 2))
print(s.findKthPositive([1], 2))