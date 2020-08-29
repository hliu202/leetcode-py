# https://leetcode-cn.com/problems/longest-palindromic-substring/

# TRANS: Pi-1,j+1 = Pi,j and si-1 == sj+1
# INIT: Pii = True
#       Pii+1 = (si == si+1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = (1, 0) # len, i
        for L in range(n):
            for i in range(n):
                j = i + L
                cur_len = L + 1
                if j >= n:
                    break
                if L == 0:
                    dp[i][j] = True
                elif L == 1:
                    dp[i][j] = s[i] == s[j]
                    if dp[i][j] and res[0] < cur_len:
                        res = (cur_len, i)
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                    if dp[i][j] and res[0] < cur_len:
                        res = (cur_len, i)
        return s[res[1]:res[1]+res[0]]

print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('babad'))
