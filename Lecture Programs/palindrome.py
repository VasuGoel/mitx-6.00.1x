def isPalindrome(str):
    if len(str) == 1:
        return True
    else:
        return str[0] == str[-1] and isPalindrome(str[1:-1])


str = input('Enter a string - ')
if isPalindrome(str):
    print('\nIt is indeed a palindrome\n')
else:
    print('\nIt is not a palindrome\n')
