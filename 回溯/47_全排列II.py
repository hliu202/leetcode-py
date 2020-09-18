from util.common_imports import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def search(left,history):
            nonlocal ret
            if not left: #如果没有可以搜的了，说明所有数字用完了
                ret.append(history)

            for i in set(left): #只考虑了当前位置不重复选择，那也就能保证history不重复，所以直接用一个集合来维护
                left.remove(i)
                left.append(i)
                search(left[:-1],history+[i])

        search(nums,[])
        return ret


print2D(Solution().permuteUnique([1,1,2]))

# 作者：xiao-yan-gou
# 链接：https://leetcode-cn.com/problems/permutations-ii/solution/jian-ji-si-lu-11xing-python-by-xiao-yan-gou/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。