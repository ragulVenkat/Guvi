"""
Write a program that take strings and returns the true if it is palindrome, False otherwise
"""
str_1 = input("Enter the string to check if it is a palindrome: ")

str_1 = str_1.casefold()

rev_str = reversed(str_1)

is_palindrome = list(str_1) == list(rev_str)
print(is_palindrome)
