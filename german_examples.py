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
    multipliers_list = []
    for m1 in range(2, 10):
        for m2 in range(m1, 10):
            multipliers_list.append((m1, m2))

    class Operation(str):
        def __init__(self, value):
            super().__init__()
            if value not in Operations():
                raise ValueError
            self.value = value

        def __str__(self):
            return str(self.value)

        def german(self):
            return Operations.operations_dict[self.value]

    def __init__(self, x=1, operation="+", y=1, get_random=False, mode='everything'):
        if get_random:
            self.operation = self.Operation(Operations(mode).random())
            if self.operation in Operations('plus / minus'):
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
            self.operation = self.Operation(operation)

        self.z = self.x + self.y if self.operation in ('+', '-') else self.x * self.y
        if self.operation in ('-', '/'):
            (self.x, self.z) = (self.z, self.x)

    def __str__(self):
        return f'{self.x} {self.operation} {self.y} = {self.z}'

    def german(self):
        return f'{core.GermanNumeral(self.x)} {self.operation.german()} ' \
               f'{core.GermanNumeral(self.y)} gleich {core.GermanNumeral(self.z)}'


class Operations(tuple):
    # Dictionary with math operations in German
    operations_dict = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplizieren mit',
        '/': 'geteilt durch'
    }

    def __init__(self, mode='everything'):
        super().__init__()
        # Take a slice from the list of operations or the entire list
        if mode == 'everything':
            self.value = tuple(self.operations_dict.keys())
        if mode == 'plus / minus':
            self.value = list(self.operations_dict.keys())[:2]
        if mode == 'multiply / divide':
            self.value = list(self.operations_dict.keys())[2:]

    # Returns one of the operations in alternating order
    def random(self):
        return core.unique_item(self.value, 'operations')

    def __contains__(self, item):
        return True if item in self.value else False

    def __str__(self):
        return f'{self.value}'


# Creating a list with pairs of multipliers to use them in random order
# Returns four elements of a random example: the first number, the operation, the second number, and the result
# Returns a string value with an example of its parts received as input
# Returns a string value with an example written in German words
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
