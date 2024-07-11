"""
Create a Pyramid of numbers from 1 to 20 using For loop
"""

# pyramid_row_Number = int(20)

# for i in range(pyramid_row_Number):
#     for j in range(i+1):
#         print(j+1 ," ", end="")
#     print()


pyramid_row_number = int(20)

for i in range(pyramid_row_number):
    print(' ' * (pyramid_row_number - i - 1), end='')
    for j in range(i + 1):
        print(j + 1, "", end="")
    print()