# Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function. You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.
#
# Sample Output and Hints
# Here is how the game output should look...
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: u
#
# Current Hand: a s r e t t t
# Enter word, or a "." to indicate that you are finished: tatters
# "tatters" earned 99 points. Total: 99 points
#
# Run out of letters. Total score: 99 points.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
#
# Enter u to have yourself play, c to have the computer play: c
#
# Current Hand:  a s r e t t t
# "stretta" earned 99 points. Total: 99 points
#
# Total score: 99 points.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: me
# Invalid command.
#
# Enter u to have yourself play, c to have the computer play: you
# Invalid command.
#
# Enter u to have yourself play, c to have the computer play: c
#
# Current Hand:  a c e d x l n
# "axled" earned 65 points. Total: 65 points
#
# Current Hand:  c n
# Total score: 65 points.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: u
#
# Current Hand: a p y h h z o
# Enter word, or a "." to indicate that you are finished: zap
# "zap" earned 42 points. Total: 42 points
#
# Current Hand: y h h o
# Enter word, or a "." to indicate that you are finished: oy
# "oy" earned 10 points. Total: 52 points
#
# Current Hand: h h
# Enter word, or a "." to indicate that you are finished: .
# Goodbye! Total score: 52 points.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
#
# Enter u to have yourself play, c to have the computer play: c
#
# Current Hand:  a p y h h z o
# "hypha" earned 80 points. Total: 80 points
#
# Current Hand:  z o
# Total score: 80 points.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: e
# Hints about the output
# Be sure to inspect the above sample output carefully - very little is actually printed out in this function specifically. Most of the printed output actually comes from the code you wrote in playHand and compPlayHand - be sure that your code is modular and uses function calls to these helper functions!
#
# You should also make calls to the dealHand helper function. You shouldn't make calls to any other helper function that we've written so far - in fact, this function can be written in about 15-20 lines of code.
#
# Here is the above output, with the output from playHand and compPlayHand obscured:
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
# You have not played a hand yet. Please play a new hand first!
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: u
#
# <call to playHand>
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
#
# Enter u to have yourself play, c to have the computer play: c
#
# <call to compPlayHand>
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: x
# Invalid command.
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: me
# Invalid command.
#
# Enter u to have yourself play, c to have the computer play: you
# Invalid command.
#
# Enter u to have yourself play, c to have the computer play: c
#
# <call to compPlayHand>
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: n
#
# Enter u to have yourself play, c to have the computer play: u
#
# <call to playHand>
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: r
#
# Enter u to have yourself play, c to have the computer play: c
#
# <call to compPlayHand>
#
# Enter n to deal a new hand, r to replay the last hand, or e to end game: e
# Hopefully this hint makes the problem seem a bit more approachable.
#
# A Note On Runtime
# You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the compChooseWord function.
#
# Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).
#
# IMPORTANT:Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.
#
# Entering Your Code
# Be sure to only paste your definition for playGame from ps4b.py in the following box. Do not include any other function definitions.


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet.
          Please play a new hand first!"

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
