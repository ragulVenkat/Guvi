"""
Write a program that takes a string and returns the new string with all the vowels removed
"""

String = input("Enter the string : ")
String = String.lower()
result = str()

for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pass
    else:
        result = result + i   

if len(result) == 0:
    print('No vowel found in ' + String)
else:
    print('After removing vowels : ' + result)