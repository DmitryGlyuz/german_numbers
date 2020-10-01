# This script generates random dates in German

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
# days_log = []
# months_log = []
# years_log = []
# centuries_log = []
random_days = []
random_months = []
random_years = []
random_centuries = []

# Tuple with range of years in three used centuries
centuries = ((1800, 1899), (1900, 1999), (2000, 2030))


# Prepare data for writing dates by numbers and words
def print_dates():
    # if len(months_log) == 12:
    #     months_log.clear()
    # if len(centuries_log) == 3:
    #     centuries_log.clear()

    # Choose random month
    # month = core.new_randint(1, 12, months_log)
    month = core.unique_rnd(1, 12, random_months)

    # Value str_month is for writing a date in a short format
    # Add zero in the begin if day < 10
    if month < 10:
        str_month = '0' + str(month)
    else:
        str_month = str(month)

    # Generate random day. Take max value from months_dict
    # day = core.new_randint(1, months_dict['days'][month - 1], days_log)
    day = core.unique_rnd(1, months_dict['days'][month - 1], random_days)

    # Convert day to German ordinal
    day_words = int_to_ordinal(day)

    # Choose century avoiding repeats
    # century_index = core.new_randint(0, 2, random_centuries)
    century_index = core.unique_rnd(0, 2, random_centuries)
    (min_year, max_year) = centuries[century_index]

    # Generate random year
    # year = core.new_randint(min_year, max_year, years_log)
    year = core.unique_rnd(min_year, max_year, random_years)

    # There are two ways how to write years in German. It depends on century
    if year > 1999:
        year_words = core.int_to_german(year)
    else:
        year_first_part = int(str(year)[:2])
        year_second_part = int(str(year)[2:])
        year_words = core.int_to_german(year_first_part) + 'hundert' + core.int_to_german(year_second_part)

    # DD.MM.YYYY
    short_date = f'{day}.{str_month}.{year}'

    # Russian format
    russian_date = f'{day} {months_dict["russian"][month - 1]} {year} г.'

    # American format
    english_date = f'{months_dict["english"][month - 1]} {day}, {year}'

    # German format with numbers
    german_date = f'{day}. {months_dict["german"][month - 1]} {year}'

    # The entire date is written by german words
    german_date_words = f'{day_words} {months_dict["german"][month - 1]} {year_words}'

    # Output
    result = f'{short_date} / {english_date}\n' \
             f'   {russian_date}\n' \
             f'   German:\n' \
             f'   {german_date}\n' \
             f'   {german_date_words}\n'
    return result


# Run simple console interface which show random content with user's parameters
core.show(print_dates, 'dates')



