from util.common_imports import *

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        mono_stack = deque()
        res = []
        for i in range(len(T)-1,-1,-1):
            while mono_stack and T[i] >= T[mono_stack[0]]: # !注意是 >=，而不是 >
                mono_stack.popleft()
            if not mono_stack:
                res.append(0)
            else:
                res.append(mono_stack[0] - i)
            mono_stack.appendleft(i)
        return res[::-1]

# print (Solution().dailyTemperatures(T = [73, 74, 75, 71, 69, 72, 76, 73]))
print (Solution().dailyTemperatures(T = [89,62,70,58,47,47,46,76,100,70])) # [8,1,5,4,3,2,1,1,0,0]
