
s = "111001"
c = [0, s.count('1')]
res = 0

res = -10000
cur = 0 # max count(0) - count(1) from left
ones = 0 # ones: 1) from right, 2) extra 1s subtructed by left.
for i,c in enumerate(s):
    if c == '0':
        cur += 1
    else:
        cur -= 1
        ones += 1
    if i < len(s) - 1:
        res = max(res, cur)

print (res + ones)
