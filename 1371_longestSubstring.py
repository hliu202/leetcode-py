# https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

# Fi: A0^A1^..Ai
# Fij: Ai^...^Aj
# Fij = F(i-1) ^ Fj
#   求 Fij = 0的最大 j - (i-1)
# a,e,i,o.u: 1,2,4,8,16, others:0

# 前缀表达式

from collections import defaultdict

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        F = [0] * len(s)
        D = defaultdict(list)
        res = 0

        for i, c in enumerate(s):
            if c == 'a':
                F[i] = F[i-1]^1
            elif c == 'e':
                F[i] = F[i-1]^2
            elif c == 'i':
                F[i] = F[i-1]^4
            elif c == 'o':
                F[i] = F[i-1]^8
            elif c == 'u':
                F[i] = F[i-1]^16
            else:
                F[i] = F[i-1]
            if F[i] == 0:
                res = i + 1
            else:
                D[F[i]].append(i)

        for v in D.values():
            if len(v) > 1:
                res = max(res, v[-1] - v[0])

        return res

print (Solution().findTheLongestSubstring('bcbcbc'))
print (Solution().findTheLongestSubstring('eleetminicoworoep'))
print (Solution().findTheLongestSubstring('leetcodeisgreat'))

# 内存消耗 : 42.9 MB , 在所有 Python3 提交中击败了 100.00% 的用户



