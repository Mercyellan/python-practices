# # # # # # Example: Opening a file in read mode
# # # # # file = open("my_document.txt", "r")

# # # # # # Example: Opening a file in write mode
# # # # # file = open("report.txt", "w")

# # # # # # Example: Opening a file in append mode
# # # # # file = open("application.log", "a")

# # # # # # Example: Opening a file in binary read mode
# # # # # file = open("image.jpg", "rb")



# # # # # try:
# # # # #     file = open("nonexistent_file.txt", "r")
# # # # #     # Perform operations on the file
# # # # # except FileNotFoundError:
# # # # #     print("Error: The file 'nonexistent_file.txt' was not found.")




# # # # #     file = open("my_document.txt", "r")
# # # # # # Perform operations on the file
# # # # # file.close()





# # # # # with open("my_document.txt", "r") as file:
# # # # #     # Perform operations on the file
# # # # #     content = file.read()
# # # # # # The file is automatically closed here
# # # # # print(content)





# # # # # try:
# # # # #     with open("my_document.txt", "r") as file:
# # # # #         content = file.read()
# # # # #         print(content)
# # # # # except FileNotFoundError:
# # # # #     print("Error: The file 'my_document.txt' was not found.")


# # # # # with open("report.txt", "w") as file:
# # # # #     file.write("This is a sample report.\n")
# # # # #     file.write("It contains important information.\n")


# # # # # with open("application.log", "a") as file:
# # # # #     file.write("Log entry: An event occurred.\n")



# # # # # try:
# # # # #     with open("new_file.txt", "x") as file:
# # # # #         file.write("This is a new file.\n")
# # # # # except FileExistsError:
# # # # #     print("Error: The file 'new_file.txt' already exists.")






# # # # #     #reading files line by line using loop

# # # # #     filename = "my_file.txt"

# # # # # try:
# # # # #     with open(filename, 'r') as file:
# # # # #         for line in file:
# # # # #             # Process each line
# # # # #             print(line.strip())  # Remove leading/trailing whitespace
# # # # # except FileNotFoundError:
# # # # #     print(f"Error: The file '{filename}' was not found.")
# # # # # except Exception as e:
# # # # #     print(f"An error occurred: {e}")




# # # # #Exercise 1: Word Count
# # # # def word_count(filename):
# # # #   """Counts the number of words in a file.
# # # #   Words are separated by spaces and punctuation is removed.
# # # #   """
# # # #   word_count = 0
# # # #   try:
# # # #       with open(filename, 'r') as file:
# # # #           for line in file:
# # # #               words = line.strip().split() #Remove white spaces then split sentence into words.
# # # #               word_count += len(words)
# # # #       return word_count
# # # #   except FileNotFoundError:
# # # #       return f"Error: The file '{filename}' was not found."
# # # #   except Exception as e:
# # # #       return f"An error occurred: {e}"

# # # # #Example usage of exercise 1
# # # # file_name = "my_file.txt" #You can add some content into this file to test.
# # # # word_count_result = word_count(file_name)
# # # # print(f"Total number of words in {file_name}: {word_count_result}")

# # # # #Exercise 2: Specific Line Retrieval
# # # # def get_line(filename, line_number):
# # # #     """Retrieves a specific line from a file.
# # # #     Returns an error message if the line number is out of range.
# # # #     """
# # # #     try:
# # # #         with open(filename, 'r') as file:
# # # #             for i, line in enumerate(file, 1):
# # # #                 if i == line_number:
# # # #                     return line.strip()
# # # #             return f"Error: Line {line_number} not found in the file."
# # # #     except FileNotFoundError:
# # # #         return f"Error: The file '{filename}' was not found."
# # # #     except Exception as e:
# # # #         return f"An error occurred: {e}"

# # # # #Example usage of exercise 2
# # # # file_name = "my_file.txt"
# # # # line_number_to_get = 2
# # # # line_content = get_line(file_name, line_number_to_get)
# # # # print(f"Content of line {line_number_to_get}: {line_content}")

# # # # #Exercise 3: Chunked Processing
# # # # def chunked_processing(filename, chunk_size=1024):
# # # #     """Reads a file in chunks and prints each chunk."""
# # # #     try:
# # # #         with open(filename, 'r') as file:
# # # #             while True:
# # # #                 chunk = file.read(chunk_size)
# # # #                 if not chunk:
# # # #                     break #End of file
# # # #                 print(chunk)
# # # #     except FileNotFoundError:
# # # #         print(f"Error: The file '{filename}' was not found.")
# # # #     except Exception as e:
# # # #         print(f"An error occurred: {e}")

# # # # #Example usage of exercise 3
# # # # file_name = "my_file.txt"
# # # # chunked_processing(file_name)








# # # #Writing to Files: Modes and Operations

# # # # Example: Writing to a file in 'w' mode
# # # try:
# # #     with open('my_file.txt', 'w') as file:
# # #         file.write('This is the first line.\n')
# # #         file.write('This is the second line.\n')
# # #     print("Data written to my_file.txt successfully.")
# # # except Exception as e:
# # #     print(f"An error occurred: {e}")

# # # # Verify the file content:
# # # # my_file.txt will contain:
# # # # This is the first line.
# # # # This is the second line.


