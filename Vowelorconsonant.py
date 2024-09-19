'''
2)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
Ans:
'''
# Get a character from the user
char = input("Enter a character: ")

# Check if the input is a single alphabet character
if len(char) != 1 or not char.isalpha():
    print("Not an alphabet")
else:
    # Check if the character is a vowel
    if char.lower() in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
