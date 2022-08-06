import sys

print('Hello. I am a simple calculator')
number_1 = input('Please enter the first number -> ')
try:
    number_1 = float(number_1) if "." in number_1 else int(number_1)
except ValueError:
    print("You cannot use letters. Please use numbers")
    sys.exit(0)

number_2 = input('Please enter the second number -> ')
try:
    number_2 = float(number_2) if "." in number_2 else int(number_2)
except ValueError:
    print("You cannot use letters. Please use numbers")
    sys.exit(0)

operator = input('Please enter an action for the calculator -> ')

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



