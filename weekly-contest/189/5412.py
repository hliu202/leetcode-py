class Solution:
    def busyStudent(self, startTime, endTime, queryTime) -> int:
        res = 0
        for i,v in enumerate(startTime):
            if v > queryTime:
                continue
            if queryTime <= endTime[i]:
                res += 1
        return res

# print(Solution().busyStudent(startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
print(Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 5))