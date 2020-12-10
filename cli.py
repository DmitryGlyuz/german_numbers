# This file contains functions for working via the command line
import core


# Input integer & show error message & repeat if something goes wrong or use default value (optionally)
def input_int(prompt, min_n=1, max_n=999999999999999, default=False, show_default=None, show_range=True):
    def print_error(message):
        beginning = 'Error: ' if not default else ''
        ending = f'The default value will be used {default}.' if default else 'Try again.'
        print(f'{beginning}{message}. {ending}')

    if default is not False and show_default is None:
        show_default = True
    number = 0
    prompt_default = f' (default - {default})' if show_default else ''
    prompt_range = f' [{min_n} - {max_n}]' if show_range else ''
    # Checking whether a number is in the required range
    while not min_n <= number <= max_n:
        error_message = None
        try:
            number = int(input(f'{prompt}{prompt_default}{prompt_range}: '))
            if not min_n <= number <= max_n:
                error_message = f'Your number less than {min_n}' if number < min_n else f'Your number more than {max_n}'
                raise ValueError
        except ValueError:
            if not error_message:
                error_message = 'That is not integer value'
            print_error(error_message)
            if default:
                number = default
    return number


# Request the required number of items in the list
def number_of_points(things, min_val, max_va, new_line=False):
    first = '\n' if new_line is True else ''
    return input_int(f'{first}Enter the number of {things}', min_val, max_va)


# Simple CL interface for saving data to a file with a predefined name
def save_file(incoming_data, file_name):
    if input(f"Enter 'Y' if you would like to save the data to {file_name}: ").upper() == 'Y':
        try:
            core.write_to_file(incoming_data, file_name)
        except:
            print('An error occurred while writing to file')
        else:
            print(f'The data was saved to {file_name}')
