#A while true block is used so that specific conditions are met before input is carried forward.
#In this case it is to ask whether they will be inputting numbers or using a text file.

while True:
    try:
        opentxt = int(input("Would you like to enter an equation or use a txt file? \nPlease type:  \n1 if you would like to input the information or \n2 if you would like to use a text file:\n"))
        if opentxt in (1, 2):
            break
        else:
            print("\n ERROR: Please enter either 1 or 2. \n")
    except ValueError:
        print("\n ERROR: Please enter either 1 or 2. \n")

#If the user wants to input their values, anoter while true block is used to get the correct input.
#User inputs two numbers and a specified operator to give out a calculation.

if opentxt == 1:
    while True:
        try:
            number1 = float(input("Please enter the first number:"))
            number2 = float(input("Please enter the second number:"))
            operation = input("Please enter the operation (+, -, /, x):")
            if number2 == 0.0 and operation == "/":
                print("\n ERROR: Cannot divide by zero")
            elif operation in ("+", "-", "/", "x"):
                break
            else:
                print("\n ERROR: Please enter one of the following: +, -, /, x. \n")
        except ValueError:
            print("\n ERROR: Please enter a valid number. \n")
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "x":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2

    equation = str(number1) + " " + operation + " " + str( number2) + " = " + str(result)
    print(equation)

#This writes or adds to a text file saved as "Eq_archive"

    with open("Eq_archive.txt", 'a') as file:
        file.write(equation)
        file.write("\n")

#If the user wants to use a text file, the code allows them to choose their text file.
#The code reads the file and uses if, elif and else to determine the operator and calculate the output for the equations.
#The code can give three different errors, this includes not being able to find the file, incorrect operator and incorrect equation. The latter two are useful if the text file includes words as well as numbers.
#Outputs are limited to 3 d.p. for a more presentable display.

if opentxt == 2:
    while True:
        try:
            filename = input("Please enter the file name:\n")
            with open(filename, 'r') as file:
            
                for line in file.readlines():
                    while True:
                        try:
                            if "+" in line:
                                sep_eq = line.partition("+")
                                result = format(float(sep_eq[0]) + float(sep_eq[2]), ".3f")
                                equation = line.split("\n")[0] + " = " + str(result)
                                print(equation)

                            elif "-" in line:
                                sep_eq = line.partition("-")
                                result = format(float(sep_eq[0]) - float(sep_eq[2]), ".3f")
                                equation = line.split("\n")[0] + " = " + str(result)
                                print(equation)

                            elif "x" in line:
                                sep_eq = line.partition("x")
                                result = format(float(sep_eq[0]) * float(sep_eq[2]), ".3f")
                                equation = line.split("\n")[0] + " = " + str(result)
                                print(equation)

                            elif "/" in line:
                                sep_eq = line.partition("/")
                                if float(sep_eq[2]) == 0.0:
                                    print(line.split("\n")[0], "ERROR: Cannot divide by 0")
                                else:
                                    result = format(float(sep_eq[0]) / float(sep_eq[2]), ".3f")
                                    equation = line.split("\n")[0] + " = " + str(result)
                                    print(equation)
                            else:
                                print(line.split("\n")[0]," ERROR: Invalid operator")
                            break
                        except ValueError:
                            print(line.split("\n")[0], " ERROR: Invalid equation")
                            break
            break
        except FileNotFoundError as error:
            print("ERROR: Invalid file name")
            print(error)
