# Program to check voting eligibility

# Ask the user to input their age
while True:
    try:
        age = int(input("Please enter your age: "))
        break  # Exit the loop if the input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Check the age and determine eligibility to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")

