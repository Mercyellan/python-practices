def calculate_rectangle_area(length, width):
  """
  Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  area = length * width
  return area

# Example usage
rectangle_length = 10
rectangle_width = 5
rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
print("The area of the rectangle is:", rectangle_area)  # Output: 50




def calculate_triangle_area(base, height):
  """
  Calculates the area of a triangle.

  Args:
    base: The base of the triangle.
    height: The height of the triangle.

  Returns:
    The area of the triangle.
  """
  area = (base * height) / 2
  return area

# Example usage
triangle_base = 8
triangle_height = 6
triangle_area = calculate_triangle_area(triangle_base, triangle_height)
print("The area of the triangle is:", triangle_area)  # Output: 24.0



import math

def calculate_circle_area(radius):
  """
  Calculates the area of a circle.

  Args:
    radius: The radius of the circle.

  Returns:
    The area of the circle.
  """
  area = math.pi * (radius ** 2)
  return area

# Example usage
circle_radius = 7
circle_area = calculate_circle_area(circle_radius)
print("The area of the circle is:", circle_area)  # Output: 153.93804002589985



def greet(name, greeting="Hello"): # greeting has a default value
    """Greets the person passed in as a parameter."""
    message = f"{greeting}, {name}!"
    return message

print(greet("Alice")) # Output: Hello, Alice! - uses the default greeting
print(greet("Bob", "Hi")) # Output: Hi, Bob! - overrides the default greeting




def add(x, y):
    """Adds two numbers and returns the sum."""
    return x + y

result = add(5, 3)
print(result)  # Output: 8

def no_return(x):
    """This function doesn't return anything explicitly."""
    x * 2 # this calculation happens but the value is not returned

return_value = no_return(5)
print(return_value) # Output: None





global_variable = 10  # Global scope

def my_function():
    local_variable = 5  # Local scope
    print("Inside the function:")
    print("Global variable:", global_variable)
    print("Local variable:", local_variable)

my_function()

print("Outside the function:")
print("Global variable:", global_variable)
# print("Local variable:", local_variable)  # This will cause an error, as local_variable is not accessible here