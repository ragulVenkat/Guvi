"""
Give a Python List [10, 501, 22, 37, 100, 999, 87, 315] find out how many numbers are there in the given Python List which are Happy Numbers
"""


Python_List = [10, 501, 22, 37, 100, 999, 87, 315]
Happy_number = []
def is_happy(Python_List):
    for i in range (len(Python_List)):
        sum = Python_List[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
           Happy_number.append(Python_List[i])
    return Happy_number
print(is_happy(Python_List))