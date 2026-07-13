# # #working with date and time 

# # # Using 'import'
# # import datetime

# # today = datetime.date.today()
# # print("Today's date:", today)


# # # Using 'from ... import'
# # from datetime import datetime, timedelta

# # now = datetime.now()
# # print("Current date and time:", now)

# # future_date = now + timedelta(days=7)
# # print("Date in one week:", future_date)

# # # Using 'as'
# # import datetime as dt

# # current_time = dt.datetime.now()
# # print("Current time:", current_time)



# #geneating random numbers 

# # Using 'import'
# # import random

# # random_number = random.randint(1, 100)
# # print("Random number between 1 and 100:", random_number)

# # # Using 'from ... import'
# # from random import random

# # random_float = random()  # Generates a float between 0.0 and 1.0
# # print("Random float:", random_float)

# # # Using 'as'
# # import random as rnd

# # lottery_number = rnd.randint(1, 60)
# # print("Lottery number:", lottery_number)





# #performing mathematical operations
# # Using 'import'
# import math

# area = math.pi * (5**2)
# print("Area of a circle with radius 5:", area)

# # Using 'from ... import'
# from math import ceil, floor

# number = 4.3

# print("Ceiling of", number, ":", ceil(number))  # Round up
# print("Floor of", number, ":", floor(number))  # Round down

# # Using 'as'
# import math as m

# power_of_two = m.pow(2, 8)  # 2 raised to the power of 8
# print("2 to the power of 8:", power_of_two)







import datetime

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = datetime.date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"Age: {age}") # Output: Age: 33 (example)