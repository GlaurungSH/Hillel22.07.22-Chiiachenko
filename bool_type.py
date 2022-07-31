# Fix the error in comparison 3 ! 5

equation = 3 != 5
print("3 != 5 =", equation)


# List all combinations of comparisons for 5 _ 5 in which the result will be True

number_5 = 5
number2_5 = 5

number5_and_2number5 = bool(5 and 5)
print("5 and 5 =", number5_and_2number5)

number5_or_2number5 = bool(5 or 5)
print("5 or 5 =", number5_or_2number5)

number5_equals_2number5 = bool(5 == 5)
print("5 = 5 ->", number5_equals_2number5)

print("5 is 5 =", number_5 is number2_5)


# List 5 combinations of logical operators (or, and, not) and parentheses so that the result in the expression
# True _ True _ False is True

example_1 = True and True or False
example_2 = not True and True or not False
example_3 = True and (True or False)
example_4 = not True and not True or not False
example_5 = not ((True and not True) or False)

print("True and True or False =", example_1)
print("not True and True or not False =", example_2)
print("True and (True or False) =", example_3)
print("not True and not True or not False =", example_4)
print("not ((True and not True) or False) =", example_5)


# Compare the logical values None and 7

variable_none = None
variable_7 = 7
none_and_7 = bool(None and 7)
none_or_7 = bool(None or 7)

print("None and 7 =", none_and_7)
print("None or 7 =", none_or_7)
print("None is 7 = ", variable_none is variable_7)


# Compare the logical values of the empty string and the expression 10 - 1

empty_string = ""
expression = 10 - 1
empty_str_and_expression = bool("" and 10 - 1)
empty_str_or_expression = bool("" or 10 - 1)

print('"" and 10 - 1 ->', empty_str_and_expression)
print('"" or 10 - 1 ->', empty_str_or_expression)
print('"" is (10 - 1) -> ', empty_string is expression)

