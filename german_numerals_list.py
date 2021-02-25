# This file generates a list of numbers in a given range in numeric format and in German

import cli
import core

# Dictionary with numbers as keys and German numerals as values
numerals_dict = {}


# Add number and German numeral to numerals_dict
def add_number(number):
    numerals_dict[number] = str(core.GermanNumeral(number))


# Add every number from the specified range to numerals_dict
def add_range(min_value, max_value):
    # result = {}
    for n in range(min_value, max_value + 1):
        add_number(n)


if __name__ == '__main__':
    print("Enter numbers to fill in the list of numerals\n"
          "You can enter individual numbers or ranges (two numbers separated by '-')\n"
          "Press Enter to finish filling\n")

    user_input = ' '
    while user_input:
        user_input = input("Enter a number or range: ")
        if '-' in user_input:
            user_input = user_input.split('-')[:2]
            for i in range(2):
                print(f'{user_input[i]} - {("first", "last")[i]} value in range')
                if not cli.try_int(user_input[i]):
                    break
            else:
                first, last = map(int, user_input)
                if first > last:
                    first, last = last, first
                add_range(first, last)
                print(f'Range {first} - {last} added')
        elif user_input:
            if cli.try_int(user_input):
                add_number(int(user_input))
                print('The number added')

    # Generate string value with numerals list
    numerals = core.get_lines(numerals_dict)

    # Print & Save to file
    print(f'\nGerman numerals:\n{numerals}')
    cli.save_file(numerals, 'numerals.txt')
