# This script generates simple random math examples written in German

import random
import interface
from german_numbers import int_to_german

# List of modes
print('1 - plus/minus examples\n'
      '2 - multiplizieren/geteilt examples\n'
      '3 - everything\n')
mode = 0

# Input mode
mode = interface.input_int('Select mode: ', 1, 3)

operations_list = ['+', '-', '*', '/']

# Dictionary with math operations in German
german_operations_dict = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplizieren mit',
    '/': 'geteilt durch'
}


# Prepare data for writing math examples
def print_examples():
    # Selection type of math operation
    if mode == 1:
        operation = random.choice(operations_list[:2])
    elif mode == 2:
        operation = random.choice(operations_list[2:])
    else:
        operation = random.choice(operations_list)
    operation_german = german_operations_dict[operation]

    # Generate firs random number
    x = random.randint(1, 99)

    # Generate second number & selected operation with X and Y and result
    if operation == '+':
        y = random.randint(1, 99)
        z = x + y
    elif operation == '-':
        y = random.randint(1, x)
        z = x - y
    else:
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        z = x * y
        if operation == '/':
            (x, z) = (z, x)

    # Strings with example by numbers and words
    example_numbers = f'{x} {operation} {y} = {z}'
    example_words = int_to_german(x) + ' ' + operation_german + ' ' + int_to_german(y) + ' gleich ' + int_to_german(z)

    # Send these strings to interface script
    return example_numbers, example_words


# Run simple console interface which show random content with user's parameters
interface.generator(print_examples, 'examples', True)