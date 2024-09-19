'''
10)


 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
Ans:
'''
# Function to find the suitable lab for 'n' students
def find_suitable_lab(x, y, z, n):
    # List to store labs that can accommodate 'n' students
    suitable_labs = []
    
    # Check each lab's capacity
    if x >= n:
        suitable_labs.append('L1')
    if y >= n:
        suitable_labs.append('L2')
    if z >= n:
        suitable_labs.append('L3')
    
    # If there are suitable labs, choose the one with maximum capacity
    if suitable_labs:
        # Get the lab with the maximum capacity from suitable labs
        lab_capacities = {'L1': x, 'L2': y, 'L3': z}
        suitable_labs.sort(key=lambda lab: lab_capacities[lab], reverse=True)  # Sort by capacity
        return suitable_labs[0]  # Return the lab with the highest capacity
    else:
        return "No suitable lab available"

# Main program
# Input values
x = int(input("Enter seating capacity of L1: "))
y = int(input("Enter seating capacity of L2: "))
z = int(input("Enter seating capacity of L3: "))
n = int(input("Enter number of students: "))

# Find the suitable lab for 'n' students
result = find_suitable_lab(x, y, z, n)

# Output the result
print(result)
