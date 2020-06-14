from german_numbers import int_to_german
import random
import interface

ord_numbers_dict = {
    1: 'erste',
    2: 'zweite',
    3: 'dritte',
    7: 'siebte',
    8: 'achte',

}

months_dict ={
'days': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
'english': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
'german': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
'russian': ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
}


# Перевод обычного числительного в виде строки с немецкими словами в порядковое
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


def print_dates():
    month = random.randint(1, 12)
    if month < 10:
        str_month = '0' + str(month)
    else:
        str_month = str(month)
    day = random.randint(1, months_dict['days'][month - 1])
    day_words = int_to_ordinal(day)
    year = random.randint(1800, 2036)
    if year > 1999:
        year_words = int_to_german(year)
    else:
        year_first_part = int(str(year)[:2])
        year_second_part = int(str(year)[2:])
        year_words = int_to_german(year_first_part) + 'hundert' + int_to_german(year_second_part)
    short_date = f'{day}.{str_month}.{year}'
    russian_date = f'{day} {months_dict["russian"][month - 1]} {year} г.'
    german_date = f'{day}. {months_dict["german"][month - 1]} {year}'
    german_date_words = f'{day_words} {months_dict["german"][month - 1]} {year_words}'
    result = f'{short_date}\n' \
             f'   {russian_date}\n' \
             f'   {german_date}\n' \
             f'   {german_date_words}\n'
    return (result, None)


interface.generator(print_dates, 'dates')



