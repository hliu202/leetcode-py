class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        cur = strs[0]
        for s in strs[1:]:
            if not s:
                return ""

            i = 0
            n = min(len(cur), len(s))
            while i < n and cur[i] == s[i]:
                i += 1
            if i == 0:
                return ""
            else:
                cur = cur[0:i]
        return cur


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["dog", ""]))
