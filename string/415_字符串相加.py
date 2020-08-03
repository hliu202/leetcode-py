class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1: return num2
        if not num2: return num1

        n1 = len(num1)
        n2 = len(num2)
        i = 1
        res = []
        carry = 0

        chars = list('0123456789')

        while i <= n1 and i <= n2:
            cur = (ord(num1[-i]) - ord('0')) + (ord(num2[-i]) - ord('0')) + carry
            carry = cur // 10

            res.append(chars[cur % 10])
            i += 1

        i -= 1
        if carry == 0:
            if i == n1:
                return num2[0:-i] + ''.join(res[::-1])
            else:
                return num1[0:-i] + ''.join(res[::-1])
        else:
            if i == n1:
                return self.addStrings(num2[0:-i], '1') + ''.join(res[::-1])
            else:
                return self.addStrings(num1[0:-i], '1') + ''.join(res[::-1])

print(Solution().addStrings("72345", "2345678"))
