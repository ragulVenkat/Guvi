"""
Write a python program to find the first non - repeating elements in a given list of integers
"""

def first_non_repeating_element(list):
    count_dict = {}
    
    for element in list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    
    for element in list:
        if count_dict[element] == 1:
            return element
    
    return None

list = [4, 5, 1, 2, 0, 4, 1, 2, 5, 7, 8, 8]
result = first_non_repeating_element(list)
print("The first non-repeating element is:", result)
