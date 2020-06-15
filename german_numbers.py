# This is main function, it converts simple integer to string value with this number written in German
# Other files in this project use it


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
    def units_tens_hundreds(threedigits):
        # Units
        units_str_slice = str(threedigits)[-1]
        units_slice = int(units_str_slice)
        if threedigits > 0 and str(threedigits)[-1] == '0':
            units = ''
        else:
            units = numbers_dict[int(str(threedigits)[-1])]

        # Tens
        if len(str(threedigits)) == 1 or str(threedigits)[-2] == '0':
            tens_units = units
        elif int(str(threedigits)[-2:]) in numbers_dict.keys():
            tens_units = numbers_dict[int(str(threedigits)[-2:])]
        else:
            int_tens_units = int(str(threedigits)[-2:])
            tens = numbers_dict[int_tens_units - units_slice]
            tens_units = units + 'und' + tens

        # Hundreds
        if threedigits < 100:
            hundreds = ''
        else:
            str_hundreds = str(threedigits)[-3]
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
        # Dictonary with large numbers in German
        large_numbers_dict = {
            'millions': ('Million', 'Millionen'),
            'billions': ('Milliarde', 'Milliarden'),
            'trillions': ('Billion', 'Billionen')
        }

        # Position of large values in number
        positions = {
            'millions': (-9, -6),
            'billions': (-12, -9),
            'trillions': (-15, -12)
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
    if number >= 1000000:
        result = large_numbers('millions') + result
    if number >= 1000000000:
        result = large_numbers('billions') + result
    if number >= 1000000000000:
        result = large_numbers('trillions') + result
    return result


# Simple interface where we can check how our function works
# Enter any non-Int to exit
if __name__ == '__main__':
    while True:
        try:
            n = int(input('Number: '))
            print(int_to_german(n))
        except ValueError:
            print('Tschüss!')
            exit()

