"""
Write a phthon program using Function  to read from a text file. The function will take the name of the text file and display the content of the file into the console
"""


def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Content of the file '{filename}':\n")
            line = file.readline()
            while line:
                print(line, end='')  # end='' prevents adding extra new lines
                line = file.readline()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_to_read = input("Enter the name of the text file to read: ")
read_file_content(file_to_read)
