class Solution:
    def hIndex(self, citations) -> int:
        citations.sort()
        res = 0
        for i,c in enumerate(citations):
            if c >= len(citations) - i:
                res = len(citations) - i
                break
        return res

        

s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([3,0,6,1,5,4]))