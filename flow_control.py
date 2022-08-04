print('Hello. I am a simple calculator')

number_1 = input('Please enter the first number -> ')
number_1 = float(number_1) if "." in number_1 else int(number_1)

number_2 = input('Please enter the second number -> ')
number_2 = float(number_2) if "." in number_2 else int(number_2)

operator = input('Please enter an action for the calculator -> ')

if operator == "+":
    sum_numbers = number_1 + number_2
    print(f"{number_1} + {number_2} =", sum_numbers)

elif operator == "-":
    number_subtraction = number_1 - number_2
    print(f"{number_1} - {number_2} =", number_subtraction)

elif operator == "*":
    multiplic_numbers = number_1 * number_2
    print(f"{number_1} * {number_2} =", multiplic_numbers)

elif operator == "/":
    try:
        result = number_1 / number_2
        result = float(result) if number_1 % number_2 != 0 else int(result)
        print(f"{number_1} / {number_2} =", result)
    except ZeroDivisionError:
        print("You can't dividing on zero")

elif operator == "**":
    power_number = number_1 ** number_2
    print(f"{number_1} ** {number_2} =", power_number)

else:
    print('You have entered an invalid operation character. Restart the program')









