'''
6)
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
Ans:
'''
# Function to calculate age
def calculate_age(birth_year, current_year):
    # Calculate age based on the years
    if current_year >= birth_year:
        age = current_year - birth_year
    else:
        age = (100 + current_year) - birth_year  # Considering the century change
    return age

# Main program
# Input values
birth_year = int(input("Enter the last 2 digits of your birth year: "))
current_year = int(input("Enter the last 2 digits of the current year: "))

# Calculate age
age = calculate_age(birth_year, current_year)

# Output the result
print(age)
