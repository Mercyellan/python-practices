# # # Example: Iterating through a list of fruits
# # fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)

# #Example: Iterating through a string

# # Example: Using range() to print numbers from 0 to 4
# # for i in range(5):
# #     print(i)
# # # Example: Using range() to print numbers from 2 to 5
# # for i in range(2, 6):
# #     print(i)
# # # Example: Using range() to print even numbers from 0 to 100
# # for i in range(0, 11, 2):
# #     print(i)

#     # Example: Using range() to print even numbers from 0 to 2000
# for i in range(0, 11, 2):
#     print(i)


# Example: Nested for loops to print coordinates
# for i in range(3):
#     for j in range(2):
#         print(f"({i}, {j})")
        
# for set_num in range(3):        # Outer loop (0, 1, 2)
#     for pushup_num in range(2): # Inner loop (0, 1)
#         print(f"Set {set_num}, Push-up {pushup_num}")



        # k=[[3,2,4],[6,1,2],[2,4,7],[8,1,5],[5,3,1]]
        # for i in k:
        #     for j in i (i):
        #         print (j)
        #         print (k[i][j])

# k=[[3,2,4],[6,1,2],[2,4,7],[8,1,5],[5,3,1]]

# for i in k:
#     for j in i:
#         print (j)


# k = [[3,2,4],[6,1,2],[2,4,7],[8,1,5],[5,3,1]]

# for row in k:          # 'row' loops through each small list
#     for item in row:   # 'item' loops through each number inside that list
#         print(item)    # This directly prints 3, then 2, then 4, etc.



        #while loops
        # Example: Printing numbers from 1 to 5 using a while loop
# count = 1



# name = "mae"
# for my in name:
#     print (my)


# for p in range(3,21,3):
#     print (p)

# else: print ("loop cannot continue")


# Outer loop tracks the hours (0, 1, 2)
for hour in range(3):
    
    # Inner loop tracks the minutes (0, 1, 2, 3)
    for minute in range(4):
        
        # This prints the current time on the screen
        print(f"Time is -> {hour}:{minute}")

