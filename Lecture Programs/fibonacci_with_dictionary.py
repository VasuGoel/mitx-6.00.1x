# Dictionary to store calculated fibonacci terms to save computational time while computing larger fibonacci terms.
aDict = {
    # 1st and 2nd term in fibonacci series is 0 and 1 respectively
    1: 0,
    2: 1
}

numFibCalls = 0

def fibonacci_efficient(n, aDict):
    global numFibCalls
    numFibCalls += 1
    if n in aDict:
        return aDict[n]
    else:
        ans = fibonacci_efficient(n-1, aDict) + fibonacci_efficient(n-2, aDict)
        aDict[n] = ans
        return ans


n = int(input('What term of fibonacci series do you wish to get?\n'))
print(f'fibonacci_efficient({n, aDict}) : {fibonacci_efficient(n, aDict)}')
print(f'numFibCalls : {numFibCalls}')
