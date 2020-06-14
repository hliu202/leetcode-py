# the zip function in Python 3 returns an iterator. Iterators can only be
# exhausted (by something like making a list out of them) once. The purpose
# of this is to save memory by only generating the elements of the iterator
# as you need them, rather than putting it all into memory at once.
# If you want to reuse your zipped object, just create a list out of it as you
# do in your second example, and then duplicate the list by something like

# https://www.programiz.com/python-programming/methods/built-in/zip

# 1. 长度相同的 iterator
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)

# 2. 长度不同
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_list = list(result)
print(result_list)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_list = list(result)
print(result_list)

# 3. unzip
# The * operator can be used in conjunction with zip() to unzip the list.
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)

# 3.1 行列变换
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix_ = list(zip(*matrix))
print (matrix_)