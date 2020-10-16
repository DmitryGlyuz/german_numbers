# This file contains functions for working via the command line

# Input integer & show error message & repeat if something goes wrong
def input_int(prompt, min_n, max_n):
    def print_error(message):
        print(f'Error: {message}. Try again.')

    # Checking whether a number is in the required range
    number = 0
    while number < min_n or number > max_n:
        try:
            number = int(input(f'{prompt} [{min_n} - {max_n}]: '))
            if number < min_n:
                print_error(f'Yor number less than {min_n}')
            elif number > max_n:
                print_error(f'Your number more than {max_n}')
        except ValueError:
            print_error('That is not integer value')
    return number


# Request the required number of items in the list
def number_of_points(things, min_val, max_va, new_line=False):
    first = '\n' if new_line is True else ''
    return input_int(f'{first}Enter the number of {things}', min_val, max_va)
