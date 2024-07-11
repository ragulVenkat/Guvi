"""
Write a program to find to find the sum of the first and the last digit of a integer.
"""


def sum_first_and_last_digit(n):
    n_str = str(n)
    
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])
    
    sum_digits = first_digit + last_digit
    
    return sum_digits

number = 123456
result = sum_first_and_last_digit(number)
print("Sum of the first and last digit:", result)
