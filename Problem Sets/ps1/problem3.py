# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#
# Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#
# Longest substring in alphabetical order is: abc

s = 'efabgkpb'
seq = s[0]
longest_seq = s[0]

for c in s[1:]:
    if c >= seq[-1]:
        seq += c
        if len(seq) > len(longest_seq):
            longest_seq = seq
    else:
        seq = c

    print(f'On character - {c}')
    print(f'Seq - {seq}')
    print(f'Longest_seq - {longest_seq}')
    print()

print('Longest substring in alphabetical order is:' + longest_seq)


# -----------------------------------------------------------------------------------
# Original Logic
# -----------------------------------------------------------------------------------

# s = 'azcbobobegghakl'
# seq = s[0]
# longest_seq = s[0]
#
# for c in range(len(s)-1):
#     if s[c] <= s[c+1]:
#         if seq == '':
#             seq = s[c:c+2]
#         else:
#             seq += s[c+1]
#     else:
#         if len(seq) > len(longest_seq):
#             longest_seq = seq
#         seq = ''
#
# if len(seq) > len(longest_seq):
#     print ('Longest substring in alphabetical order is: ' + seq)
# else:
#     print ('Longest substring in alphabetical order is: ' + longest_seq)
