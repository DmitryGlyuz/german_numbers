# This file generates string value with random dates written in few formats
# You can get them as two values from the outside via the function get_data(count, short, us, ru, short_de, de)
#       count - number of required elements
#       Next boolean variables define the output formats and are enabled by default
#       short - DD.MM.YYYY
#       us - US format
#       ru - Russian format
#       short_de - German format
#       de - everything is written as German words


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


# Convert natural integer (from 1 to 31) to German ordinal number and return with a prefix 'der'
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


# Lists where already used values are placed so that they are not repeated
days_log = []
months_log = []
years_log = []
centuries_log = []

# Dictionary with for centuries, and the years included in them
centuries_dict = {
    19: (1800, 1899),
    20: (1900, 1999),
    21: (2000, 2030)
}


# Returns three integer values with elements of random date: day, month and year
def random_date():
    # Choose number with random month
    month = core.unique_randint(1, 12, months_log)

    # Generate random day. Take max value from months_dict
    day = core.unique_randint(1, months_dict['days'][month - 1], days_log)

    # Choose century avoiding repeats and define range of years
    century = core.unique_randint(19, 21, centuries_log)
    (min_year, max_year) = centuries_dict[century]

    # Generate random year
    year = core.unique_randint(min_year, max_year, years_log)
    return day, month, year


# Returns a string value with a date in the format DD.MM.YYYY
def dd_mm_yyyy(day, month, year):
    if month < 10:
        month_string = '0' + str(month)
    else:
        month_string = str(month)
    return f'{day}.{month_string}.{year}'


# Returns a string value with a date in Russian format
def russian(day, month, year):
    return f'{day} {months_dict["russian"][month - 1]} {year} г.'


# Returns a string value with a date in US format
def american(day, month, year):
    return f'{months_dict["english"][month - 1]} {day}, {year}'


# Returns a string value with a date in German format
def short_german(day, month, year):
    return f'{day}. {months_dict["german"][month - 1]} {year}'


# Returns a string value with a date written by German words
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


# Returns string value with random dates written in few formats described at the beginning of the file
def get_data(count, short=True, us=True, ru=True, short_de=True, de=True):
    # Create a list with elements of random dates
    raw_dates = core.raw_list(random_date, count)

    # Simplified version of convert_list function
    def dates_to(something):
        return core.convert_list(raw_dates, something)

    # Create lists with dates in different formats
    short_dates = dates_to(dd_mm_yyyy)
    russian_dates = dates_to(russian)
    american_dates = dates_to(american)
    short_german_dates = dates_to(short_german)
    german_dates = dates_to(german)

    # A list with string values containing each date represented in the required formats
    output_list = []

    # Create string variables that contain either the date in the required format,
    # or nothing if some format is not needed
    def fill_var(mode, var_val):
        return var_val if mode is True else '\n'

    slash = ' / ' if us is True else ''
    for i in range(count):
        short_date = fill_var(short, f'{short_dates[i]}{slash}')
        american_date = fill_var(us, f'{american_dates[i]}\n')
        russian_date = fill_var(ru, f'   {russian_dates[i]}\n')
        header_german = f'   German:\n' if short_de is True or de is True else ''
        short_german_date = fill_var(short_de, f'   {short_german_dates[i]}\n')
        german_date = fill_var(de, f'   {german_dates[i]}\n')

        # Add the received string value to the outgoing list
        output_list.append(f'{short_date}{american_date}{russian_date}{header_german}{short_german_date}{german_date}')
    # Return this list as string value
    return core.get_lines(output_list)


# Command line interface
if __name__ == '__main__':
    # Input required number of examples
    number_of_dates = cli.number_of_points('dates', 1, 100)
    # Print these days
    print(get_data(number_of_dates))
