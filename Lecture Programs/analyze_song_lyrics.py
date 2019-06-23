"""
Created on Sun Jun 23 18:18 2019

@author: Vasu Goel
"""

LYRICS_FILENAME = "lyrics.txt"

def loadlyrics():
    """
    Returns a list of all words in the lyrics.

    Depending on the size of the lyics, this function may
    take a while to finish.
    """
    print("\nLoading lyrics from file ...\n")
    # # inFile: file
    # inFile = open(LYRICS_FILENAME, 'r')
    # # line: string
    # line = inFile.readline()
    # # wordlist: list of strings
    # wordlist = line.split()
    # print(len(wordlist), "words loaded.")
    # return wordlist
    with open(LYRICS_FILENAME) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
    wordlist = []
    for line in content:
        l = line.split()
        for word in l:
            wordlist.append(word)
    print(wordlist, '\n')
    print(len(wordlist), "words processed.\n")
    return wordlist


def welcome():
    msg = '''
Welcome to the song lyrics analyzer!

Instructions: Paste the lyrics of the song you wish to analyze in a new file 'lyrics.txt' inside the same directory as this program.
    '''
    return msg


print(welcome())
input('Press \'Enter\' after you\'ve created \'lyrics.txt\'...')
# Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program
wordlist = loadlyrics()


def lyrics_to_frequencies(wordlist):
    """
    wordlist (list): list of words (strings) of song lyrics

    Returns a dictionary mapping different lyrics words to their frequencies or number of occurences
    """
    myDict = {}
    for word in wordlist:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


lyrics_dict = lyrics_to_frequencies(wordlist)
print(lyrics_dict)


def most_common_words(lyrics_dict):
    """
    lyrics_dict (dictionary): dictionary containing mapping of different words in lyrics and their frequencies

    Returns most commonly occuring word/s (if many) and their frequency
    """
    values = lyrics_dict.values()
    best = max(values)
    words = []
    for key in lyrics_dict:
        if lyrics_dict[key] == best:
            words.append(key)
    return (words, best)

most_common, freq = most_common_words(lyrics_dict)
print(f'\n\nMost common word - {most_common}, Frequency - {freq}\n')


def words_often(lyrics_dict, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(lyrics_dict)
        if temp[1] >= minTimes:
            result.append(temp)
            for word in temp[0]:
                del(lyrics_dict[word])
        else:
            done = True
    return result


minTimes = int(input('Enter a threshold frequency - '))
print(f'Words that appeared at least {minTimes} times are - \n')
print(words_often(lyrics_dict, minTimes), '\n')
