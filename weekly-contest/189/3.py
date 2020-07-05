import collections


class Solution:
    def peopleIndexes(self, favoriteCompanies):
        D = collections.defaultdict(list)
        for i, L in enumerate(favoriteCompanies):
            D[len(L)].append(i)

        K = list(D.keys())
        K.sort(reverse=True)

        res = D[K[0]]
        resSets = []
        for i in res:
            resSets.append(set(favoriteCompanies[i]))

        # !同len的set不用比较（一定不一样）
        for i in range(1, len(K)):
            for j in D[K[i]]:
                curSet = set(favoriteCompanies[j])
                isSub = False
                for pre in resSets:
                    if curSet.issubset(pre):
                        isSub = True
                        break
                if not isSub:
                    resSets.append(curSet)
                    res.append(j)

        res.sort()
        return res


print(
    Solution().peopleIndexes(
        [
            ["leetcode", "google", "facebook"],
            ["leetcode", "amazon"],
            ["facebook", "google"],
        ]
    )
)
print(Solution().peopleIndexes([["leetcode"], ["google"], ["facebook"], ["amazon"]]))
print(
    Solution().peopleIndexes(
        [
            ["leetcode", "google", "facebook"],
            ["google", "microsoft"],
            ["google", "facebook"],
            ["google"],
            ["amazon"],
        ]
    )
)

