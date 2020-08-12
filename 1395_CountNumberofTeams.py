class Solution:
    def numTeams(self, rating) -> int:
        teams = 0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        teams += 1
                    elif rating[i] > rating[j] and rating[j] > rating[k]:
                        teams += 1
                    else:
                        continue
        return teams

        
s = Solution()
print(s.numTeams([2,5,3,4,1]))
print(s.numTeams([2,1,3]))