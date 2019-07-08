def get_ratios(L1, L2):
    """
    Assume L1 and L2 as lists of equal lengths

    Return list of containing L1[i]/L2[i]
    """
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/float(L2[i]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  # Appends nan i.e. not a number
        except:
            raise ValueError('get_ratios called with bad arguments')
    return ratios

# print(get_ratios([1, 2, 3, 4, 5], [6, 7, 8, 9, 0])) prints [0.16666666666666666, 0.2857142857142857, 0.375, 0.4444444444444444, nan]

print(get_ratios([1, 2, 3], [4, 's', 6]))
