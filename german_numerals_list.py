import core
import cli


def get_translations_list(min_value, max_value):
    result = ''
    for number in range(min_value, max_value + 1):
        result += f'{number}{core.add_indent(number, max_value)}{core.GermanNumeral(number)}\n'
    return result


if __name__ == '__main__':
    first = cli.input_int('Enter the first number in th list', default=1, show_range=False)
    default_last = 100 if first == 1 else False
    last = cli.input_int('Enter the last number in th list', first + 1, default=default_last, show_range=False)

    print(f'\nGerman numerals from {first} to {last}:\n{get_translations_list(first, last)}')
