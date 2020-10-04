# This file generates two string values with numeric lists:
# 1. Simple random math examples
# 2. These examples written in German
# You can get them as two values from the outside via the function get_data(count, mode)
#       count - number of required elements
#       mode - which type of examples to use - addition and subtraction, multiplication and division, or all together.
#              String values with mode names are contained in the modes_dict dictionary

import random
import cli
import core

# Dictionary with operating modes
modes_dict = {
    1: 'plus / minus',
    2: 'multiply / divide',
    3: 'everything'
}

# Lists where already used values are placed so that they are not repeated
numbers_log = []
operations_log = []
multipliers_log = []

# Dictionary with math operations in German
german_operations_dict = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplizieren mit',
    '/': 'geteilt durch'
}

# Get list with operations from previous dictionary's keys
operations_list = [k for k in german_operations_dict.keys()]

# Creating a list with pairs of multipliers to use them in random order
multipliers_list = []
for m1 in range(2, 10):
    for m2 in range(m1, 10):
        multipliers_list.append((m1, m2))


# Returns four elements of a random example: the first number, the operation, the second number, and the result
def random_example(mode):
    # Returns one of the operations in alternating order
    def alternate(operations):
        return core.unique_item(operations, operations_log)

    # Selecting the type of mathematical operation
    # Take a slice from the list of operations or the entire list
    if mode == 'plus / minus':
        operation = alternate(operations_list[:2])
    elif mode == 'multiply / divide':
        operation = alternate(operations_list[2:])
    else:
        operation = alternate(operations_list)

    # Generating two random numbers and calculating the result of an operation with them
    if operation == '+' or operation == '-':
        (x, y) = [core.unique_randint(1, 99, numbers_log) for _ in range(2)]
        z = x + y
    else:
        # Take one random pair from generated list
        pair = core.unique_item(multipliers_list, multipliers_log)

        # Random order of multipliers
        (x, y) = pair if random.getrandbits(1) == 0 else (pair[1], pair[0])
        z = x * y

    # Swap x and z if the operation is - or /
    if operation == '-' or operation == '/':
        (x, z) = (z, x)
    return x, operation, y, z


# Returns a string value with an example of its parts received as input
def strings(x, operation, y, result):
    return f'{x} {operation} {y} = {result}'


# Returns a string value with an example written in German words
def german(x, operation, y, result):
    german_x = core.int_to_german(x)
    german_operation = german_operations_dict[operation]
    german_y = core.int_to_german(y)
    german_result = core.int_to_german(result)
    return f'{german_x} {german_operation} {german_y} gleich {german_result}'


def get_data(count, mode):
    def examples_to(something):
        return core.convert_list(raw_examples, something)

    raw_examples = core.raw_list(random_example, count, mode)
    examples = examples_to(strings)
    german_examples = examples_to(german)
    output_examples = core.get_lines(examples)
    output_german = core.get_lines(german_examples)
    return output_examples, output_german


if __name__ == '__main__':
    print('What operations do you need to output examples with?')
    for (k, v) in modes_dict.items():
        print(f'   {k} - {v}')
    # Input mode
    selected_mode = modes_dict[cli.input_int('\nSelect mode', 1, 3)]
    number_of_examples = cli.number_of_points('examples', 1, 100, True)
    lines_with_examples, lines_with_german = get_data(number_of_examples, selected_mode)
    print(f'\nExamples:\n'
          f'{lines_with_examples}\n'
          f'German words:\n'
          f'{lines_with_german}')
