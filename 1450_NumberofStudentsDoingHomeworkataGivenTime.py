class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        if len(startTime) != len(endTime):
            return 0
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                count = count + 1
        return count

        

s = Solution()
print(s.busyStudent([1,2,3],[3,2,7],4))
print(s.busyStudent([4],[4],4))
print(s.busyStudent([4],[4],5))
print(s.busyStudent([1,1,1,1],[1,3,2,4],7))
print(s.busyStudent([9,8,7,6,5,4,3,2,1],[10,10,10,10,10,10,10,10,10],5))