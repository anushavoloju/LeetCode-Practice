class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        res = ''
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
        for d in digits:
            res = res + d
        return int(res)


        
s = Solution()
print(s.maximum69Number(9669))