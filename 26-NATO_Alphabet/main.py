# creating a new list with for loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# creating a new list with list comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

# python sequences
# -------------------
# string
# tuple
# list
# dictionary

# conditional list comprehension
# new_list = [new_item for item in list if test]

# new_list = [n + 1 for n in numbers]
# print(new_list)
# [2, 3, 4]
# print(numbers)
# [1, 2, 3]
# name = "Angela"
# letters_list = [letter for letter in name]
# doubled = [2 * n for n in range(1, 5)]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# uppercase_names = [name.upper() for name in name if len(name) >= 5]
# print(uppercase_names)
# []
# uppercase_names = [name.upper() for name in names if len(name) >= 5]
# print(uppercase_names)
# ['CAROLINE', 'ELANOR', 'FREDDIE']

