class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j = 0, len(s)-1
        lastD = None
        while i != j and i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue

            if not lastD: # can del i or j
                if i + 1 <= j:
                    if s[i + 1] == s[j]:
                        lastD = (True, i, j)  # try del s[j] again
                        i += 2
                        j -= 1
                        continue
                    elif s[i] == s[j-1]:
                        i += 1
                        j -= 2
                        lastD = (False, i, j)
                        continue
            elif lastD[0]:
                i = lastD[1]
                j = lastD[2]
                if s[i] == s[j-1]:
                    i += 1
                    j -= 2
                    lastD = (False, i, j)
                    continue
            return False
        return True

print(Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
# print(Solution().validPalindrome('abcda'))
# print(Solution().validPalindrome('aba'))


# 该题解的实现过于复杂，简洁明了的实现如下：

# class Solution {
# public:
#     bool palindrome(const std::string& s, int i, int j)
#     {
#         for ( ; i < j && s[i] == s[j]; ++i, --j);
#         return i >= j;
#     }

#     bool validPalindrome(string s) {
#         int i = 0, j = s.size() - 1;
#         for ( ; i < j && s[i] == s[j]; ++i, --j);        
#         return palindrome(s, i, j - 1) || palindrome(s, i + 1, j);
#     }
# };