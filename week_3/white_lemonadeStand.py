"""
Title: white_lemonadeStand.py
Author: Rachel White
Date: 1/26/2025
Description: Lemonade Stand Python program
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):

    total_cost = lemons_cost + sugar_cost  # Calculate the total cost
    return total_cost  # Return the total cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
 
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Calculate the total cost
    profit = selling_price - total_cost  # Calculate the profit
    return profit  # Return the profit

# Variables to test each function
lemons_cost =4.99 # Example cost of lemons in dollars
sugar_cost = 2.5   # Example cost of sugar in dollars
selling_price = 8.5 # Example selling price in dollars

# Prepare a string for the results
cost = calculate_cost(lemons_cost, sugar_cost)
result_string = f"{cost}"

#  Profit calculation
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Concatenating results into an output variable
output = f"Total Cost of making lemonade:${result_string}\nSelling price:  ${selling_price:.2f}\nProfit Selling lemonade: ${profit:.2f}"

# Print the output to the console
print(output)

