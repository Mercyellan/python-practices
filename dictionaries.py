# Creating a dictionary using curly braces
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Creating a dictionary using the dict() constructor with keyword arguments
student_2 = dict(name="Bob", age=22, major="Engineering")

# Creating a dictionary using the dict() constructor with a list of tuples
student_3 = dict([("name", "Charlie"), ("age", 19), ("major", "Mathematics")])

print(student)
print(student_2)
print(student_3)




student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20



student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(student.get("name"))       # Output: Alice
print(student.get("city"))       # Output: None
print(student.get("city", "Unknown")) # Output: Unknown



student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

print(student.get("name"))       # Output: Alice
print(student.get("city"))       # Output: None
print(student.get("city", "Unknown")) # Output: Unknown




student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Getting keys
keys = student.keys()
print(keys) # Output: dict_keys(['name', 'age', 'major'])

# Getting values
values = student.values()
print(values) # Output: dict_values(['Alice', 20, 'Computer Science'])

# Getting items
items = student.items()
print(items) # Output: dict_items([('name', 'Alice'), ('age', 20), ('major', 'Computer Science')])

# Updating the dictionary
student.update({"city": "New York", "gpa": 3.8})
print(student) # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'city': 'New York', 'gpa': 3.8}

# Popping an item
age = student.pop("age")
print(student) # Output: {'name': 'Alice', 'major': 'Computer Science', 'city': 'New York', 'gpa': 3.8}
print(age)     # Output: 20

# Clearing the dictionary
student.clear()
print(student) # Output: {}



user_profile = {
    "username": "johndoe",
    "email": "john.doe@example.com",
    "age": 30,
    "city": "San Francisco"
}

print(f"Username: {user_profile['username']}")
print(f"Email: {user_profile['email']}")


def word_frequency(text):
    """
    Calculates the frequency of each word in a string.

    Args:
        text: The input string.

    Returns:
        A dictionary where keys are words and values are their frequencies.
    """
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace()) # Remove punctuation
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = "This is a test string. This string is a test."
print(word_frequency(text))
# Expected output: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'string': 2}



def get_job_title(company_structure, employee_id):
    """
    Retrieves the job title of an employee from a nested dictionary.

    Args:
        company_structure: A nested dictionary representing the company's organizational structure.
        employee_id: The ID of the employee.

    Returns:
        The job title of the employee, or None if the employee is not found.
    """
    for department, employees in company_structure.items():
        if employee_id in employees:
            return employees[employee_id]
    return None

company = {
    "Engineering": {
        101: "Software Engineer",
        102: "Data Scientist"
    },
    "Marketing": {
        201: "Marketing Manager",
        202: "Social Media Specialist"
    }
}

print(get_job_title(company, 101))  # Output: Software Engineer
print(get_job_title(company, 202))  # Output: Social Media Specialist
print(get_job_title(company, 301))  # Output: None
