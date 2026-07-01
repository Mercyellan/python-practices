# Basic concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2  
print(result)  


# Concatenating with variables of different data types (requires type conversion)
name = "Alice"
age = 30
# TypeError: can only concatenate str (not "int") to str
# message = "My name is " + name + " and I am " + age # This will cause an error
message = "My name is " + name + " and I am " + str(age) # Convert int to string
print(message)  


# Example: Appending to a string
greeting = "Hello"
greeting += " "  # Append a space
greeting += "there!" # Append "there!"
print(greeting)  # Output: Hello there!


# Example: Using join() to concatenate a list of strings
words = ["This", "is", "a", "sentence."]
sentence = " ".join(words)  # Join the words with a space in between
print(sentence)  # Output: This is a sentence.

# Example: Using join() with an empty string as a separator
characters = ['P', 'y', 't', 'h', 'o', 'n']
word = "".join(characters)
print(word) # Output: Python


#string slicing
# Example 1: Slicing with start and end indices
text = "Python is fun!"
substring = text[0:6]  # Extract characters from index 0 up to (but not including) index 6
print(substring)  # Output: Python

# Example 2: Slicing with only the start index
substring = text[7:]  # Extract characters from index 7 to the end of the string
print(substring)  # Output: is fun!

# Example 3: Slicing with only the end index
substring = text[:6]  # Extract characters from the beginning of the string up to (but not including) index 6
print(substring)  # Output: Python

# Example 4: Slicing with a step
substring = text[0:13:2]  # Extract every second character from index 0 to 12
print(substring) # Output: Pto sfn

# Example 5: Slicing with a negative step (reversing the string)
reversed_text = text[::-1]  # Reverse the entire string
print(reversed_text)  # Output: !nuf si nohtyP

#nagative indeces
# Example: Using negative indices
text = "Python"
last_character = text[-1]  # Access the last character
print(last_character)  # Output: n

second_last = text[-2] # Access the second to last character
print(second_last) # Output: o

# Example: Slicing with negative indices
substring = text[-3:]  # Extract the last three characters
print(substring)  # Output: hon

substring = text[:-3] # Extract everything up to the last three characters
print(substring) # Output: Pyt


#string formatting
# Example 1: Basic f-string formatting
name = "Bob"
age = 40
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Bob and I am 40 years old.

# Example 2: F-strings with expressions
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)  # Output: The sum of 10 and 5 is 15.

# Example 3: F-strings with formatting specifications
pi = 3.14159265359
formatted_pi = f"The value of pi is approximately {pi:.2f}"  # Format to 2 decimal places
print(formatted_pi)  # Output: The value of pi is approximately 3.14





#The .format() Method (Legacy)
name = "Alex"
score = 0.95
print("{} got {:.0%}".format(name, score))
