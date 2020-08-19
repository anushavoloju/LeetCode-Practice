class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        res = []
        start = left
        while start <= right:
            digits = list(str(start))
            valid = True
            for d in digits:
                if int(d) == 0 or start % int(d) != 0:
                    valid = False
                    break
                else:
                    continue
            if valid:
                res.append(start)
            start = start + 1
        return res
            
        
s = Solution()
print(s.selfDividingNumbers(1, 22))