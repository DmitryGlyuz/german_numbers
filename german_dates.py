# This script generates random dates in German

from german_numbers import int_to_german
import random
import interface

# Dictionary with ordinal numbers in German
ord_numbers_dict = {
    1: 'erste',
    2: 'zweite',
    3: 'dritte',
    7: 'siebte',
    8: 'achte',

}

# This dictionary contains the number of days in each mouth and names of months in English, German and Russian
months_dict ={
'days': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
'english': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
'german': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
'russian': ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
}


# Convert natural integer to German ordinal number and return with a prefix 'der'
def int_to_ordinal(number):
    if 1 <= number <= 19:
        if number in ord_numbers_dict.keys():
            ord_number = ord_numbers_dict[number]
        else:
            ord_number = int_to_german(number) + 'te'
    elif 20 <= number <= 31:
        ord_number = int_to_german(number) + 'ste'
    else:
        raise ValueError
    return 'der ' + ord_number


# Prepare data for writing dates by numbers and words
def print_dates():
    # Choose random month
    month = random.randint(1, 12)

    # Value str_month is for writing a date in a short format
    # Add zero in the begin if day < 10
    if month < 10:
        str_month = '0' + str(month)
    else:
        str_month = str(month)

    # Generate random day. Take max value from months_dict
    day = random.randint(1, months_dict['days'][month - 1])

    # Convert day to German ordinal
    day_words = int_to_ordinal(day)

    # Generate random year
    year = random.randint(1800, 2036)

    # There are two ways how to write years in German. It depends on century
    if year > 1999:
        year_words = int_to_german(year)
    else:
        year_first_part = int(str(year)[:2])
        year_second_part = int(str(year)[2:])
        year_words = int_to_german(year_first_part) + 'hundert' + int_to_german(year_second_part)

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
interface.generator(print_dates, 'dates')



