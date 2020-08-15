class Solution:
    def destCity(self, paths) -> str:
        for _,d1 in paths:
            path_found = False
            for s2,_ in paths:
                if d1 == s2:
                    path_found = True
            if path_found == False:
                return d1
        return ''


        
s = Solution()
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(s.destCity([["B","C"],["D","B"],["C","A"]]))
print(s.destCity([["A","Z"]]))