import random
import interface
from german_numbers import int_to_german

second_list = []

print('1 - plus/minus examples\n'
      '2 - multiplizieren/geteilt examples\n'
      '3 - everything\n')
mode = 0
mode = interface.input_int('Select mode: ', 1, 3)

operations_list = ['+', '-', '*', '/']
german_operations_dict = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplizieren mit',
    '/': 'geteilt durch'
}


def print_examples():
    if mode == 1:
        operation = random.choice(operations_list[:2])
    elif mode == 2:
        operation = random.choice(operations_list[2:])
    else:
        operation = random.choice(operations_list)
    operation_german = german_operations_dict[operation]
    x = random.randint(1, 99)
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

    result = f'{x} {operation} {y} = {z}'
    second_list.append(int_to_german(x) + ' ' + operation_german + ' ' + int_to_german(y) + ' gleich ' + int_to_german(z))
    return result, second_list


interface.generator(print_examples, 'examples', True)