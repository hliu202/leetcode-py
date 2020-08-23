from util.common_imports import *
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m

        SS, ES = defaultdict(int), defaultdict(int) # 开始和结束的 index, 以及他们之间的steps (存 1 个就好)
        nm = 0 # 当前满足 m 条件的数量
        last = -1 # 上次存在 m 条件 > 0 的结果
        ans = -1 # 最终结果

        # 维护 ranges, 更新满足 m 条件的个数, 保存答案
        for i in range(0,len(arr)):
            v = arr[i]
            if v - 1 in ES:
                old_step = ES[v-1]
                start = v-1 - old_step
                del ES[v-1]
                
                ES[v] = old_step + 1
                SS[start] = ES[v]
            
                cur_len = SS[start] + 1
                if old_step + 1 == m:
                    nm -= 1
                if v + 1 in SS: #concate
                    old_step2 = SS[v+1]
                    end = v+1 + old_step2
                    del SS[v+1]

                    SS[start] = old_step + old_step2 + 2
                    ES[end] = SS[start]

                    if old_step2 + 1 == m:
                        nm -= 1
                    cur_len = SS[start] + 1
            elif v+1 in SS:
                old_step = SS[v+1]
                end = v+1 + old_step
                del SS[v+1]
                
                SS[v] = old_step + 1
                ES[end] = SS[v]
            
                cur_len = SS[v] + 1
                if old_step + 1 == m:
                    nm -= 1
            else:
                SS[v], ES[v] = 0, 0
                cur_len = 1

            if cur_len == m:
                nm += 1
            if nm > 0:
                last = i + 1
            if nm == 0 and last > 0:
                ans = last
        return ans

print(Solution().findLatestStep(arr = [3,5,1,2,4], m = 1)) # 4
print(Solution().findLatestStep(arr = [3,1,5,4,2], m = 2))
print(Solution().findLatestStep(arr = [1], m = 1))
print(Solution().findLatestStep(arr = [2,1], m = 2))
print(Solution().findLatestStep(arr = [2,1], m = 1))
print(Solution().findLatestStep([3,1,5,4,2], 2)) # -1
print(Solution().findLatestStep([3,1,2], 1)) # 2
