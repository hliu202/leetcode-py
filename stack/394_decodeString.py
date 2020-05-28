# https://leetcode-cn.com/problems/decode-string/

from util.common_imports import *

class Solution:
    def decodeString(self, s: str) -> str:
        def traverse(i):
            res = ''
            N = 0
            while i < len(s):
                if s[i] >= '0' and s[i] <= '9':
                    N = N*10 + int(s[i])
                elif s[i] == '[':
                    i,tmp = traverse(i+1)
                    res += N * tmp
                    N = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1

            return res

        return traverse(0)

# print(Solution().decodeString(s = ""))
print(Solution().decodeString("3[a]2[b4[F]c]"))
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# print(Solution().decodeString(s = "3[a]2[bc]"))
# print(Solution().decodeString(s = "3[a2[c]]"))
# print(Solution().decodeString(s = "2[abc]3[cd]ef"))
