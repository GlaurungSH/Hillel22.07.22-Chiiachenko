# Task 1

first_user_text = set(input('Please enter any text -> '))
second_user_text = set(input('Please re-enter any text -> '))

elements_in_two_sets = first_user_text & second_user_text
unique_elements = first_user_text ^ second_user_text
only_letters_in_sets = {element for element in elements_in_two_sets if element.isalpha()}
unique_numbers_in_sets = {element for element in unique_elements if element.isdigit()}

print(f'List of letters that are present in both sets -> {only_letters_in_sets}')
print(f'List of unique numbers in sets -> {unique_numbers_in_sets}')


# Task 2

# update()
set1 = {1, 2, 3, 5, 6, 8, 9, 10}
set2 = {1, 2, 4, 5, 6, 9, 12}
set3 = { 2, 5, 6, 9, 13, 7}
set1 |= set2 | set3 # Adds to set1 all elements from set2 and set3

print(f'{set1 = } <- update()')


# intersection_update()
set_A = {1, 2, 3, 5, 6, 8, 9, 10}
set_B = {1, 2, 4, 5, 6, 9, 12}
set_C = { 2, 5, 6, 9, 13, 7}
set_A &= set_B & set_C # Leaves in set_A only those elements that are in set_B and set_C

print(f'{set_A = } <- intersection_update()')

# difference_update()
first_set = {1, 2, 3, 5, 6, 8, 9, 10, 'f', 'g'}
second_set = {1, 2, 4, 5, 6, 9, 12}
third_set = { 2, 5, 6, 9, 13, 7}
first_set -= second_set | third_set # Removes from first_set all elements included in second_set and third_set

print(f'{first_set = } <- difference_update()')

#symmetric_difference_update()
set_I = {1, 2, 3, 5, 6, 8, 9, 10, 'f', 'g'}
set_II = {1, 2, 4, 5, 6, 9, 12}
set_III = { 2, 5, 6, 9, 13, 7}
set_I ^= set_II | set_III # Adds to the set_I the elements that are in set_I or set_II or set_III ->
# -> but not three of them at the same time

print(f'{set_I = } <- symmetric_difference_update()')
