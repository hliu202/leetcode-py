
a = "hello"

# 大小写
c1 = a[0].upper()
c2 = c1.lower()
print(c1, c2)

b1 = a.title()
b2 = a.lower()
print(b1, b2)

# join & split
b = ['hello', 'world', '!']
bb = '[' + ','.join(b) + ']'
print(bb)  # str
print(bb[1:-1].split(',')) # list

# to list
L = list('0123456789')
print(L)

# char
print(ord('1')-ord('0'))
print(ord('a'))
print(chr(97)) # a

# to int
print(int("255"))
