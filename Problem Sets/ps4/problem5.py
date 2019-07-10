# In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.
#
# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.
#
# Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:
#
# Test Cases
# Case #1
# Function Call:
# wordList = loadWords()
# playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
# Output:
#   Current Hand:  a c i h m m z
#   Enter word, or a "." to indicate that you are finished: him
#   "him" earned 24 points. Total: 24 points
#
#   Current Hand:  a c m z
#   Enter word, or a "." to indicate that you are finished: cam
#   "cam" earned 21 points. Total: 45 points
#
#   Current Hand:  z
#   Enter word, or a "." to indicate that you are finished: .
#   Goodbye! Total score: 45 points.
# Case #2
# Function Call:
# wordList = loadWords()
# playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
# Output:
#   Current Hand:  a s t t w f o
#   Enter word, or a "." to indicate that you are finished: tow
#   "tow" earned 18 points. Total: 18 points
#
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: tasf
#   Invalid word, please try again.
#
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: fast
#   "fast" earned 28 points. Total: 46 points
#
#   Run out of letters. Total score: 46 points.
# Case #3
# Function Call:
# wordList = loadWords()
# playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
# Output:
#   Current Hand: a r e t i i n
#   Enter word, or a "." to indicate that you are finished: inertia
#   "inertia" earned 99 points. Total: 99 points
#
#   Run out of letters. Total score: 99 points.
# Additional Testing
# Be sure that, in addition to the listed tests, you test the same basic test conditions with varying values of n. n will never be smaller than the number of letters in the hand.
