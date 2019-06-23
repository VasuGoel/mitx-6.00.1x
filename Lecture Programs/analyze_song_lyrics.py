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
    print("\nLoading lyrics from file ...")
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
    print('\n', wordlist, '\n')
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
wordlist = loadlyrics()