# # # # Example: Appending to a file in 'a' mode
# # # try:
# # #     with open('my_file.txt', 'a') as file:
# # #         file.write('This is the third line (appended).\n')
# # #     print("Data appended to my_file.txt successfully.")
# # # except Exception as e:
# # #     print(f"An error occurred: {e}")

# # # # Verify the file content:
# # # # my_file.txt will now contain:
# # # # This is the first line.
# # # # This is the second line.
# # # # This is the third line (appended).




# # # # Example: Using 'x' mode to create a new file
# # # try:
# # #     with open('new_file.txt', 'x') as file:
# # #         file.write('This is the first line in the new file.\n')
# # #     print("new_file.txt created and data written successfully.")
# # # except FileExistsError:
# # #     print("Error: new_file.txt already exists.")
# # # except Exception as e:
# # #     print(f"An error occurred: {e}")



# # #     # Example: Writing numbers to a file
# # # try:
# # #     with open('numbers.txt', 'w') as file:
# # #         number1 = 10
# # #         number2 = 3.14
# # #         file.write(str(number1) + '\n')
# # #         file.write(str(number2) + '\n')
# # #     print("Numbers written to numbers.txt successfully.")
# # # except Exception as e:
# # #     print(f"An error occurred: {e}")

# # # # Verify the file content:
# # # # numbers.txt will contain:
# # # # 10
# # # # 3.14


# # # # Example: Writing a list to a file
# # # try:
# # #     my_list = ['apple', 'banana', 'cherry']
# # #     with open('fruits.txt', 'w') as file:
# # #         for fruit in my_list:
# # #             file.write(fruit + '\n')
# # #     print("List written to fruits.txt successfully.")
# # # except Exception as e:
# # #     print(f"An error occurred: {e}")

# # # # Verify the file content:
# # # # fruits.txt will contain:
# # # # apple
# # # # banana
# # # # cherry






# # # Example: Writing a dictionary to a file (simplified, without JSON)
# # import io


# # try:
# #     my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# #     with open('person.txt', 'w') as file:
# #         for key, value in my_dict.items():
# #             file.write(f'{key}: {value}\n')
# #     print("Dictionary written to person.txt successfully.")
# # except Exception as e:
# #     print(f"An error occurred: {e}")

# # # Verify the file content:
# # # person.txt will contain:
# # # name: Alice
# # # age: 30
# # # city: New York






# # # Example: Using 'with open()' for automatic file closing
# # try:
# #     with open('example.txt', 'w') as file:
# #         file.write('This is a line of text.')
# #     print("Data written to example.txt and file closed automatically.")
# # except Exception as e:
# #     print(f"An error occurred: {e}")





# #     # Example: Manually closing a file
# # try:
# #     file = open('example.txt', 'w')
# #     file.write('This is a line of text.')
# #     file.close()  # Manually close the file
# #     print("Data written to example.txt and file closed manually.")
# # except Exception as e:
# #     print(f"An error occurred: {e}")
# # finally:
# #  if 'file' in locals() and isinstance(file, io.IOBase) and not file.closed:
# #   file.close() # Ensure file is closed even if an error occurred








# #Examplestry:
# from dbm import error


# with open('user_input.txt', 'w') as file:
#     while True:
#         line = input("Enter a line of text (or type 'done'): ")
#         if line.lower() == 'done':
#                 break
#         file.write(line + '\n')
#     print("Data written to user_input.txt successfully.")



# # a program that reads a list of names from the user and appends them to a file named names.txt. 
# # Ensure that the file is created if it doesn't exist.


# try:
#     with open('names.txt', 'a') as file:
#         while True:
#             name = input("Enter a name (or type 'done'): ")
#             if name.lower() == 'done':
#                 break
#             file.write(name + '\n')
#     print("Names appended to names.txt successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")


#     #  a program that writes the numbers from 1 to 100 to a file named numbers.txt, 
#     # each on a new line
# try:
#      with open('numbers.txt', 'w') as file:
#         for i in range(1, 101):
#             file.write(str(i) + '\n')
#      print("Numbers written to numbers.txt successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")



#     file = None  # Initialize file outside the try block
# try:
#     file = open("my_file.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: The file was not found.")
# finally:
#     if file:
#         file.close()
#         print("File closed.")
#     else:
#         print("File was never opened.")





# Example : Reading from a File and Processing Data
# def calculate_sum_from_file(filename):
#     total = 0
#     try:
#         file = open(filename, "r")
#         for line in file:
#             try:
#                 number = float(line.strip()) # Convert each line to a float
#                 total += number
#             except ValueError:
#                 print(f"Warning: Skipping invalid data: {line.strip()}")
#         return total
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return None
#     finally:
#         if 'file' in locals() and file:  # Ensure 'file' is defined and open before closing
#             file.close()
#             print("File closed.")

# # Example usage
# filename = "numbers.txt"
# file = open(filename, "w") # Creating the numbers file
# file.write("1\n")
# file.write("2\n")
# file.write("abc\n")
# file.write("4\n")
# file.close()

# sum_of_numbers = calculate_sum_from_file(filename)

# if sum_of_numbers is not None:
#     print(f"The sum of the numbers in the file is: {sum_of_numbers}")

        

# Using with statement for Automatic Resource Management


def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Example usage
filename = "example.txt"
file = open(filename, "w") # Creating the file
file.write("Hello, world!\n")
file.close()

content = read_file_content(filename)

if content:
    print("File Content:\n", content)