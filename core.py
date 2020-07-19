import random


# Input integer and repeat if something goes wrong
def input_int(prompt, min_n, max_n):
    def print_error(message):
        print(f'Error: {message}. Try again.')

    number = 0
    while number < min_n or number > max_n:
        try:
            number = int(input(prompt))
            if number < min_n:
                print_error(f'Yor number less than {min_n}')
            elif number > max_n:
                print_error(f'Your number more than {max_n}')
        except ValueError:
            print_error('That is not integer value')
    return number


# Generator of new random numbers. It avoid repeats
def new_randint(range_min, range_max, used_list):
    available_values = []
    for i in range(range_min, range_max + 1):
        # Filling the list of available numbers with numbers were not used
        if i not in used_list:
            available_values.append(i)
    # Take any random value if all numbers in the range were used
    if not available_values:
        value = random.randint(range_min, range_max - 1)
    else:
        # If we have available numbers -> Take one of them
        value = random.choice(available_values)
        used_list.append(value)
    return value


# This function shows random content from another modules
def show(func, things, show_second_list=False, second_list_header='', min_num=1, max_num=30):
    # Enter the number of things to print
    num_of_outputs = input_int(f'Enter the number of {things} (from {min_num} to {max_num}): ', min_num, max_num)

    # Output
    second_list = [] if show_second_list is True else None
    print()
    for i in range(1, num_of_outputs + 1):
        if show_second_list is True:
            (first_out, second_out) = func()
            second_list.append(second_out)
        else:
            first_out = func()
        print(f'{i}. {first_out}')

    # Print separated list
    if show_second_list is True:
        print(f'\n{second_list_header}')
        for line in second_list:
            print(f'{second_list.index(line) + 1}. {line}')


# Main function which converts integers to strings with these integers in German
def int_to_german(number):
    # Dictionary with numbers in German
    numbers_dict = {
        0: 'null',
        1: 'eins',
        2: 'zwei',
        3: 'drei',
        4: 'vier',
        5: 'fünf',
        6: 'sechs',
        7: 'sieben',
        8: 'acht',
        9: 'neun',
        10: 'zehn',
        11: 'elf',
        12: 'zwölf',
        13: 'dreizehn',
        14: 'vierzehn',
        15: 'fünfzehn',
        16: 'sechzehn',
        17: 'siebzehn',
        18: 'achtzehn',
        19: 'neunzehn',
        20: 'zwanzig',
        30: 'dreißig',
        40: 'vierzig',
        50: 'fünfzig',
        60: 'sechzig',
        70: 'siebzig',
        80: 'achtzig',
        90: 'neunzig'

    }
    # We work only with this range
    if number > 999999999999999 or number < 0:
        raise ValueError

    # Take three digits from some part of the number and work with them
    def units_tens_hundreds(three_digits):
        # Units
        units_str_slice = str(three_digits)[-1]
        units_slice = int(units_str_slice)
        if three_digits > 0 and str(three_digits)[-1] == '0':
            units = ''
        else:
            units = numbers_dict[int(str(three_digits)[-1])]

        # Tens
        if len(str(three_digits)) == 1 or str(three_digits)[-2] == '0':
            tens_units = units
        elif int(str(three_digits)[-2:]) in numbers_dict.keys():
            tens_units = numbers_dict[int(str(three_digits)[-2:])]
        else:
            int_tens_units = int(str(three_digits)[-2:])
            tens = numbers_dict[int_tens_units - units_slice]
            tens_units = units + 'und' + tens

        # Hundreds
        if three_digits < 100:
            hundreds = ''
        else:
            str_hundreds = str(three_digits)[-3]
            int_hundreds = int(str_hundreds)
            if int_hundreds == 1:
                hundreds = 'hundert'
            elif int_hundreds == 0:
                hundreds = ''
            else:
                hundreds = numbers_dict[int_hundreds] + 'hundert'
        german_three_digits = hundreds + tens_units
        return german_three_digits

    # First part of number is ready!
    result = units_tens_hundreds(number)

    # Thousands
    if number > 999:
        if result.startswith('hundert') is True:
            result = 'ein' + result
        thousands = 'tausend' if number < 1000000 or number >= 1000000 and str(number)[-6:-3] != '000' else ''
        if 2000 > number > 1000:
            thousands = 'ein' + thousands
        elif number >= 2000:
            thousands = units_tens_hundreds(int(str(number)[:-3])) + thousands
        result = thousands + result

    # Large numbers
    def large_numbers(key):
        # Dictionary with large numbers in German
        large_numbers_dict = {
            1000000: ('Million', 'Millionen'),
            1000000000: ('Milliarde', 'Milliarden'),
            1000000000000: ('Billion', 'Billionen')
        }

        # Position of large values in number
        positions = {
            1000000: (-9, -6),
            1000000000: (-12, -9),
            1000000000000: (-15, -12)
        }
        pos = positions[key]
        if len(str(number)[:pos[1]]) > 3 and str(number)[pos[0]:pos[1]] == '000':
            return ''
        part_of_number = units_tens_hundreds(int(str(number)[:pos[1]]))

        # Cut the ending if number ends with 1
        if part_of_number.endswith('eins'):
            if part_of_number == 'eins':
                part_of_number = 'eine'
            else:
                # Cutting 's'
                part_of_number = part_of_number[:-1]
            return part_of_number + ' ' + large_numbers_dict[key][0] + ' '
        else:
            return part_of_number + ' ' + large_numbers_dict[key][1] + ' '

    # Merge everything
    for large_number in (1000000, 1000000000, 1000000000000):
        if number >= large_number:
            result = large_numbers(large_number) + result
    return result
