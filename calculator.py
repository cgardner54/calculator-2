"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
"""
have 3 parameters as inputs 
    operand
    num1
    num2

tokenize based on spaces ' '
if it's just one parameter "q" it quits the program

after we split it we write our functions for each of the conditional statements.
"""

while True:
        
    initial_string = input("Enter prefix calculation: ")

    def calculate(initial_string):
        if initial_string == "q":
            exit()

        else:
            split_string = initial_string.split(" ")
        
            num1 = int(split_string[1])
            num2 = 0

            if len(split_string) > 2:
                num2 = int(split_string[2]) 

            #consideration to make dictionary for operands 
            """(add, subtract, multiply, divide, square, cube,
                            power, mod, )
                            """
            if split_string[0] == '+':
                print(add(num1, num2))

            elif split_string[0] == '-':
                print(subtract(num1, num2))

            elif split_string[0] == '*':
                print(multiply(num1, num2))

            elif split_string[0] == '/':
                print(divide(num1, num2))

            elif split_string[0] == 'square':
                print(square(num1))

            elif split_string[0] == 'cube':
                print(cube(num1))

            elif split_string[0] == 'pow':
                print(pow(num1, num2))

            elif split_string[0] == 'mod':
                print(mod(int(num1), int(num2)))

    calculate(initial_string)