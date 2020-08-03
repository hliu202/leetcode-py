from util.common_imports import *


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        last = 0
        ct = 0
        dq = deque(arr)
        last = dq.popleft()
        max_val = -1
        count = 0
        N = len(arr) * 2
        while count < N:
            if last > dq[0]:
                ct +=1
                dq.append(dq.popleft())
                if ct == k:
                    return last
            else:
                dq.append(last)
                last = dq.popleft()
                ct = 1
                if ct == k:
                    return last
            
            count += 1
            max_val = max(last, max_val)
        return max_val
        
print(Solution().getWinner(arr = [3,2,1], k = 10))
print(Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2))
print(Solution().getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7))
print(Solution().getWinner(arr = [1,25,35,42,68,70], k = 1))
print(Solution().getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000))
