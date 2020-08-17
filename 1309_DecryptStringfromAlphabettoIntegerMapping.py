class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ''
        alpha_int_map = {}
        first = 97
        for i in range(1,10):
            alpha_int_map[str(i)] = chr(first)
            first = first + 1
        for i in range(10,27):
            alpha_int_map[str(i)+'#'] = chr(first)
            first = first + 1
        i = 0
        while i < len(s):
            if (i + 2) < len(s) and s[i+2] == '#':
                c = alpha_int_map.get(s[i]+s[i+1]+s[i+2])
                result = result + c
                i = i + 3
            else:
                c = alpha_int_map.get(s[i])
                result = result + c
                i = i + 1
        return result



        
s = Solution()
print(s.freqAlphabets("10#11#12"))
print(s.freqAlphabets("1326#"))
print(s.freqAlphabets("25#"))
print(s.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))