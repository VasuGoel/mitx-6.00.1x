# Given function calls a function 'func' for each element in list 'list'.

# def applyToEach(list, func):
#     for x in list:
#         print(func(x, 100))
#
# def increment(num, offset):
#     return num + offset
#
# list = [1, 2, 3, 4, 5]
# applyToEach(list, increment)

# -----------------------------------------------------------------------------------

# map(fun, iter) function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

def square(n):
    return n*n

numbers = (1, 2, 3)
results = map(square, numbers)
print(results)          # <map object at 0x102f61048>
print(type(results))    # <class 'map'>
print(list(results))    # [1, 4, 9]

for i in map(square, numbers):
    print(i)
