class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        T = {'a', 'e', 'i', 'o', 'u'}
        cur = 0
        o = k - 1
        for i in range(k):
            if s[i] in T:
                cur += 1
        res = cur
        for i in range(1, len(s) - o):
            j = i + o
            if s[i-1] in T:
                cur -= 1
            if s[j] in T:
                cur += 1
            res = max(cur, res)
        return res

# print(Solution().maxVowels(s = "abciiidef", k = 3))
# print(Solution().maxVowels(s = "aeiou", k = 2))
# print(Solution().maxVowels(s = "leetcode", k = 3))
# print(Solution().maxVowels(s = "leetcode", k = 1))
# print(Solution().maxVowels(s = "rhythms", k = 4))
# print(Solution().maxVowels(s = "tryhard", k = 4))
print(Solution().maxVowels(s = "weallloveyou", k = 7)) # 4
