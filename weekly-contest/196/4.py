from util.common_imports import *
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        N = len(num)
        v2idx = defaultdict(list)
        for i in range(N):
            v = int(num[i])
            N[v].append(i)

        