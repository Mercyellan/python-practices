# # # Example: Searching for a specific number in a list
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # target = 5

# # for number in numbers:
# #     print(f"Checking number: {number}")
# #     if number == target:
# #         print(f"Found the target: {target}")
# #         break  # Exit the loop when the target is found
# #     else:
# #         print(f"{number} is not the target.")

# # print("Loop finished.")



# # Example: Breaking out of an inner loop
# for i in range(3):
#     print(f"Outer loop iteration: {i}")
#     for j in range(5):
#         print(f"  Inner loop iteration: {j}")
#         if j == 2:
#             print("  Breaking out of the inner loop")
#             break  # Breaks only the inner loop
#     print("Outer loop continues")

# print("Program finished.")



# Example: Printing only odd numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     if number % 2 == 0:  # Check if the number is even
#         continue  # Skip the rest of the iteration if the number is even
#     print(f"Odd number: {number}")

# print("Loop finished.")





# # Example: Using continue in nested loops
# for i in range(3):
#     print(f"Outer loop iteration: {i}")
#     for j in range(5):
#         if j == 2:
#             print("  Skipping inner loop iteration 2")
#             continue  # Skips the rest of the inner loop iteration
#         print(f"  Inner loop iteration: {j}")
#     print("Outer loop continues")

# print("Program finished.")








# Example: Using continue in a while loop
# count = 0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         print(f"Skipping even number: {count}")
#         continue  # Skip even numbers
#     print(f"Odd number: {count}")

# print("Loop finished.")







# Example: Validating user input
# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")

#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'

#     try:
#         number = float(user_input)  # Convert the input to a float
#         print(f"You entered: {number}")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         continue  # Skip to the next iteration if the input is not a number



# Example: Filtering data
# data = [10, -5, 20, -2, 0, 15, -8, 5]

# for value in data:
#     if value <= 0:
#         continue  # Skip non-positive values
#     print(f"Processing positive value: {value}")




# Example: Finding the first prime number
def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in range(2, 20):  # Check numbers from 2 to 19
    if is_prime(number):
        print(f"The first prime number found is: {number}")
        break  # Exit the loop after finding the first prime number