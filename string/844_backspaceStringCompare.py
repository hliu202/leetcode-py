class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def trim(s: str) -> str:
            i, n = 0, len(s)
            res = ""
            while i < n:
                if s[i] == "#":
                    res = res[0:-1]
                else:
                    res += s[i]
                i += 1
            return res

        S = trim(S)
        T = trim(T)
        return S == T


print(Solution().backspaceCompare(S="ab#c", T="ad#c"))
print(Solution().backspaceCompare(S="ab##", T="c#d#"))
print(Solution().backspaceCompare(S="a##c", T="#a#c"))
print(Solution().backspaceCompare(S="a#c", T="b"))
print(Solution().backspaceCompare(S="bxj##tw", T="bxo#j##tw"))
