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

month_lists = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December'],
    ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
                   'November', 'Dezember'],
    ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                    'ноября', 'декабря']
]


class Date:
    class Day(int):
        def __init__(self, value):
            self.value = value

        def german(self):
            if 1 <= self.value <= 19:
                if self.value in ord_numbers_dict.keys():
                    ord_number = ord_numbers_dict[self.value]
                else:
                    ord_number = f'{core.GermanNumeral(self.value)}te'
            elif 20 <= self.value <= 31:
                ord_number = f'{core.GermanNumeral(self.value)}ste'
            else:
                raise ValueError
            return 'der ' + ord_number

    class Month(int):
        def __init__(self, value):
            self.value = value
            self.position = value - 1
            self.days_number, self.english, self.german, self.russian = [lst[self.position] for lst in month_lists]

        def __str__(self):
            return f'0{self.value}' if self.value < 10 else str(self.value)

    class Year(int):
        def __init__(self, value):
            self.value = value

        def german(self):
            if self.value > 1999:
                return core.GermanNumeral(self.value)
            else:
                return f'{core.GermanNumeral(self.value // 100)}hundert{core.GermanNumeral(self.value % 100)}'

    def __init__(self, day, month, year):
        self.day = self.Day(day)
        self.month = self.Month(month)
        self.year = self.Year(year)

    # Returns a string value with a date in the format DD.MM.YYYY
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    # Returns a string value with a date in Russian format
    def russian(self):
        return f'{self.day} {self.month.russian} {self.year} г.'

    # Returns a string value with a date in US format
    def american(self):
        return f'{self.month.english} {self.day}, {self.year}'

    # Returns a string value with a date in German format
    def short_german(self):
        return f'{self.day}. {self.month.german} {self.year}'

    # Returns a string value with a date written by German words
    def german(self):
        return f'{self.day.german()} {self.month.german} {self.year.german()}'

    def in_format(self, short=True, us=True, ru=True, short_de=True, de=True):
        def optional_out(mode, val, tab=False):
            return f'{"   " if tab else ""}{val if mode else ""}'

        def new_line(mode):
            return "\n" if mode else ""

        return f'{optional_out(short, self.__str__())}' \
               f'{optional_out((short and us), " / ")}' \
               f'{optional_out(us, self.american())}' \
               f'{new_line((short or us))}' \
               f'{optional_out(ru, self.russian(), tab=short)}' \
               f'{new_line((ru and short_de))}' \
               f'{optional_out(short_de, self.short_german(), tab=short)}' \
               f'{new_line((short_de and de))}' \
               f'{optional_out(de, self.german(), tab=short)}\n'


class Century(int):
    # Dictionary with for centuries, and the years included in them
    centuries_dict = {
        19: (1800, 1899),
        20: (1900, 1990),
        21: (2000, 2030)
    }

    def __init__(self, value):
        self.value = value
        self.min, self.max = self.centuries_dict[value]


# Lists where already used values are placed so that they are not repeated
# days_log = []
# months_log = []
# years_log = []
# centuries_log = []


# Returns Date object with random values
def random_date():
    # Choose number with random month
    month = core.unique_randint(1, 12, 'months')

    # Generate random day. Take max value from months_dict
    day = core.unique_randint(1, Date.Month(month).days_number, 'days')

    # Choose century avoiding repeats and define range of years
    century = Century(core.unique_randint(19, 21, 'centuries'))

    # Generate random year
    year = core.unique_randint(century.min, century.max, 'years')
    return Date(day, month, year)


# Returns string value with random dates written in few formats described at the beginning of the file
def get_data(count, **kwargs):
    dates = []
    for i in range(count):
        dates.append(random_date().in_format(**kwargs))
    return core.get_lines(dates)


# Command line interface
if __name__ == '__main__':
    # Input required number of examples
    # number_of_dates = cli.number_of_points('dates', 1, 100)
    # Print these days
    # print(get_data(number_of_dates))
    print(get_data(5))

