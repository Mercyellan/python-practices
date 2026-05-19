# Assigning a boolean to a variable
is_active = True
is_valid = False

print(is_active) 
print(is_valid)  

# Setup variables
has_homework_done = True
has_room_cleaned = False

# AND example (Both must be True)
print(has_homework_done and has_room_cleaned)  
# Output: False (because the room is not cleaned)


# OR example (Only one needs to be True)
print(has_homework_done or has_room_cleaned)   
# Output: True (because homework is done)

# NOT example (Flips the value)
print(not has_homework_done)                    
# Output: False




#more examples 
my_age = 20
driving_age = 18

# Python answers with True or False
can_drive = (my_age >= driving_age)  
print(can_drive)  
# Output: True

print(10 == 5)  



# Testing numbers
print(bool(100))  # Output: True  (It is a number that is not 0)
print(bool(0))    # Output: False (Zero counts as empty/False)

# Testing text strings
print(bool("Pizza")) # Output: True  (The string has letters)
print(bool(""))      # Output: False (The string is empty)

