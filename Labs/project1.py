#defining calculate function for the mathmatical operatorations
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

#Defining the variables for the calculation
    number1 = int(input('Please enter the first number: '))
    number2 = int(input('Please enter the second number: '))

 #if and else if for each mathmatical operation
    if operation == '+':
        print('{} + {} = '.format(number1, number2))
        print(number1 + number2)

    elif operation == '-':
        print('{} - {} = '.format(number1, number2))
        print(number1 - number2)

    elif operation == '*':
        print('{} * {} = '.format(number1, number2))
        print(number1 * number2)

    elif operation == '/':
        print('{} / {} = '.format(number1, number2))
        print(number1 / number2)

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

#Defines the again function that restarts the script
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

#if/else if statement asking for "yes" or "no" inputs to start the script again
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Hasta La Vista Baby.')
    else:
        again()

calculate()
