from util.common_imports import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates = list(set(candidates))
        candidates.sort()
        ans = []
        n = len(candidates)

        def traverse(start, cur_target, cur_list):
            nonlocal ans
            if start == n:
                return

            if candidates[start] > cur_target:
                return

            if candidates[start] == cur_target:
                cur_list.append(candidates[start])
                ans.append(cur_list)
                return

            # how many cur?
            i = 0
            cur = candidates[start]
            while cur * i <= cur_target:
                n_list = cur_list.copy()
                if cur * i == cur_target:
                    n_list.extend([cur] * i)
                    ans.append(n_list)
                    return

                n_list.extend([cur] * i)
                traverse(start + 1, cur_target - cur * i, n_list)
                i += 1

        traverse(0, target, [])
        return ans

print(Solution().combinationSum(candidates = [2,3,6,7], target = 7))
print(Solution().combinationSum(candidates = [2,3,5], target = 8))
