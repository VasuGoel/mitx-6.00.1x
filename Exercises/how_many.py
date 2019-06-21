# Consider the following sequence of expressions:
#
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.
#
# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:
#
# >>> print(how_many(animals))
# 6

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    result = 0
    for l in aDict.values():
        result += len(l)
    return result

print(how_many(animals))
