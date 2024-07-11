"""
You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 315] your task is to create two List ,one which have all the Even Numbers and another List which will have all the ODD numbers in it ?

"""
Python_List = [10, 501, 22, 37, 100, 999, 87, 315]

even_numbers = []
odd_numbers = []

for number in Python_List:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
