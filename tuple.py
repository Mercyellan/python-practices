# Creating a tuple of integers
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Creating a tuple of mixed data types
mixed_tuple = (1, "hello", 3.4, True)
print(mixed_tuple)  # Output: (1, 'hello', 3.4, True)




# Creating an empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()


my_tuple = (10, 20, 30, 40, 50)

# Accessing elements by index
print(my_tuple[0])  # Output: 10
print(my_tuple[3])  # Output: 40

# Negative indexing (accessing from the end)
print(my_tuple[-1]) # Output: 50
print(my_tuple[-2]) # Output: 40

# Slicing tuples
print(my_tuple[1:4]) # Output: (20, 30, 40)
print(my_tuple[:3])  # Output: (10, 20, 30)
print(my_tuple[3:])  # Output: (40, 5