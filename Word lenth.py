def count_words(input_string):
    input_string = input_string.strip()
    
    words = input_string.split()
    
    return len(words)

input_string = "Hello, how are you?"
num_words = count_words(input_string)
print(f"The number of words in '{input_string}' is: {num_words}")
