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


def welcome():
    msg = '''
Welcome to the song lyrics analyzer!

Instructions: Paste the lyrics of the song you wish to analyze in a new file 'lyrics.txt' inside the same directory as this program.
    '''
    return msg


print(welcome())
input('Press \'Enter\' after you\'ve created \'lyrics.txt\'...')
print("\nLoading lyrics from file ...")
