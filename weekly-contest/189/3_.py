# 暴力循环
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        n = len(favoriteCompanies)
        favoriteCompanies = list(set(f) for f in favoriteCompanies)
        for i in range(n):
            for j in range(n):
                if i != j and favoriteCompanies[i].issubset(
                        favoriteCompanies[j]):
                    break
            else:
                res.append(i)
        return res

# 作者：suibianfahui
# 链接：https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/solution/di-189-chang-zhou-sai-ti-jie-by-suibianfahui-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。