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

months = {
    1: {'days': 31,
        'english': 'January',
        'german': 'Januar',
        'russian': 'января'
        },
    2: {'days': 28,
        'english': 'February',
        'german': 'Februar',
        'russian': 'февраля'
        },
    3: {'days': 31,
        'english': 'March',
        'german': 'März',
        'russian': 'марта'
        },
    4: {'days': 30,
        'english': 'April',
        'german': 'April',
        'russian': 'апреля'
        },
    5: {'days': 31,
        'english': 'May',
        'german': 'Mai',
        'russian': 'мая'
        },
    6: {'days': 30,
        'english': 'June',
        'german': 'Juni',
        'russian': 'июня'
        },
    7: {'days': 31,
        'english': 'July',
        'german': 'Juli',
        'russian': 'июля'
        },
    8: {'days': 31,
        'english': 'August',
        'german': 'August',
        'russian': 'августа'
        },
    9: {'days': 30,
        'english': 'September',
        'german': 'September',
        'russian': 'сентября'
        },
    10: {'days': 31,
        'english': 'October',
        'german': 'Oktober',
        'russian': 'октября'
        },
    11: {'days': 30,
        'english': 'November',
        'german': 'November',
        'russian': 'ноября'
        },
    12: {'days': 31,
        'english': 'December',
        'german': 'Dezember',
        'russian': 'декабря'
        }
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
    day = random.randint(1, months[month]['days'])
    day_words = int_to_ordinal(day)
    year = random.randint(1800, 2036)
    if year > 1999:
        year_words = int_to_german(year)
    else:
        year_first_part = int(str(year)[:2])
        year_second_part = int(str(year)[2:])
        year_words = int_to_german(year_first_part) + 'hundert' + int_to_german(year_second_part)
    short_date = f'{day}.{str_month}.{year}'
    russian_date = f'{day} {months[month]["russian"]} {year} г.'
    german_date = f'{day}. {months[month]["german"]} {year}'
    german_date_words = f'{day_words} {months[month]["german"]} {year_words}'
    result = f'{short_date}\n' \
             f'   {russian_date}\n' \
             f'   {german_date}\n' \
             f'   {german_date_words}\n'
    return (result, None)


interface.generator(print_dates, 'dates')



