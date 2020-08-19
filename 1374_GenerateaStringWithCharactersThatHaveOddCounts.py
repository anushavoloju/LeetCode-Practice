import random
import string
class Solution:
    def generateTheString(self, n: int) -> str:
        res = ''
        if n % 2 == 0:
            rand_letter = random.choice(string.ascii_lowercase)
            res = res + (rand_letter * (n-1))
            if rand_letter == 'z':
                res = res + 'a' 
            else:
                res = res + chr(ord(rand_letter)+1)
        else:
            rand_letter = random.choice(string.ascii_lowercase)
            res = res + (rand_letter * n)
        return res

        
s = Solution()
print(s.generateTheString(4))
print(s.generateTheString(2))
print(s.generateTheString(5))