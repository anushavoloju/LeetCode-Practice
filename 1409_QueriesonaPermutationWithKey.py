class Solution:
    def processQueries(self, queries, m: int):
        P = [i for i in range(1,m+1)]
        res = []
        for i in range(len(queries)):
            val = queries[i]
            ind = P.index(val)
            res.append(ind)
            P.remove(val)
            P.insert(0,val)
        return res

        
s = Solution()
print(s.processQueries([3,1,2,1],5))
print(s.processQueries([4,1,2,2],4))
print(s.processQueries([7,5,5,8,3],8))