def read_and_modify_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (example: add a line)
        modified_content = content + "\nThis line was added."

        with open('modified_' + filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"File '{filename}' modified successfully.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading or writing file: {e}")

# Get filename from user
filename = input("Enter the filename: ")

# Call the function to read, modify, and write the file
read_and_modify_file(filename)