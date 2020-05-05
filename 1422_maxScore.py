# https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/

s = "111001"
c = [0, s.count('1')]
res = 0

for i in s[:-1]:
    if i == '0':
        c[0] = c[0] + 1
    else:
        c[1] = c[1] - 1
    res = max(res, c[0] + c[1])

print(res)
