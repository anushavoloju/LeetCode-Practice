class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        res = [0]*num_people
        i = 0
        counter = 0
        while i < num_people:
            if candies >= (counter * num_people) + i + 1:
                candies = candies - (counter * num_people) - i - 1
                res[i] = res[i] + (counter * num_people) + i + 1
            else:
                res[i] = res[i] + candies
                candies = 0
                return res
            if candies > 0:
                if i == num_people - 1:
                    i = 0
                    counter = counter + 1
                else:
                    i = i + 1
            else:
                return res

        
s = Solution()
#print(s.distributeCandies(7,4))
#print(s.distributeCandies(10,3))
print(s.distributeCandies(60,4))