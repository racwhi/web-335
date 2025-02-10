"""
Author: Rachel White 
Date: 2/9/2025
File Name: white_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand by using lists, 
loops, and conditionals to display tasks for each day of the week.
"""

# Tasks for lemonade stand
tasks = [
    "Buy lemons",
    "Make lemonade",
    "Sell lemonade",
    "Count earnings",
    "Clean up"
]

# for loop to iterate over the list of tasks and print them
print("Tasks for running a lemonade stand:")
for task in tasks:
    print("** " + task) #add ** before each task in list

# Creating a list of days from Sunday to Saturday. \n to add a new line
days = ["Sunday", "\nMonday", "\nTuesday", "\nWednesday", "\nThursday", "\nFriday", "\nSaturday"]

# Using a for loop to iterate over the list of days
print("\nWeekly Schedule:")
for day in days:
    if day == "\nSaturday" or day == "Sunday":  # Checking if it is a weekend
        print(f"{day}: It's the weekend! Time to rest!")
    else:
        # using the day's index to map to tasks
        task_index = days.index(day)
        # Displaying the weekday along with a corresponding task
        print(f"{day}: {tasks[task_index % len(tasks)]}")