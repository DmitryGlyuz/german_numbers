# This file contains data processing functions that are called from several other files

import random

# Dictionary with numbers in German
NUMERALS = {
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
            super().__init__()
            self.value = value

            # Variables for each digit in class
            self.units = self.value % 10
            self.tens = self.value % 100 - self.units
            self.hundreds = self.value % 1000 - self.tens - self.units

        def __str__(self):
            return str(self.value)

        def __eq__(self, other):
            return self.value == other

        # this method converts the number class to German with separate parameters for thousands and large numbers
        def german(self, large=False, thousand=False):
            # Start the conversion and step by step add the result to the variable
            result = ''

            # Hundreds
            if self.hundreds:
                # If there is only one hundred in the class, write 'hundert' without digit before
                if 100 < self.hundreds < 1000:
                    result = NUMERALS[self.hundreds // 100] + result
                result += 'hundert'

            # Tens & Units
            if self.tens:
                # the simplest case is if the number is in the dictionary
                if self.tens + self.units in NUMERALS.keys():
                    result += NUMERALS[self.tens + self.units]
                else:
                    # write down the units first, and then the tens
                    result += NUMERALS[self.units] + 'und' + NUMERALS[self.tens]
            else:
                if self.units > 0:
                    # Take into various cases of writing units with large numbers
                    if (large or thousand) and self.units == 1:
                        last_digit = 'eine' if large and self.value == 1 else 'ein'
                    else:
                        # Or take units from our dictionary
                        last_digit = NUMERALS[self.units]
                    result += last_digit
            return result

    def __init__(self, number):
        # We work only with this range
        super().__init__()
        if number > 999999999999999 or number < 0:
            raise ValueError
        self.number = int(number)

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
        # Dictionary with values. Numbers in keys are positions in classes_list
        # Here are two elements in pairs: for singular and plural
        large_numbers = {
            4: ('Billion', 'Billionen'),
            3: ('Milliarde', 'Milliarden'),
            2: ('Million', 'Millionen')
        }
        # Start collecting data to this variable
        result = ''

        for key in large_numbers.keys():
            large_value = ''
            # Check whether there is a class of trillions, billions, millions
            if key > (len(self.classes) - 1):
                continue
            else:
                if self.classes[key]:
                    # Singular or plural
                    tuple_index = 0 if self.classes[key].units == 1 else 1
                    large_value = large_numbers[key][tuple_index]
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
        return str(result)


# Dictionary for already used random values
log = {}


# Returns a random number and uses a list with already used values to avoid repetitions
def unique_randint(min_val, max_val, log_key):
    if not log.get(log_key):
        log[log_key] = []
    required_range = range(min_val, max_val + 1)
    recent_values = log[log_key][-len(required_range) + 1:]
    available_values = list(set(required_range) - set(recent_values))
    value = random.choice(available_values)
    log[log_key].append(value)
    return value


# Returns a random list item using the logic of the previous function
def unique_item(incoming_list, log_key):
    return incoming_list[unique_randint(0, len(incoming_list) - 1, log_key)]


# Returns a string with numeric (optionally) list from a variable of type list or dictionary
# The list is indented so that the items on the right are evenly spaced
def get_lines(incoming, numeric_list=True):
    output = ''
    if type(incoming) == dict:
        keys_length = [len(str(k)) for k in incoming.keys()]
        for k, v in incoming.items():
            indent_length = max(keys_length) - len(str(k)) + 1
            output += f'{k}{" " * indent_length}{v}\n'
    elif type(incoming) == list:
        list_length = len(incoming)
        for n in range(1, list_length + 1):
            if numeric_list:
                indent_length = len(str(list_length)) - len(str(n)) + 1
                output += f'{n}.{" " * indent_length}'
            output += f'{incoming[n - 1]}\n'
    else:
        raise TypeError
    return output


# Saves incoming variable
def write_to_file(content, file_name):
    with open(file_name, 'w') as text_file:
        print(content, file=text_file)
