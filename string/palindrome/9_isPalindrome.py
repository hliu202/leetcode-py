# https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        D = 1
        y = x
        while y >= 10:
            y /= 10
            D *= 10
        
        while x > 0: # = 10:
            R = x % 10
            L = x // D
            if R != L:
                return False

            x %= D
            x //= 10
            D /= 100

        return True
# print(Solution().isPalindrome(1221))
# print(Solution().isPalindrome(123454321))
# print(Solution().isPalindrome(10))
# print(Solution().isPalindrome(1000021))
print(Solution().isPalindrome(2000022))

