# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
#
# Number of vowels: 5

s = 'azcbobobegghakl'
count = 0
for c in s:
    if(c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        count += 1

print('Number of vowels:', count)
