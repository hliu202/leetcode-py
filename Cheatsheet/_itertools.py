# https://docs.python.org/3/library/itertools.html
# Functions creating iterators for efficient looping
from itertools import *

# Combinatoric iterators:
for i in product('ABCD', repeat=2):
    print (i, end=' ')
# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
print()

for i in product('ABCD', 'xy'):
    print (i, end=' ')
# Ax Ay Bx By Cx Cy Dx Dy
print()

for i in product('AB', 'xy', '12'):
    print (i, end=' ')
print()
