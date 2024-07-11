"""
Give a Python List [10, 501, 22, 37, 100, 999, 87, 315] your task is to Count all the Prime Numbers and create a new Python List which will contain all the prime Numbers in it ?

"""

Python_list =  [10, 501, 22, 37, 100, 999, 87, 315]
prime = []
for i in Python_list:
    c = 0
    for j in range(1,i):
        if i % j == 0:
            c+= 1
    if c== 1 :
        prime.append(i)
print("Prime Numbers are : ",prime)
count_prime_numbers = len(prime)
print("Count of prime numbers:", count_prime_numbers)
