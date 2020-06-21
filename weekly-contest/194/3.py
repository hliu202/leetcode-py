from util.common_imports import *
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [1] * n
        j = 0 # 第几轮下雨，和排水
        D = defaultdict(int)
        pump = []
        i = 0
        while i < n:
            r = rains[i]
            if r > 0:
                res[i] = -1
                if r in D:
                    jj = D[r]
                    while jj < j:
                        if pump[jj]:
                            idx = pump[jj].popleft() # 排水
                            res[idx] = r
                            break
                        else:
                            jj += 1
                    if jj == j: # 没有空位排水
                        return []
                D[r] = j
                i += 1
            else:
                p = deque()
                while i < n:
                    p.append(i)
                    i += 1
                    if i < n and rains[i] != 0:
                        break
                pump.append(p)
                j += 1
        return res

# print (Solution().avoidFlood(rains = [1,2,3,4]))
# print (Solution().avoidFlood(rains = [1,2,0,0,2,1]))
# print (Solution().avoidFlood(rains = [1,2,0,1,2]))
# print (Solution().avoidFlood(rains = [69,0,0,0,69]))
# print (Solution().avoidFlood(rains = [10,20,20]))
print (Solution().avoidFlood([1,0,2,0]))
