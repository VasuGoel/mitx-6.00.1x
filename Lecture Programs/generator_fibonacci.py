def genFib():
    f1 = 0
    f2 = 1
    yield 0
    yield 1
    while True:
        next = f1 + f2
        yield next
        f1 = f2
        f2 = next

fib = genFib()
n = int(input('How many fibonacci numbers would you like? - '))
for i in range(n):
    print(fib.__next__())
