'''
7)
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
Ans:
# Function to find the lab with minimal seating capacity
def find_minimum_lab(a, b, c):
    if a < b and a < c:
        return "L1"
    elif b < a and b < c:
        return "L2"
    elif c < a and c < b:
        return "L3"
    else:
        return "All labs have equal capacity"  # In case of a tie

# Main program
# Input values
a = int(input("Enter seating capacity of L1: "))
b = int(input("Enter seating capacity of L2: "))
c = int(input("Enter seating capacity of L3: "))

# Find the lab with minimal seating capacity
result = find_minimum_lab(a, b, c)

# Output the result
print(result)
