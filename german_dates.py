# This script generates random dates in German

import cli
import core

# Dictionary with ordinal numbers in German
ord_numbers_dict = {
    1: 'erste',
    2: 'zweite',
    3: 'dritte',
    7: 'siebte',
    8: 'achte',

}

# This dictionary contains the number of days in each mouth and names of months in English, German and Russian
months_dict = {
    'days': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'english': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December'],
    'german': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
               'November', 'Dezember'],
    'russian': ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                'ноября', 'декабря']
    }


# Convert natural integer to German ordinal number and return with a prefix 'der'
def int_to_ordinal(number):
    if 1 <= number <= 19:
        if number in ord_numbers_dict.keys():
            ord_number = ord_numbers_dict[number]
        else:
            ord_number = core.int_to_german(number) + 'te'
    elif 20 <= number <= 31:
        ord_number = core.int_to_german(number) + 'ste'
    else:
        raise ValueError
    return 'der ' + ord_number


# Lists of numbers that have already been used, so that they do not repeat
days_log = []
months_log = []
years_log = []
centuries_log = []

centuries_dict = {
    19: (1800, 1899),
    20: (1900, 1999),
    21: (2000, 2030)
}


def random_date():
    # Choose random month
    month = core.unique_randint(1, 12, months_log)

    # Generate random day. Take max value from months_dict
    day = core.unique_randint(1, months_dict['days'][month - 1], days_log)

    # Choose century avoiding repeats
    century = core.unique_randint(19, 21, centuries_log)
    (min_year, max_year) = centuries_dict[century]

    # Generate random year
    year = core.unique_randint(min_year, max_year, years_log)
    return day, month, year


def dd_mm_yyyy(day, month, year):
    if month < 10:
        month_string = '0' + str(month)
    else:
        month_string = str(month)
    return f'{day}.{month_string}.{year}'


def russian(day, month, year):
    return f'{day} {months_dict["russian"][month - 1]} {year} г.'


def american(day, month, year):
    return f'{months_dict["english"][month - 1]} {day}, {year}'


def short_german(day, month, year):
    return f'{day}. {months_dict["german"][month - 1]} {year}'


def german(day, month, year):
    # Convert day to German ordinal
    day_german = int_to_ordinal(day)
    # There are two ways how to write years in German. It depends on century
    if year > 1999:
        year_german = core.int_to_german(year)
    else:
        year_first_part = int(str(year)[:2])
        year_second_part = int(str(year)[2:])
        year_german = core.int_to_german(year_first_part) + 'hundert' + core.int_to_german(year_second_part)
    return f'{day_german} {months_dict["german"][month - 1]} {year_german}'


def get_lists(count):
    def dates_to(something):
        return core.convert_list(raw_dates, something)

    raw_dates = core.raw_list(random_date, 10)
    short_dates = dates_to(dd_mm_yyyy)
    russian_dates = dates_to(russian)
    american_dates = dates_to(american)
    short_german_dates = dates_to(short_german)
    german_dates = dates_to(german)
    return short_dates, russian_dates, american_dates, short_german_dates ,german_dates


def complete_output(count, short=True, us=True, ru=True, short_de=True, de=True):
    def fill_var(mode, var_val):
        return var_val if mode is True else ''

    short_dates, russian_dates, american_dates, short_german_dates, german_dates = get_lists(count)
    output_list = []
    for i in range(count):
        if short is True:
            short_date = short_dates[i]
            if us is True:
                short_date += ' / '
        else:
            short_date = ''
        american_date = fill_var(us, f'{american_dates[i]}\n')
        russian_date = fill_var(ru, f'   {russian_dates[i]}\n')
        header_german = f'   German:\n' if short_de is True or de is True else ''
        short_german_date = fill_var(short_de, f'   {short_german_dates[i]}\n')
        german_date = fill_var(de, f'   {german_dates[i]}\n')
        output_list.append(f'{short_date}{american_date}{russian_date}{header_german}{short_german_date}{german_date}')
    return core.get_lines(output_list)


if __name__ == '__main__':
    number_of_dates = cli.number_of_points('dates', 1, 100)
    print(complete_output(number_of_dates))

