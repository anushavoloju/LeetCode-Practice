class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_strings = 0
        L_count = 0
        R_count = 0
        for c in s:
            if c == 'L':
                L_count = L_count + 1
            if c == 'R':
                R_count = R_count + 1
            if L_count == R_count:
                balanced_strings = balanced_strings + 1
                L_count = 0 
                R_count = 0
        return balanced_strings


        
s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLLLLRRRLR"))
print(s.balancedStringSplit("LLLLRRRR"))