# This file contains functions for working via the command line
import core


def try_int(incoming_str, min_int=1, max_int=999999999999999, default=False):
    def print_error(message):
        beginning = 'Error: ' if not default else ''
        ending = f'\nThe default value will be used: {default}' if default else '\nTry again.'
        print(f'{beginning}{message}. {ending}')

    error_message = None

    try:
        number = int(incoming_str)
        if not min_int <= number <= max_int:
            error_message = 'Your number ' + (f'less than {min_int}' if number < min_int else f'more than {max_int}')
            raise ValueError
    except ValueError:
        if not error_message:
            error_message = 'That is not integer value'
        print_error(error_message)
        number = default if default else None
    return number


# Input integer & show error message & repeat if something goes wrong or use default value (optionally)
def input_int(prompt, min_n=1, max_n=999999999999999, default=None, show_range=True):
    number = None
    prompt_default = f' (default: {default})' if default else ''
    prompt_range = f' [{min_n} - {max_n}]' if show_range else ''
    # Checking whether a number is in the required range
    while not number:
        number = try_int(input(f'{prompt}{prompt_range}{prompt_default}: '), min_n, max_n, default)
    return number


# Request the required number of items in the list
def number_of_points(things, min_val, max_val, new_line=False):
    first = '\n' if new_line is True else ''
    return input_int(f'{first}Enter the number of {things}', min_val, max_val, 10)


# Simple CL interface for saving data to a file with a predefined name
def save_file(incoming_data, file_name):
    if input(f"Enter 'Y' if you would like to save the data to {file_name}: ").upper() == 'Y':
        try:
            core.write_to_file(incoming_data, file_name)
        except:
            print('An error occurred while writing to file')
        else:
            print(f'The data was saved to {file_name}')
