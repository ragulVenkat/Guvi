"""
Write a phthon program using Function 

1. The Function will create a text file with current Timestamp.
2. The file content should have the content of the current time Stamp.

File 'Current_date_time.txt' created with content of the current timestamp.
"""


import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create the filename using the current timestamp
    filename = f"{current_timestamp}.txt"
    
    # Write the current timestamp into the file content
    with open(filename, 'w') as file:
        file.write(f"Current Timestamp: {current_timestamp}\n")
    
    print(f"File '{filename}' created with content of the current timestamp.")

# Call the function to create the file
create_timestamp_file()
