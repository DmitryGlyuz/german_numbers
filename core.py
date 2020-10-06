# This file contains data processing functions that are called from several other files

import random

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


# The main class, objects when created accept integers, convert and output as string values with numbers in German
class GermanNumeral(str):
    # Objects with number classes (every three digits) contain part of the logic for translating the numeral into German
    class NumberClass(int):
        def __init__(self, value):
            self.value = value

            # Variables for each digit in class
            self.units = self.value % 10
            self.tens = self.value % 100 - self.units
            self.hundreds = self.value % 1000 - self.tens - self.units

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            return True if self.value == other else False

        # this method converts the number class to German with separate parameters for thousands and large numbers
        def german(self, large=False, thousand=False):
            # Start the conversion and step by step add the result to the variable
            result = ''

            # Hundreds
            if self.hundreds:
                # If there is only one hundred in the class, write 'hundert' without digit before
                if 100 < self.hundreds < 1000:
                    result = numbers_dict[self.hundreds // 100] + result
                result += 'hundert'

            # Tens & Units
            if self.tens:
                # the simplest case is if the number is in the dictionary
                if self.tens + self.units in numbers_dict.keys():
                    result += numbers_dict[self.tens + self.units]
                else:
                    # write down the units first, and then the tens
                    result += numbers_dict[self.units] + 'und' + numbers_dict[self.tens]
            else:
                if self.units > 0:
                    # Take into various cases of writing units with large numbers
                    if (large or thousand) and self.units == 1:
                        last_digit = 'eine' if large and self.value == 1 else 'ein'
                    else:
                        # Or take units from our dictionary
                        last_digit = numbers_dict[self.units]
                    result += last_digit
            return result

    def __init__(self, number):
        # We work only with this range
        if number > 999999999999999 or number < 0:
            raise ValueError
        self.number = number

        # Divide the number into classes and add them to the list
        self.classes = []
        self.n = self.number
        while self.n > 0:
            self.remainder = self.n % 1000
            self.classes.append(self.NumberClass(self.remainder))
            self.n //= 1000

    # Main logic for converting to German numerals, also using logic from NumberClass
    def __str__(self):
        # Large numbers
        # Dictionary with values. Nu,bers in keys are positions in classes_list
        # Here are two elements in pairs: for singular and plural
        large_numbers_dict = {
            4: ('Billion', 'Billionen'),
            3: ('Milliarde', 'Milliarden'),
            2: ('Million', 'Millionen')
        }
        # Start collecting data to this variable
        result = ''

        for key in large_numbers_dict.keys():
            large_value = ''
            # Check whether there is a class of trillions, billions, millions
            if key > (len(self.classes) - 1):
                continue
            else:
                if self.classes[key]:
                    # Singular or plural
                    large_value = large_numbers_dict[key][0] if self.classes[key].units == 1 else large_numbers_dict[key][1]
                result += f'{self.classes[key].german(large=True)} {large_value} '

        # Thousands
        if self.number > 999:
            if self.classes[1]:
                # Don't write 'ein' if we have 1000
                if self.classes[1] > 1:
                    result += self.classes[1].german(thousand=True)
                elif self.classes[0]:
                    result += 'ein'
                result += 'tausend'

            # Don't write 'ein' if we have 100, but write it in cases like 1100 etc
            if self.classes[0].hundreds == 100:
                result += 'ein'

        # First class of number
        if self.classes[0] != 0:
            result += self.classes[0].german()
        return result


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
