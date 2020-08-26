class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            if len(tmp) > 1:
                res.append(tmp)
            curPres = set()
            for inx, i in enumerate(nums):
                if i in curPres:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres.add(i)
                    dfs(nums[inx+1:], tmp+[i])

        dfs(nums, [])
        return res

# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/increasing-subsequences/solution/python3-chao-xiang-xi-duo-jie-fa-by-ting-ting-28/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。