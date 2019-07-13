def genPrimes():
    primes = [2]
    yield primes[0]
    n = 3
    while True:
        # all() Return True if all elements of the iterable are true (or if the iterable is empty) while, any() return True if any element of the iterable is true. If the iterable is empty, return False
        if all(p % n != 0 for p in primes):
            primes.append(n)
        if n == primes[-1]:
            yield n
        n += 2


primes = genPrimes()
n = int(input('How many prime numbers would you like? - '))
for i in range(n):
    print(primes.__next__())
