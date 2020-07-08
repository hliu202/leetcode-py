# https://leetcode-cn.com/problems/diving-board-lcci/

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]

        ans = []
        for i in range(k + 1):
            ns = k - i
            ans.append(ns * shorter + longer * i)

        return ans

# 在所有 Python3 提交中击败了
# 17.42%
# 的用户

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]

        sub = longer - shorter

        # return list(range(shorter * k, longer * k + 1, sub)) # 步长
        cur = shorter * k
        ans = [cur]
        i = 1 # number of longer
        while i <= k:
            cur += sub
            ans.append(cur)
            i += 1

        return ans

# 在所有 Python3 提交中击败了
# 77.15%
# 的用户