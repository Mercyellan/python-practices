# #age =20
# if age >= 18:
#     print("You are eligible to vote.")

#     temperature = 5
#     if temperature < 6:
#         print("it is a very cold day.")

#         #elif statement
#         score = 75
#         if score >= 90:
#             print("Excellent")
#         elif score >= 70:
#             print("Good job")
        # elif score >= 50:
        #     print("You passed")
        # else:
        #     print("you failed")

            #'''more example'''
# username = input("Enter your username: ")
# if username == "":
#     print("Username cannot be empty.")
# else:
#     print("Username is valid.")



# password = input("Enter your password: ")
# if len(password) < 8:
#     print("Password must be at least 8 characters long.")
# else:
#     print("Password is valid.")


    #Age checker example
# age = 13
# if age <= 13:
#     print("You are a child.")
# elif age > 13 and age < 19:
#     print("You are a teenager.")
# else:    print("You are an adult.")


#Grade checker example
score = float(input("Enter test score from 0-100: "))

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 45:
    grade = "E"

else:
    grade = "F"

print(f"Your grade is: {grade}")