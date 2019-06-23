numFibCalls = 0

def fibonacci(n):
    # Declaring variable as global will help to access it ouside the scope of function
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input('What term of fibonacci series do you wish to get?\n'))
print(f'fibonacci({n}) : {fibonacci(n)}')
print(f'numFibCalls : {numFibCalls}')
