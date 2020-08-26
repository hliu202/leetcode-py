from util.common_imports import *


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def fs(cur):
            if cur == 1:
                return [nums[0:2]]

            cur_val = nums[cur]
            i = cur - 1 # 第一个不为 cur_val 的
            while nums[i] == nums[cur] and i > 0:
                i -= 1
            if i == 0:
                res = []
                for i in range(1, cur): # 
                    tail = [cur_val] * i
                    res.append([nums[0]].extend(tail))
                return res
            
            res = fs(i)

            res_ext = []
            cur_list = []
            for j in range(1, cur - i+1):
                cur_list.append([cur_val] * j)

            for L in res:
                for cur_L in cur_list:
                    Le = L.copy()
                    Le.extend(cur_L)
                    res_ext.append(Le)

            res.extend(res_ext)
            for j in range(0, i+1):
                if j == 0 or nums[j - 1] != nums[j]:  # 1个元素 + cur
                    for cur_L in cur_list:
                        Le = [nums[j]]
                        Le.extend(cur_L)
                        res.append(Le)

            res.extend(cur_list[1:])
            return res

        return fs(len(nums) - 1)


print(Solution().findSubsequences([4, 6, 7, 7]))

# !不能 sort
print(Solution().findSubsequences([[4,3,2,1]])) # []
