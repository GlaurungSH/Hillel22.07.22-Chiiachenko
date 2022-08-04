print('Hello. I am a simple calculator')

number_1 = input('Please enter the first number -> ')
if "." in number_1:
    number_1 = float(number_1)
else:
    number_1 = int(number_1)

number_2 = input('Please enter the second number -> ')
if "." in number_2:
    number_2 = float(number_2)
else:
    number_2 = int(number_2)

operator = input('Please enter an action for the calculator -> ')

if operator == "+":
        print(f"{number_1} + {number_2} =", number_1 + number_2)

elif operator == "-":
    print(f"{number_1} - {number_2} =", number_1 - number_2)

elif operator == "*":
    print(f"{number_1} * {number_2} =", number_1 * number_2)

elif operator == "/":
    try:
        result = number_1 / number_2
        if number_1 % number_2 != 0:
            result = float(result)
        else:
            result = int(result)
        print(f"{number_1} / {number_2} =", result)
    except ZeroDivisionError:
        print("You can't dividing on zero")

elif operator == "**":
    print(f"{number_1} ** {number_2} =", number_1 ** number_2)

else:
    print('You have entered an invalid operation character. Restart the program')









