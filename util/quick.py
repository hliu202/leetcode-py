# Below solution divides the problem into subproblems of size y/2 and call the subproblems recursively.
# Python3 program to calculate pow(x,n)

# Function to calculate x
# raised to the power y
def quick_power(x, y):
    if y == 0:
        return 1
    elif int(y % 2) == 0:
        return quick_power(x, int(y / 2)) * quick_power(x, int(y / 2))
    else:
        return x * quick_power(x, int(y / 2)) * quick_power(x, int(y / 2))


# Driver Code
x = 2
y = 3
print(quick_power(2, 3))
print(quick_power(5, 2))
