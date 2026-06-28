# Example: An infinite loop (avoid this!)
# p = 2 
# while p > 0:
#     print("This will not print forever!")


x = 5
while x > 3:
    print("This will print only once!")
    x = 2 # Now x is 2, so 'x > 0' becomes False, and the loop stops!
