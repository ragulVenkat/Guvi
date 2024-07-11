"""
You have been given 3 Lists . Your task is to find the duplicates in the three lists,Write a python program for the same. You can use your own python lists
"""


def find_duplicates(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    duplicates = set1 & set2 & set3
    
    return list(duplicates)

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9, 10]
list3 = [5, 6, 7, 11, 12, 13, 14]

duplicates = find_duplicates(list1, list2, list3)
print("Duplicates in the three lists:", duplicates)
