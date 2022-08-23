# # Task 1 - Create a function that sums all integers from the start value to the end value, inclusive. ->
# # -> If the user sets the first number to be greater than the second, swap them
start = int(input('Please enter starting number -> '))
end = int(input('Please enter ending number -> '))

def sum_range_numbers(start, end):
    if start > end:
        another_starting_number = end
        end = start
        sum_start_end = sum(range(another_starting_number, end + 1))
    else:
        sum_start_end = sum(range(start, end + 1))
    return sum_start_end

print(f'Task_1 - The sum of the range of numbers is -> {sum_range_numbers(start, end)}')
#
#
# # Task 2 - Create a function that displays the number of seconds as days:hours:minutes:seconds
user_seconds = int(input('Please enter number of seconds -> '))

def time(user_seconds):
    days = user_seconds // (24 * 3600)
    user_seconds %= (24 * 3600)
    hours = user_seconds // 3600
    user_seconds %= 3600
    minutes = user_seconds // 60
    user_seconds %= 60
    seconds = user_seconds

    print(f'Task_2 - Days:Hours:Minutes:Seconds -> {days}d:{hours}h:{minutes}m:{seconds}s')

time(user_seconds)
#
#
# # Task 3.1 - Create a function that calculate the sum of the numbers in the list with a for loop
while True:
    user_list = list(input('Please enter any number -> '))

    try:
        def sum_numbers_list(user_list):
            counter = 0
            for number in user_list:
               if isinstance(number, str):
                   number = int(number)
                   counter += number
            print(f'Task_3.1 - The sum of the numbers -> {counter}')
        sum_numbers_list(user_list)
        break
    except ValueError:
        print('Please enter only numbers')

#
# # Task 3.1 - Second version!
def sum_numbers_list(list_numbers):
    result = 0
    for number in list_numbers:
        if isinstance(number, int):
            result += number
        elif isinstance(number, str):
           number = int(number)
           result += number
    return result

print(f'Task_3.1(2 version) - The sum of numbers in list -> {sum_numbers_list([45, 66, 45])}')
print(f'Task_3.1(2 version) - The sum of numbers in list -> {sum_numbers_list([45, 66,"45"])}')


# Task 3.2 - Create a function that calculate the sum of the numbers in the list with a while loop
def sum_while_cycle(numbers_list):
    result = 0
    while numbers_list:
        result += sum(numbers_list)
        break
    return result

print(f'Task_3.2 - The sum of numbers in list -> {sum_while_cycle([12, 55, 12, 776])}')