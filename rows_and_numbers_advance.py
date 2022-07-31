# Create a sequence of instructions that:
# Gets a name from the user, where each letter can be both lowercase and uppercase,
# spaces before and after the name are also possible, for example wiLLiAm

enter_name = input("Please, enter your name: ")
new_length = len(enter_name) + 2
spaces_both_sides = enter_name.center(new_length)
print("Space on both sides of a word ->", spaces_both_sides)


# Strips a name of leading and trailing spaces (find a method for strings that does this)

delete_spaces = spaces_both_sides.strip()
print("Remove spaces on both sides ->", delete_spaces)


# Prints a greeting for this name in uppercase, lowercase letters

greetings_capitalize = delete_spaces.capitalize()
print(f'Hello {greetings_capitalize}')


# Prints the number of letters in the name

print('Length of string ->', len(greetings_capitalize))


# Prints the name backwards

print('The name backwards ->', greetings_capitalize[::-1])
