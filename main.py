"""
write a python program to calculate the total number of vowels and count of each individual vowel AEIOU in the string "Guvi Geeks Network Private Limited"?

"""


text = input("Enter the Text : ")

num_of_a = 0
num_of_A = 0
num_of_e = 0
num_of_E = 0
num_of_i = 0
num_of_I = 0
num_of_o = 0
num_of_O = 0
num_of_u = 0
num_of_U = 0


for vowel_words in text:
        if vowel_words == 'a':
            num_of_a += 1
        elif vowel_words == 'e':
            num_of_e += 1
        elif vowel_words == 'i':
            num_of_i += 1
        elif vowel_words == 'o':
            num_of_o += 1
        elif vowel_words == 'u':
            num_of_u += 1
        elif vowel_words == 'A':
            num_of_A += 1
        elif vowel_words == 'E':
            num_of_E += 1
        elif vowel_words == 'I':
            num_of_I += 1
        elif vowel_words == 'O':
            num_of_O += 1
        elif vowel_words == 'U':
            num_of_U += 1

total_vowels = num_of_a + num_of_A + num_of_e + num_of_E + num_of_i + num_of_I + num_of_o + num_of_O + num_of_u + num_of_U 




print("Total count of 'A':", num_of_A)
print("Total count of 'E':", num_of_E)
print("Total count of 'I':", num_of_I)
print("Total count of 'O':", num_of_O)
print("Total count of 'U':", num_of_U)
print("Total count of 'a':", num_of_a)
print("Total count of 'e':", num_of_e)
print("Total count of 'i':", num_of_i)
print("Total count of 'o':", num_of_o)
print("Total count of 'u':", num_of_u)



print(f"Total count of all vowels: {total_vowels}")