# Creating a set of integers
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set of strings
string_set = {"apple", "banana", "cherry"}
print(string_set)  # Output: {'apple', 'banana', 'cherry'} (order may vary)


# Creating a set from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

# Creating an empty set (important: {} creates an empty dictionary, not a set)
empty_set = set()
print(empty_set)  # Output: set()



my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.update((7, 8))
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

my_set.update({9, 10})
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}





# Creating a set of squares of numbers from 1 to 5
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}

# Creating a set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {x for x in numbers if x % 2 == 0}
print(even_numbers)  # Output: {2, 4, 6, 8, 10}




def unique_characters(text):
    """
    Returns a set of unique characters in the given string.
    """
    return set(text)

print(unique_characters("hello"))  # Expected output: {'h', 'e', 'l', 'o'}
print(unique_characters("programming"))  # Expected output: {'g', 'm', 'i', 'r', 'o', 'n', 'p', 'a'}



list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common_elements = list(set1.intersection(set2))
print(common_elements)  # Output: [3, 5]