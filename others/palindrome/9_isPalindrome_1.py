class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        revert = 0
        while x > revert:
            revert = revert*10 + x % 10
            x //= 10

        return x == revert or x == revert//10 # 奇数 or 偶数

# https://leetcode-cn.com/problems/palindrome-number/solution/dong-hua-hui-wen-shu-de-san-chong-jie-fa-fa-jie-ch/

# print(Solution().isPalindrome(1221))
# print(Solution().isPalindrome(123454321))
# print(Solution().isPalindrome(10))
# print(Solution().isPalindrome(1000021))
print(Solution().isPalindrome(2000022))

