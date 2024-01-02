import datetime

print("This is a program to greet")

# Ask user to input their name
user_name = input("Enter your name: ")

# Input from the user
user_input = input("Enter something you like: ")

# Input your date of birth
date_of_birth_str = input("Enter your date of birth (DD-MM-YYYY): ")

# Convert the date of birth string to a datetime object
date_of_birth = datetime.datetime.strptime(date_of_birth_str, "%d-%m-%Y")

# Calculate user age and how many days of life it has
today_date = datetime.datetime.now()
age = today_date.year - date_of_birth.year - ((today_date.month, today_date.day) < (date_of_birth.month, date_of_birth.day))
days_of_life = (today_date - date_of_birth).days

# Print out user name
print("Hello,", user_name + "!")

# Print out the inputted data
print("Good to know that you like:", user_input + ".")

# Print the age inputted
print(f"Your age is: {age} and you have lived for {days_of_life} days.")
