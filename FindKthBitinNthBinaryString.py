class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sequence = {}
        sequence[1] = '0'
        for i in range(2,n+1):
            previous = sequence[i-1]
            value = previous + "1" + self.reverse_of_inverse(previous)
            sequence[i] = value
        res = sequence[n][k-1]
        return res

    def reverse_of_inverse(self, string):
        inv = ''
        for c in string:
            if c == '1':
                inv = inv + '0'
            else:
                inv = inv + '1'
        rev = inv[::-1]
        return rev
        




        
s = Solution()
print(s.findKthBit(3,1))
print(s.findKthBit(4,11))
print(s.findKthBit(1,1))
print(s.findKthBit(2,3))