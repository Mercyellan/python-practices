# def greet(name):
#   """This function greets the person passed in as a parameter."""
#   print(f"Hello, {name}!")

# # Calling the function with an argument
# greet("Alice")  # Output: Hello, Alice!
# greet("Bob")    # Output: Hello, Bob!


# #multiple parameters
# def describe_person(name, age, city):
#   """This function describes a person based on their name, age, and city."""
#   print(f"{name} is {age} years old and lives in {city}.")

# # Calling the function with multiple arguments
# describe_person("Charlie", 30, "New York") # Output: Charlie is 30 years old and lives in New York.
# describe_person("Diana", 25, "London")   # Output: Diana is 25 years old



# def power(base, exponent=2):
#   """This function calculates the power of a number.
#   If no exponent is provided, it defaults to 2 (square)."""
#   result = base ** exponent
#   return result

# # Calling the function with one argument (using the default exponent)
# square = power(5)  # base=5, exponent=2 (default)
# print(square)       # Output: 25

# # Calling the function with two arguments (overriding the default exponent)
# cube = power(5, 3)  # base=5, exponent=3
# print(cube)         # Output: 125 and lives in London.





def power(base, exponent=2):
  """This function calculates the power of a number.
  If no exponent is provided, it defaults to 2 (square)."""
  result = base ** exponent
  return result

# Calling the function with one argument (using the default exponent)
square = power(5)  # base=5, exponent=2 (default)
print(square)       # Output: 25

# Calling the function with two arguments (overriding the default exponent)
cube = power(5, 3)  # base=5, exponent=3
print(cube)         # Output: 125






def greet(name):
  """This function greets the person passed in as a parameter."""
  print(f"Hello, {name}!")

# Calling the function with the argument "Alice"
greet("Alice")  # Output: Hello, Alice!

# Calling the function with the argument "Bob"
greet("Bob")  # Output: Hello, Bob!
