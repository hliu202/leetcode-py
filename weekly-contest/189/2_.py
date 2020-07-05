import collections


# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         sp = text.split(" ")
#         D = collections.defaultdict(list)
#         for i, s in enumerate(sp):
#             D[len(s)].append(i)
#         idex_sorted = list(D.keys())
#         idex_sorted.sort()

#         res = ""
#         for i, le in enumerate(idex_sorted):
#             for j, k in enumerate(D[le]):
#                 if i == 0 and j == 0:
#                     res += sp[k].capitalize()  # first letter
#                 elif k == 0:
#                     res += " " + sp[k].lower()
#                 else:
#                     res += " " + sp[k]
#         return res
# print(Solution().arrangeWords(text="Leetcode is cool"))
# print(Solution().arrangeWords(text="To be or to be not"))


class Solution:
    def arrangeWords(self, text: str) -> str:
        a = text.split()
        a[0] = a[0].lower()
        d = collections.defaultdict(list)
        for s in a:
            d[len(s)].append(s)
        res = []
        for k in sorted(d.keys()):
            res.extend(d[k])
        res[0] = res[0].title()
        return " ".join(res)


# 作者：suibianfahui
# 链接：https://leetcode-cn.com/problems/rearrange-words-in-a-sentence/solution/di-189-chang-zhou-sai-ti-jie-by-suibianfahui-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
