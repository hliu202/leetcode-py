class Solution:
    def makeGood(self, s: str) -> str:
        LEN = ord("a") - ord("A")
        while True:
            mod = False
            i = 0
            while i < len(s) - 1:
                if abs(ord(s[i]) - ord(s[i + 1])) == LEN: #!反之亦然
                    s = s[0:i] + s[i + 2 : len(s)]
                    mod = True
                else:
                    i += 1
            if not mod:
                break
        return s


print(Solution().makeGood(s="leEeetcode"))
print(Solution().makeGood(s="abBAcC"))
print(Solution().makeGood(s="s"))
print(Solution().makeGood(s="Pp"))
