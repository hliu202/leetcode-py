class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        i_e = s.find("E")
        if i_e == -1:
            i_e = s.find("e")
        dig_set = set()
        for c in '0123456789':
            dig_set.add(c)

        def trim(mi):
            if not mi: return ''
            if mi[0] == '-' or mi[0] == '+':
                return mi[1:]
            return mi

        def isInt(mi):
            if not mi: return False

            for c in mi:
                if c not in dig_set:
                    return False
            return True

        if i_e != -1:
            return isInt(trim(s[0:i_e])) and isInt(trim(s[i_e+1:]))

        s = trim(s)
        if not s: return False

        i_d = s.find('.')
        if i_d == 0:
            return isInt(s[1:])
        elif i_d == len(s) - 1:
            return isInt(s[:-1])
        elif i_d == -1:
            return isInt(s)
        else:
            return isInt(s[0:i_d]) and isInt(s[i_d+1:])

print(Solution().isNumber("46.e3")) # true
print(Solution().isNumber("3.")) # true

# for ip in ['.1 ', "+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]:
#     print(Solution().isNumber(ip))

# for ep in ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]:
#     print(Solution().isNumber(ep))
