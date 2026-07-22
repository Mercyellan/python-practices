# # # Creating a list of integers
# # integer_list = [1, 2, 3, 4, 5]
# # print(integer_list)  # Output: [1, 2, 3, 4, 5]

# # # Creating a list of strings
# # string_list = ["apple", "banana", "cherry"]
# # print(string_list)  # Output: ['apple', 'banana', 'cherry']

# # # Creating a list with mixed data types
# # mixed_list = [1, "hello", 3.14, True]
# # print(mixed_list)  # Output: [1, 'hello', 3.14, True]

# # # Creating a nested list (list of lists)
# # nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(nested_list)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# # # Creating a list from a string
# # string = "Python"
# # list_from_string = list(string)
# # print(list_from_string)  # Output: ['P', 'y', 't', 'h', 'o', 'n']

# # # Creating a list from a tuple
# # tuple_example = (1, 2, 3)
# # list_from_tuple = list(tuple_example)
# # print(list_from_tuple)  # Output: [1, 2, 3]


# # my_list = ["apple", "banana", "cherry", "date"]

# # # Accessing the first element (index 0)
# # first_element = my_list[0]
# # print(first_element)  # Output: apple

# # # Accessing the third element (index 2)
# # third_element = my_list[2]
# # print(third_element)  # Output: cherry




# # my_list = ["apple", "banana", "cherry", "date"]

# # # Accessing the last element (index -1)
# # last_element = my_list[-1]
# # print(last_element)  # Output: date

# # # Accessing the second-to-last element (index -2)
# # second_last_element = my_list[-2]
# # print(second_last_element)  # Output: cherry






# # my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# # # Slicing from index 1 to 3 (exclusive)
# # slice_1 = my_list[1:3]
# # print(slice_1)  # Output: ['banana', 'cherry']

# # # Slicing from the beginning to index 4 (exclusive)
# # slice_2 = my_list[:4]
# # print(slice_2)  # Output: ['apple', 'banana', 'cherry', 'date']

# # # Slicing from index 2 to the end
# # slice_3 = my_list[2:]
# # print(slice_3)  # Output: ['cherry', 'date', 'elderberry']

# # # Slicing with a step of 2
# # slice_4 = my_list[0:5:2]
# # print(slice_4)  # Output: ['apple', 'cherry', 'elderberry']

# # # Slicing the entire list (creating a copy)
# # slice_5 = my_list[:]
# # print(slice_5)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# # # Slicing with a negative step to reverse the list
# # slice_6 = my_list[::-1]
# # print(slice_6) # Output: ['elderberry', 'date', 'cherry', 'banana', 'apple']








# # nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # # Accessing the first element of the first sublist
# # element_1 = nested_list[0][0]
# # print(element_1)  # Output: 1

# # # Accessing the second element of the second sublist
# # element_2 = nested_list[1][1]
# # print(element_2)  # Output: 5

# # # Accessing the third element of the third sublist
# # element_3 = nested_list[2][2]
# # print(element_3)  # Output: 9




# # my_list = ["apple", "banana", "cherry"]

# # # Adding an element to the end of the list
# # my_list.append("date")
# # print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date']




# # my_list = ["apple", "banana", "cherry"]

# # # Extending the list with another list
# # my_list.extend(["date", "elderberry"])
# # print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# # # Extending the list with a string (treated as an iterable of characters)
# # my_list.extend("fig")
# # print(my_list)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'f', 'i', 'g']





# # my_list = ["apple", "banana", "cherry", "banana"]

# # # Removing the first occurrence of "banana"
# # my_list.remove("banana")
# # print(my_list)  # Output: ['apple', 'cherry', 'banana']






# # my_list = ["apple", "banana", "cherry"]

# # # Removing the element at index 1
# # removed_element = my_list.pop(1)
# # print(my_list)  # Output: ['apple', 'cherry']
# # print(removed_element)  # Output: banana

# # # Removing the last element
# # removed_element = my_list.pop()
# # print(my_list)  # Output: ['apple']
# # print(removed_element)  # Output: cherry





# # my_list = ["apple", "banana", "cherry", "date"]

# # # Deleting the element at index 1
# # del my_list[1]
# # print(my_list)  # Output: ['apple', 'cherry', 'date']

# # # Deleting a slice of the list
# # del my_list[1:3]
# # print(my_list)  # Output: ['apple']

# # # Deleting the entire list
# # del my_list
# # # print(my_list)  # This will raise a NameError because the list no longer exists




# # numbers = [1, 2, 3, 4, 5]

# # # Creating a new list with each number squared
# # squared_numbers = [x**2 for x in numbers]
# # print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# # # Creating a new list with only the even numbers
# # even_numbers = [x for x in numbers if x % 2 == 0]
# # print(even_numbers)  # Output: [2, 4]

# # # Creating a new list with strings converted to uppercase
# # words = ["hello", "world"]
# # uppercase_words = [word.upper() for word in words]
# # print(uppercase_words) # Output: ['HELLO', 'WORLD']




# #Deleting a slice of the list
# my_list = ["apple", "banana", "cherry", "date"]

# del my_list[0:3]
# print(my_list)  













