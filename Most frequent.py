"""
Write a program that take  strings and returns the  most frequent character in it.
"""

def most_frequent_character(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_char = ''
    max_count = 0
    for char, count in char_count.items():
        if count > max_count:
            max_char = char
            max_count = count

    return max_char


input_string = "hello world"
result = most_frequent_character(input_string)
print(f"The most frequent character in '{input_string}' is: '{result}'")
