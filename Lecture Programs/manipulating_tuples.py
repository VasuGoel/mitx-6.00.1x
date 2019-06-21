def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)

    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return min_nums, max_nums, unique_words   # return (min_nums, max_nums, unique_words)

smallest, largest, unique_words_count = get_data(((1, 'Vasu'), (2, 'James'), (3, 'Lily'), (4, 'Vasu')))

print(f'smallest: {smallest}, largest: {largest}, unique_words: {unique_words_count}')
