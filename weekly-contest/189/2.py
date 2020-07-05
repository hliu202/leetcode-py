import collections


class Solution:
    def arrangeWords(self, text: str) -> str:
        sp = text.split(" ")
        D = collections.defaultdict(list)
        for i, s in enumerate(sp):
            D[len(s)].append(i)
        idex_sorted = list(D.keys())
        idex_sorted.sort()

        res = ""
        for i, le in enumerate(idex_sorted):
            for j, k in enumerate(D[le]):
                if i == 0 and j == 0:
                    res += sp[k].capitalize()  # first letter
                elif k == 0:
                    res += " " + sp[k].lower()
                else:
                    res += " " + sp[k]
        return res

print(Solution().arrangeWords(text="Leetcode is cool"))
print(Solution().arrangeWords(text="To be or to be not"))

