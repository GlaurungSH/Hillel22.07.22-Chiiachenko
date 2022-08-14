user_string = input("Please enter any text -> ")
every_third_word = ', '.join(user_string.split(' ')[2::3])

incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
output_list = [letter if isinstance(letter, float)
               else letter if (isinstance(letter, int) and int(letter % 2 == 0))
               else int(letter ** 2) if (isinstance(letter, int) and int(letter % 2 == 1))
               else str(int(letter) * 3) if (isinstance(letter, str) and letter.isnumeric())
               else -1 for letter in incoming_list
               ]

print(f'{every_third_word = }')
print(f'{incoming_list = }')
print(f'{output_list = }')

# I checked each condition individually. I'll leave it here

# incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
# output_list = [letter if isinstance(letter, float) else -1 for letter in incoming_list]

# print(f'{output_list =}')
##################################################################

# incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
# output_list = [letter if (isinstance(letter, int) and int(letter % 2 == 0))
#                else -1 for letter in incoming_list
#                ]
#
# print(f'{output_list =}')
##################################################################

# incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
# output_list = [int(letter ** 2) if (isinstance(letter, int) and int(letter % 2 == 1))
#                else -1 for letter in incoming_list
#                ]
#
# print(f'{output_list =}')
##################################################################

# incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
# output_list = [str(int(letter) * 3) if (isinstance(letter, str) and letter.isnumeric())
#                else -1 for letter in incoming_list
#                ]
#
# print(f'{output_list =}')
##################################################################

