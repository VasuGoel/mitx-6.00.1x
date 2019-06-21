# This code won't produce the desired output as we are iterating over a currently mutating list

# def remove_dups(L1, L2):
#     for e in L1:
#         if e in L2:
#             L1.remove(e)
#
# L1 = [1, 2, 3, 4, 5]
# L2 = [1, 2, 3, 4 ,5]
# print(f'Before mutation and iteration -> L1: {L1}, L2: {L2}')
# remove_dups(L1, L2)
# print(f'After mutation and iteration -> L1: {L1}, L2: {L2}')


# This code produces the desired output cuz we are iterating over a list which is not mutated throughout the code
def remove_dups(L1, L2):
    # Cloning list
    dup_L1 = L1[:]
    for e in dup_L1:
        if e in L2:
            L1.remove(e)

L1 = [1, 2, 3, 4, 5]
L2 = [4 ,5, 6, 7, 8]
print(f'Before mutation and iteration -> L1: {L1}, L2: {L2}')
remove_dups(L1, L2)
print(f'After mutation and iteration -> L1: {L1}, L2: {L2}')
