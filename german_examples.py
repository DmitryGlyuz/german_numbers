# This script generates simple random math examples written in German

import random
import core

# List of modes
print('1 - plus/minus examples\n'
      '2 - multiplizieren/geteilt examples\n'
      '3 - everything\n')

# Input mode
mode = core.input_int('Select mode: ', 1, 3)

operations_list = ['+', '-', '*', '/']
operations_log = []

# A list of numbers that have already been used, so that they do not repeat
numbers_log = []

# We need this boolean because we have a generator of number pair inside the function which will run several times,
# but is must be created only onc time
first_run = True

# This is a list where we will put these pairs
multipliers_list = []

# Dictionary with math operations in German
german_operations_dict = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplizieren mit',
    '/': 'geteilt durch'
}


# Prepare data for writing math examples
def print_examples():
    # Take boolean from gloval scope. We will turn it off in the end of this function
    global first_run

    # Alternate operations (for first two modes)
    def alternate(op1, op2):
        if not operations_log:
            return op1
        else:
            return op2 if operations_log[-1] == op1 else op1

    # Selection type of math operation
    if mode == 1:
        operation = alternate('+', "-")
    else:
        # If there will be examples for multiplication and division -> generate a list with number's pairs
        if first_run:
            for m1 in range(2, 10):
                for m2 in range(m1, 10):
                    multipliers_list.append((m1, m2))
        if mode == 2:
            operation = alternate('*', '/')
        elif mode == 3:
            # If we already have 4 examples, clear log and choose any new random operation, but not last
            if len(operations_log) == 4:
                available_operations = operations_list[:]
                available_operations.remove(operations_log[-1])
                # And clear log
                operations_log.clear()
            else:
                # Choose any random operation which is not in log
                available_operations = operations_list[:]
                for op in operations_log:
                    available_operations.remove(op)
            operation = random.choice(available_operations)

    # Add operation to log
    operation_german = german_operations_dict[operation]

    # Generate random numbers and result
    if operation == '+':
        x = core.new_randint(1, 99, numbers_log)
        y = core.new_randint(1, 99, numbers_log)
        z = x + y
    elif operation == '-':
        x = core.new_randint(2, 99, numbers_log)
        y = core.new_randint(1, x, numbers_log)
        z = x - y
    else:
        # Take one random pair from generated list
        pair = random.choice(multipliers_list)
        # And remove
        multipliers_list.remove(pair)

        # Random order of multipliers
        (x, y) = pair if random.getrandbits(1) == 0 else (pair[1], pair[0])
        z = x * y
        if operation == '/':
            (x, z) = (z, x)

    # Strings with example by numbers and words
    example_numbers = f'{x} {operation} {y} = {z}'
    example_words = f'{core.int_to_german(x)} {operation_german} {core.int_to_german(y)} gleich {core.int_to_german(z)}'

    operations_log.append(operation)

    # Turn off this boolean to not repeat generator's running
    first_run = False
    # Send these strings to interface script
    return example_numbers, example_words


# Run simple console interface which show random content with user's parameters
core.show(print_examples, 'examples', True, 'Deutsche Wörter:')
