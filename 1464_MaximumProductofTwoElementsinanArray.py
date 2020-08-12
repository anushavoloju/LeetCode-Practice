class Solution:
    def maxProduct(self, nums) -> int:
        max_value = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = (nums[i]-1) * (nums[j]-1)
                if prod > max_value:
                    max_value = prod
        return max_value

        
s = Solution()
print(s.maxProduct([3,4,5,2]))
print(s.maxProduct([1,5,4,5]))
print(s.maxProduct([3,7]))