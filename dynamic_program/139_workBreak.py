# https://leetcode-cn.com/problems/word-break/

from util.common_imports import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        max_len, wordSet = -1, set()
        for w in wordDict:
            wordSet.add(w)
            max_len = max(max_len, len(w))
        if max_len <= 0:
            return False

        f = [False] * n  # !f(i)是否重复计算
        starts = deque()
        starts.append(0)
        while starts:
            i = starts.popleft()
            for j in range(i, min(n, i + max_len)):
                if s[i : j + 1] in wordSet:
                    if j + 1 == n:
                        return True
                    if not f[j + 1]:
                        starts.append(j + 1)
                        f[j + 1] = True
        return False


print(
    Solution().wordBreak(
        s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        wordDict=[
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ],
    )
)
