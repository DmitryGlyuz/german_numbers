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


# Prepare data for writing math examples
def random_example(mode):
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


def strings(x, operation, y, result):
    return f'{x} {operation} {y} = {result}'


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
