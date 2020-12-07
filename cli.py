# This file contains functions for working via the command line

# Input integer & show error message & repeat if something goes wrong
def input_int(prompt, min_n=1, max_n=999999999999999, default=False, show_default=None, show_range = True):
    def print_error(message):
        beginning = 'Error: ' if not default else ''
        ending = f'The default value will be used {default}.' if default else 'Try again.'
        print(f'{beginning}{message}. {ending}')

    # Checking whether a number is in the required range
    if default is not False and show_default is None:
        show_default = True
    number = 0
    prompt_default = f' (default - {default})' if show_default else ''
    prompt_range = f' [{min_n} - {max_n}]' if show_range else ''
    while not min_n <= number <= max_n:
        error_message = None
        try:
            number = int(input(f'{prompt}{prompt_default}{prompt_range}: '))
            if not min_n <= number <= max_n:
                error_message = f'Your number less than {min_n}'if number < min_n else f'Your number more than {max_n}'
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
