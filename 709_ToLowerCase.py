class Solution:
    def toLowerCase(self, str: str) -> str:
        new_str = ''
        for c in str:
            if ord(c) >= 65 and ord(c) <= 90:
                new_str += chr(ord(c) + 32)
            else:
                new_str += c
        return new_str

        
s = Solution()
print(s.toLowerCase('Hello'))