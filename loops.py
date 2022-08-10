import sys

any_characters = input("Please, enter any characters -> ")

upper = ''
spaces = ''
vowels = ''
numbers = 0

for index, symbol in enumerate(any_characters):
    if symbol.isupper():
        upper += symbol

    elif symbol == ' ':
        spaces += str(index) + ', '

    elif symbol in "aeiouyAEIOUY":
        vowels += symbol

    if symbol.isdigit():
        numbers += 1
        if numbers == 3:
            print('Breaking cycle')
            break
    else:
        numbers = 0

if numbers != 3:
    print('Correct end of the cycle')
    print('Uppercase characters:', upper)
    print(f'Whitespace indexes -> {spaces}')
    print('Vowels:', vowels)

# Task 2

while True:
    number_1 = input('Please enter the first number -> ')
    if number_1 == 'exit':
        break
    try:
        number_1 = float(number_1) if "." in number_1 else int(number_1)
    except ValueError:
        print("You cannot use letters. Please use numbers")
        sys.exit(0)

    number_2 = input('Please enter the second number -> ')
    if number_2 == 'exit':
        break
    try:
        number_2 = float(number_2) if "." in number_2 else int(number_2)
    except ValueError:
        print("You cannot use letters. Please use numbers")
        sys.exit(0)

    operator = input('Please enter an action for the calculator -> ')
    if operator == 'exit':
        break

    if operator == "+":
        result = number_1 + number_2

    elif operator == "-":
        result = number_1 - number_2

    elif operator == "*":
        result = number_1 * number_2

    elif operator == "/":
        try:
            result = number_1 / number_2
            result = float(result) if number_1 % number_2 != 0 else int(result)
        except ZeroDivisionError:
            print("You can't dividing on zero")
            sys.exit(0)

    elif operator == "**":
        result = number_1 ** number_2

    else:
        print('You have entered an invalid operation character. Restart the program')
        sys.exit(0)

    print("Result ->", result)
