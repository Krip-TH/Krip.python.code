"""
Week 1 Lab - Additional Practice Exercises
Complete these exercises to reinforce your learning.
"""

# Exercise 1: Personal Profile Creator
print("=== Personal Profile Creator ===")
# Create a program that asks for:
# - Full name
# - Age
# - Email
# - Phone number
# - Favorite hobby
# Then display it as a profile

# Write your solution here:
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
hobby = input("Enter your favorite hobby: ")

print("\n--- Personal Profile ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Favorite Hobby: {hobby}")

# Exercise 2: Shopping Receipt
print("\n=== Shopping Receipt ===")
# Ask the user for:
# - Item name
# - Item price
# - Quantity
# Calculate and display the total cost

# Write your solution here:
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total_cost = item_price * quantity

print("\n--- Shopping Receipt ---")
print(f"Item: {item_name}")
print(f"Price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Cost: ${total_cost:.2f}")


# Exercise 3: Student Grade Calculator
print("\n=== Student Grade Calculator ===")
# Ask for three test scores and calculate the average
# Display each score and the average

# Write your solution here:
score1 = float(input("Enter first test score: "))
score2 = float(input("Enter second test score: "))
score3 = float(input("Enter third test score: "))
average = (score1 + score2 + score3) / 3

print("\n--- Student Grades ---")
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print(f"Average: {average:.2f}")


# Exercise 4: Time Converter
print("\n=== Time Converter ===")
# Ask user for a number of minutes
# Convert and display as hours and minutes
# Example: 150 minutes = 2 hours and 30 minutes

# Write your solution here:
minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")


# Exercise 5: Circle Calculator
print("\n=== Circle Calculator ===")
# Ask for the radius of a circle
# Calculate and display:
# - Diameter (2 * radius)
# - Circumference (2 * pi * radius)
# - Area (pi * radius^2)
# Use 3.14159 for pi

# Write your solution here:
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2

print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Area: {area}")


# Exercise 6: String Manipulator
print("\n=== String Manipulator ===")
# Ask user for a sentence
# Display:
# - The sentence in uppercase
# - The sentence in lowercase
# - The number of characters
# - The number of words (hint: count spaces + 1)

# Write your solution here:
sentence = input("Enter a sentence: ")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Number of characters: {len(sentence)}")
print(f"Number of words: {len(sentence.split())}")


# Exercise 7: Password Strength Checker (Basic)
print("\n=== Password Strength Checker ===")
# Ask user for a password
# Display:
# - Length of password
# - Whether it's longer than 8 characters
# - First and last character

# Write your solution here:
password = input("Enter a password: ")
length = len(password)
is_strong = length > 8
first_char = password[0] if length > 0 else ""
last_char = password[-1] if length > 0 else ""

print(f"Length of password: {length}")
print(f"Longer than 8 characters: {'Yes' if is_strong else 'No'}")
print(f"First character: {first_char}")
print(f"Last character: {last_char}")


# Exercise 8: Distance Calculator
print("\n=== Distance Calculator ===")
# Ask for speed (miles per hour) and time (hours)
# Calculate and display the distance traveled
# Formula: distance = speed × time

# Write your solution here:
speed = float(input("Enter speed (miles per hour): "))
time = float(input("Enter time (hours): "))
distance = speed * time

print(f"Distance traveled: {distance} miles")


# Exercise 9: Age in Days
print("\n=== Age in Days Calculator ===")
# Ask for user's age in years
# Calculate and display their age in:
# - Days (approximately, use 365 days per year)
# - Hours
# - Minutes

# Write your solution here:
age_years = int(input("Enter your age in years: "))
age_days = age_years * 365
age_hours = age_days * 24
age_minutes = age_hours * 60

print(f"Age in days: {age_days}")
print(f"Age in hours: {age_hours}")
print(f"Age in minutes: {age_minutes}")


# Exercise 10: Bill Splitter
print("\n=== Bill Splitter ===")
# Ask for:
# - Total bill amount
# - Number of people
# - Tip percentage
# Calculate and display:
# - Tip amount
# - Total with tip
# - Amount per person

# Write your solution here:
bill_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
tip_amount = bill_amount * (tip_percent / 100)
total_with_tip = bill_amount + tip_amount
amount_per_person = total_with_tip / num_people

print("\n--- Bill Splitter ---")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total with Tip: ${total_with_tip:.2f}")
print(f"Amount per Person: ${amount_per_person:.2f}")


# Bonus Challenge: Mad Libs Game
print("\n=== Mad Libs Game ===")
# Write your solution here:
# Ask user for various words (noun, verb, adjective, etc.)
# Use them to create a funny story
# Example: "The [adjective] [noun] [verb] over the [noun]"

noun1 = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
noun2 = input("Enter another noun: ")

story = f"The {adjective} {noun1} {verb} over the {noun2}."
print("\n--- Mad Libs Story ---")
print(story)









