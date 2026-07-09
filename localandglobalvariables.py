discount_rate = 0.1  # Global variable for discount rate

def calculate_price(price, quantity):
    """Calculates the total price after applying a discount."""
    global discount_rate # Use the global variable

    # Apply discount
    discount = price * discount_rate
    final_price = (price - discount) * quantity
    return final_price

# Example usage
price = 100
quantity = 5
total_price = calculate_price(price, quantity)
print("Total price:", total_price) # Output: 450.0



def counter():
    count = 0 # This is enclosed in counter

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# Create an instance of the counter
my_counter = counter()

# Call the increment function multiple times
print(my_counter()) # Output: 1
print(my_counter()) # Output: 2
print(my_counter()) # Output: 3