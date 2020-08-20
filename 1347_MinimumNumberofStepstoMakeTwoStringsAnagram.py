class Solution:
    def minSteps(self, s: str, t: str) -> int:
        steps = 0
        for c in t:
            if c in s:
                i = s.index(c)
                s = s[:i] + s[i+1:]
            else:
                steps += 1
        return steps
            
        
s = Solution()
print(s.minSteps("bab","aba"))
print(s.minSteps("leetcode","practice"))
print(s.minSteps("anagram","mangaar"))
print(s.minSteps("xxyyzz","xxyyzz"))
print(s.minSteps("friend","family"))