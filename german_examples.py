# This script generates simple random math examples written in German

import random
import cli
import core

# Lists with items that have already been used, so that they will not repeat
numbers_log = []
operations_log = []


def random_multipliers():
    outgoing_list = []
    for m1 in range(2, 10):
        for m2 in range(m1, 10):
            outgoing_list.append((m1, m2))
    random.shuffle(outgoing_list)
    return outgoing_list


multipliers_list = random_multipliers()


def get_pair():
    if not multipliers_list:
        multipliers_list.extend(random_multipliers())
    return multipliers_list.pop()


# Dictionary with math operations in German
german_operations_dict = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplizieren mit',
    '/': 'geteilt durch'
}

# Get list with operations from previous dictionary's keys
operations_list = [k for k in german_operations_dict.keys()]

# Dictionary with operating modes
modes_dict = {
    1: 'plus / minus',
    2: 'multiply / divide',
    3: 'everything'
}


def get_lines(incoming_list, numeric=True):
    output = ''
    number = 1
    for element in incoming_list:
        if numeric is True:
            output += f'{number}. {element}\n'
            number += 1
        else:
            output += f'{element}\n'
    return output


# Prepare data for writing math examples
def get_example_parts(mode):
    # Alternate operations (for first two modes)
    def alternate(operations):
        return core.unique_item(operations, operations_log)

    # Selection type of math operation
    if mode == 'plus / minus':
        operation = alternate(operations_list[:2])
    else:
        if mode == 'multiply / divide':
            operation = alternate(operations_list[2:])
        elif mode == 'everything':
            operation = alternate(operations_list)

    # Generate random numbers and result
    if operation == '+':
        x = core.unique_randint(1, 99, numbers_log)
        y = core.unique_randint(1, 99, numbers_log)
        z = x + y
    elif operation == '-':
        x = core.unique_randint(2, 99, numbers_log)
        y = core.unique_randint(1, x, numbers_log)
        z = x - y
    else:
        # Take one random pair from generated list
        pair = get_pair()

        # Random order of multipliers
        (x, y) = pair if random.getrandbits(1) == 0 else (pair[1], pair[0])
        z = x * y
        if operation == '/':
            (x, z) = (z, x)
    return x, operation, y, z


raw_examples = []


def make_raw_examples_list(count, mode):
    for i in range(count):
        raw_examples.append(get_example_parts(mode))


def raw_example_to_string(ex):
    (x, operation, y, result) = ex
    return f'{x} {operation} {y} = {result}'


def raw_example_to_german(ex):
    german_x = core.int_to_german(ex[0])
    german_operation = german_operations_dict[ex[1]]
    german_y = core.int_to_german(ex[2])
    german_result = core.int_to_german(ex[3])
    return f'{german_x} {german_operation} {german_y} gleich {german_result}'


def convert_list(incoming_list, converting_action):
    outgoing_list = []
    for element in incoming_list:
        outgoing_list.append(converting_action(element))
    return outgoing_list


def get_data(count, mode, numeric=True):
    make_raw_examples_list(count, mode)
    examples_list = convert_list(raw_examples, raw_example_to_string)
    german_examples_list = convert_list(raw_examples, raw_example_to_german)
    output_examples = get_lines(examples_list, numeric)
    output_german = get_lines(german_examples_list, numeric)
    return output_examples, output_german


if __name__ == '__main__':
    print('What operations do you need to output examples with?')
    for (k, v) in modes_dict.items():
        print(f'   {k} - {v}')
    # Input mode
    selected_mode = modes_dict[cli.input_int('\nSelect mode', 1, 3)]
    number_of_examples = cli.input_int('\nEnter the number of examples', 1, 100)
    (lines_with_examples, lines_with_german) = get_data(number_of_examples, selected_mode)
    print(f'\nExamples:\n'
          f'{lines_with_examples}\n'
          f'German words:\n'
          f'{lines_with_german}')

