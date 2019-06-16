# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
#
# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
occurence = 0
for c in range(len(s)-2):
    if(s[c:c+3] == 'bob'):
        occurence += 1

print('Number of times bob occurs is:',occurence)
