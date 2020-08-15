class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        chars = list(S)
        res = []
        final_str = ''
        l_count, r_count = 0, 0
        start, end = 0, len(chars)
        for i,c in enumerate(chars):
            if c == '(':
                l_count +=  1
            if c == ')':
                r_count +=  1
            if l_count == r_count:
                end = i
                l_count = 0
                r_count = 0
                res.append(chars[start:end+1])
                start = i + 1
        for i in range(len(res)):
            res[i].pop(0)
            res[i].pop()
            for c in res[i]:
                final_str += c
        return final_str

        
s = Solution()
print(s.removeOuterParentheses("(()())(())"))
print(s.removeOuterParentheses("(()())(())(()(()))"))
print(s.removeOuterParentheses("()()"))