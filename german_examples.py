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


class Example:
    # Dictionary with math operations in German
    operations_dict = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplizieren mit',
        '/': 'geteilt durch'
    }
    # Creating a list with pairs of multipliers to use them in random order
    multipliers_list = []
    for m1 in range(2, 10):
        for m2 in range(m1, 10):
            multipliers_list.append((m1, m2))

    def __init__(self, x=1, operation="+", y=1, get_random=False, mode='everything'):
        if operation not in Example.operations_dict.keys():
            raise ValueError
        if get_random:
            # Take a slice from the list of operations or the entire list
            self.available_operations = list(self.operations_dict.keys())
            if mode == 'plus / minus':
                self.available_operations = self.available_operations[:2]
            elif mode == 'multiply / divide':
                self.available_operations = self.available_operations[2:]
            self.operation = core.unique_item(self.available_operations, 'operations')
            if self.operation in ('+', '-'):
                (self.x, self.y) = [core.unique_randint(1, 99, 'numbers') for _ in range(2)]
            else:
                # Take one random pair from generated list
                self.x, self.y = core.unique_item(self.multipliers_list, 'multipliers')

                # Random order of multipliers
                if random.getrandbits(1) == 1:
                    (self.x, self.y) = (self.y, self.x)
        else:
            self.x = x
            self.y = y
            self.operation = operation

        self.z = self.x + self.y if self.operation in ('+', '-') else self.x * self.y
        if self.operation in ('-', '/'):
            (self.x, self.z) = (self.z, self.x)

    def __str__(self):
        return f'{self.x} {self.operation} {self.y} = {self.z}'

    # Returns a string value with an example written in German words
    def german(self):
        return f'{core.GermanNumeral(self.x)} {self.operations_dict[self.operation]} ' \
               f'{core.GermanNumeral(self.y)} gleich {core.GermanNumeral(self.z)}'


# Returns two string values with numeric(optionally) lists:
def get_data(count, mode, numeric=True):
    # Create a list with random examples
    examples_list = ([Example(get_random=True, mode=mode) for _ in range(count)])
    lines_examples = core.get_lines(examples_list, numeric)
    lines_german = core.get_lines([example.german() for example in examples_list], numeric)
    return lines_examples, lines_german


# Command line interface
if __name__ == '__main__':
    print('What operations do you need to output examples with?')
    for (k, v) in modes_dict.items():
        print(f'   {k} - {v}')

    # Input mode
    selected_mode = modes_dict[cli.input_int('\nSelect mode', 1, 3)]

    # Input required number of examples
    number_of_examples = cli.number_of_points('examples', 1, 100, True)

    # Get two string values with lists
    examples, german_examples = get_data(number_of_examples, selected_mode)

    # Print these lists
    print(f'\nExamples:\n'
          f'{examples}\n'
          f'German words:\n'
          f'{german_examples}')
