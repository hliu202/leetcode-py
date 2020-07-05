# Below solution divides the problem into subproblems of size y/2 and call the subproblems recursively.
# Python3 program to calculate pow(x,n)

# Function to calculate x
# raised to the power y
def quick_power(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return 1
    elif y % 2 == 0: # even
        a = quick_power(x, y // 2)
        return a * a
    else: # odd
        a = quick_power(x, y // 2)
        return x * a * a


# Driver Code
x = 2
y = 3
print(quick_power(2, 3))
# print(quick_power(5, 2))
