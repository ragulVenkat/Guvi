"""
Write a program that take  strings and returns Ture if it is an anagram of another  string,or it will be false
"""

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")
