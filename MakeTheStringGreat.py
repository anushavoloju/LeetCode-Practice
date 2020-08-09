class Solution:
    def makeGood(self, s: str) -> str:
        chars = list(s)
        i = 0
        res = ''
        print(chars)
        while i < len(chars)-1:
            if (abs(ord(chars[i])-ord(chars[i+1]))) == 32:
                chars.pop(i)
                chars.pop(i)
                print(chars)
                i = 0
            else:
                i = i + 1
        for c in chars:
            res = res + c
        print(res)

        
s = Solution()
print(s.makeGood(""))