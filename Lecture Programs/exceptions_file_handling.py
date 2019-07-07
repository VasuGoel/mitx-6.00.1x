FILENAME = input('Enter the filename - ')

try:
    fh = open(FILENAME, 'r')
except IOError:
    print('Cannot open file:', FILENAME)
else:
    with open(FILENAME) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    wordlist = []
    for line in content:
        l = line.split()
        for word in l:
            wordlist.append(word.lower())
    print('\n', wordlist, '\n')

    fh.close()
