# This file contains data processing functions that are called from several other files

import random

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


class GermanNumeral:
    class ClassOfNumber(int):
        def __init__(self, value):
            self.value = value
            self.units = self.value % 10
            self.tens = self.value % 100 - self.units
            self.hundreds = self.value % 1000 - self.tens - self.units

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            return True if self.value == other else False

        def german(self, large=False, thousand=False):
            result = ''
            # Hundreds
            if self.hundreds:
                hundreds_digit = self.hundreds // 100
                if 1 < hundreds_digit < 10:
                    result = numbers_dict[hundreds_digit] + result
                result += 'hundert'

            # Tens & Units
            if self.tens:
                if self.tens + self.units in numbers_dict.keys():
                    result += numbers_dict[self.tens + self.units]
                else:
                    result += numbers_dict[self.units] + 'und' + numbers_dict[self.tens]
            else:
                if self.units > 0:
                    if (large or thousand) and self.units == 1:
                        last_digit = 'eine' if large and self.value == 1 else 'ein'
                    else:
                        last_digit = numbers_dict[self.units]
                    result += last_digit
            return result

    def __init__(self, number):
        if number > 999999999999999 or number < 0:
            raise ValueError
        self.number = number
        self.classes = []
        self.n = self.number
        while self.n > 0:
            self.remainder = self.n % 1000
            self.classes.append(self.ClassOfNumber(self.remainder))
            self.n //= 1000

    def __str__(self):
        large_numbers_dict = {
            4: ('Billion', 'Billionen'),
            3: ('Milliarde', 'Milliarden'),
            2: ('Million', 'Millionen')
        }
        result = ''
        for key in large_numbers_dict.keys():
            large_value = ''
            if key > (len(self.classes) - 1):
                continue
            else:
                if self.classes[key]:
                    large_value = large_numbers_dict[key][0] if self.classes[key].units == 1 else large_numbers_dict[key][1]
                result += f'{self.classes[key].german(large=True)} {large_value} '

        if self.number > 999:
            if self.classes[1]:
                if self.classes[1] > 1:
                    result += self.classes[1].german(thousand=True)
                elif self.classes[0]:
                    result += 'ein'
                result += 'tausend'

            if self.classes[0].hundreds == 100:
                result += 'ein'

        if self.classes[0] != 0:
            result += self.classes[0].german()
        return result





# Main function which converts integers to strings with these numbers in German
def int_to_german(*args):
    # Dictionary with numbers in German

    results_list = []
    for number in args:
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
                temp = units_tens_hundreds(int(str(number)[:-3]))
                if temp.endswith('eins'):
                    thousands = temp[:-1] + thousands
                else:
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
        results_list.append(result)
    if len(results_list) == 1:
        return result
    else:
        return results_list


# Returns a random number and uses a list with already used values to avoid repetitions
def unique_randint(min_val, max_val, log):
    available_values = []
    for i in range(min_val, max_val + 1):
        # Filling the list with numbers that haven't been used yet.
        # We take a slice of the log file to take only the required range.
        # This way, repeats can only occur after all other available values have run out
        if i not in log[-len(range(min_val, max_val)):]:
            available_values.append(i)
    value = random.choice(available_values)
    log.append(value)
    return value


# Returns a random list item using the logic of the previous function
def unique_item(incoming_list, log):
    return incoming_list[unique_randint(0, len(incoming_list) - 1, log)]


# Returns a string with numeric (optionally) list from a variable of type list
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


# Returns a list of the required length, filling it with the outputs of the specified functions.
# Returned items require further processing
def raw_list(incoming_function, count, *args):
    outgoing_list = []
    for i in range(count):
        outgoing_list.append(incoming_function(*args))
    return outgoing_list


# Returns a list where each element of the incoming list is processed by the function specified in the parameters
def convert_list(incoming_list, converting_action):
    outgoing_list = []
    for element in incoming_list:
        outgoing_list.append(converting_action(*element))
    return outgoing_list


if __name__ == '__main__':
    for i in range(1, 100000000):
        word1 = str(GermanNumeral(i))
        word2 = int_to_german(i)
        if word1 != word2:
            print(i)
            print(GermanNumeral(i))
            print(int_to_german(i))
    print('done')
    # while True:
    #     val = int(input('Value: '))
    #     print(GermanNumeral(val))
    #     print(int_to_german(val))