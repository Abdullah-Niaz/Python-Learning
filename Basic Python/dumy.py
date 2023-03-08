"""
Armstrong number detection using python

The following code majorly uses type conversion and string opeartions
of Python to determine whether the provided number is armstrong or not.
Drifting from conventional remainder calculation method, this program
is relatively easy to use and understand.
"""

def check_armstrong(number):
    string_number = str(number) # Converting the number into a string in order to iterate through it
    
    # Calculating number of digits in the number using len function
    # on string_number and converting it into integer for further
    # operations.
    power = int(len(string_number))

    # Sum variable that adds up every operation
    sum = 0

    # Using for loop to iterate through each digit and calculating
    # desired output.
    for digit in string_number:
        # We need to convert the digit into integer before performing
        # arithematic operation on it.

        sum += int(digit) ** power
    
    if sum == number:
        return f"{number} is an armstrong number"
    else:
        return f"{number} is NOT an armstrong number"
check_armstrong(234)