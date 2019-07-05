# Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)
#
# This function takes in a dictionary and returns a list.

a = {'a':1, 'b':1, 'c':2, 'd':3, 'e':4, 'f':4, 'h':5, 'g':6}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    dict_list = []
    # Append keys with unique values to dict_list
    for k, v in aDict.items():
        if list(aDict.values()).count(v) == 1:
            dict_list.append(k)
    dict_list.sort()
    return dict_list



print(uniqueValues(a))
