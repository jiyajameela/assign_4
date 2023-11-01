##################1

def remove_odd_numbers(input_list):
    # Use list comprehension to filter out even numbers
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Main program for testing
if __name__ == "__main__":
    # Create a list of integers
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to remove odd numbers
    result_list = remove_odd_numbers(input_list)

    # Print the original and cut-down list
    print("Original List:", input_list)
    print("Cut-down List (Even Numbers Only):", result_list)

#####################2

import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    unit_price = price / area
    return unit_price


if __name__ == "__main__":
    pizzas = []

    # Ask the user to enter details for two pizzas
    for i in range(2):
        diameter = float(input(f"Enter the diameter of pizza {i+1} (in centimeters): "))
        price = float(input(f"Enter the price of pizza {i+1} (in euros): "))
        pizzas.append([diameter, price])

    # Calculate unit prices for both pizzas
    unit_prices = [calculate_unit_price(diameter, price) for diameter, price in pizzas]

    # Determine which pizza provides better value for money
    if unit_prices[0] < unit_prices[1]:
        print("Pizza 1 provides better value for money.")
    elif unit_prices[1] < unit_prices[0]:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

##########################3
# Define seasons as strings in a tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")

# Ask the user for a number of a month
month_number = int(input("Enter a number of a month (1-12): "))

# Determine the corresponding season based on the month number
# December, January, and February are considered winter (months 12, 1, 2)
# March, April, and May are considered spring (months 3, 4, 5)
# June, July, and August are considered summer (months 6, 7, 8)
# September, October, and November are considered autumn (months 9, 10, 11)
season_index = (month_number % 12) // 3
current_season = seasons[season_index]

# Print the corresponding season
print(f"The corresponding season for month {month_number} is {current_season}.")

