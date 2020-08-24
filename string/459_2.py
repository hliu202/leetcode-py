class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)

                    
print(Solution().repeatedSubstringPattern("abab")) # a bababa b
print(Solution().repeatedSubstringPattern("aba")) # a baab a