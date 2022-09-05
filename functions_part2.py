# Task 3_3 -> Create a function that calculates the sum of the numbers in a list using recursion
user_list = [2, 56, 13, 45, 23]


def sum_numbers_list(any_list):
    if len(any_list) == 0:
        return 0
    else:
        return any_list[0] + sum_numbers_list(any_list[1:])


print(sum_numbers_list(user_list))


# Task_4 -> Create a function that calculates Fibonacci numbers.
# # The function accepts the serial number of the sequence number.
def fibonacci_numbers(number):
    if number <= 0:
        print("Please enter only positive integers")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci_numbers(number - 1) + fibonacci_numbers(number - 2)


try:
    user_number = int(input("Please enter any integer -> "))

    print(f'Fibonacci number №{user_number} -> {fibonacci_numbers(user_number)}')

except ValueError:
    print('Please enter only integers')

# Task_5 -> Print 4 lines: tomato -> meat -> cheese -> bread, conditions:
# 1) Create 4 functions, each printing its own layer
# 2) Call only one function
# 3) Use decorator syntax


def tomato(function):
    print('tomato')
    return function


def meat(function):
    print('meat')
    return function


def cheese(function):
    print('cheese')
    return function


def bread(function):
    print('bread')
    return function


@bread
@cheese
@meat
@tomato
def ingredients():
    return None
