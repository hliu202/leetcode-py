
from util.common_imports import *
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        D = defaultdict(int)
        for v in arr:
            D[v % k] += 1

        for key in D.keys():
            t_key = k - key
            if key == 0:
                if D[key] % 2 != 0:
                    return False
            elif t_key not in D:
                return False
            else:
                if t_key == key:
                    if D[key] % 2 != 0:
                        return False
                elif (D[key] + D[t_key]) % 2 != 0:
                    return False
        return True

# print (Solution().canArrange(arr = [-1,1,-2,2,-3,3,-4,4], k = 3))
# print (Solution().canArrange(arr = [-10,10], k = 2))
# print (Solution().canArrange(arr = [1,2,3,4,5,6], k = 10))
# print (Solution().canArrange(arr = [1,2,3,4,5,6], k = 7))
# print (Solution().canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
print (Solution().canArrange(arr = [3,8,17,2,5,6], k = 10))