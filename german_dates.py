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


class Date:
    """' Contains the date, its components, and all the logic for output in the required form """
    class Day(int):
        # Dictionary with ordinal numbers in German
        ord_numbers_dict = {
            1: 'erste',
            2: 'zweite',
            3: 'dritte',
            7: 'siebte',
            8: 'achte',
        }

        def __init__(self, value):
            super().__init__()
            self.value = value

        def german(self):
            if 1 <= self.value <= 19:
                if self.value in self.ord_numbers_dict.keys():
                    ord_number = self.ord_numbers_dict[self.value]
                else:
                    ord_number = f'{core.GermanNumeral(self.value)}te'
            elif 20 <= self.value <= 31:
                ord_number = f'{core.GermanNumeral(self.value)}ste'
            else:
                raise ValueError
            return 'der ' + ord_number

    class Month(int):
        month_lists = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December'],
            ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
             'November', 'Dezember'],
            ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
             'ноября', 'декабря']
        ]

        def __init__(self, value):
            super().__init__()
            self.value = value
            self.position = value - 1
            self.days_number, self.english, self.german, self.russian = [lst[self.position] for lst in self.month_lists]

        def __str__(self):
            return f'0{self.value}' if self.value < 10 else str(self.value)

    class Year(int):
        def __init__(self, value):
            super().__init__()
            self.value = value

        def german(self):
            if self.value > 1999:
                return core.GermanNumeral(self.value)
            else:
                first_part = self.value // 100
                second_part = self.value % 100
                return f'{core.GermanNumeral(first_part)}hundert' \
                       f'{core.GermanNumeral(second_part) if second_part > 0 else ""}'

    class Century(int):
        # Dictionary with for centuries, and the years included in them
        centuries_dict = {
            19: (1800, 1899),
            20: (1900, 1990),
            21: (2000, 2030)
        }

        def __init__(self, value):
            super().__init__()
            self.value = value
            self.min, self.max = self.centuries_dict[value]

    def __init__(self, day=1, month=1, year=2000, century=21, random=False):
        self.day = self.Day(day)
        if random:
            self.month = self.Month(core.unique_randint(1, 12, 'months'))
            self.day = self.Day(core.unique_randint(1, self.month.days_number, 'days'))
            self.century = self.Century(core.unique_randint(19, 21, 'centuries'))
            self.year = self.Year(core.unique_randint(self.century.min, self.century.max, 'years'))
        else:
            self.month = self.Month(month)
            self.year = self.Year(year)
            self.century = self.Century(century)

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

        return f'{optional_out(short, self.__str__())}{optional_out((short and us), " / ")}' \
               f'{optional_out(us, self.american())}' \
               f'{new_line((short or us))}' \
               f'{optional_out(ru, self.russian(), tab=short)}' \
               f'{new_line((ru and short_de))}' \
               f'{optional_out(short_de, self.short_german(), tab=short)}' \
               f'{new_line((short_de and de))}' \
               f'{optional_out(de, self.german(), tab=short)}\n'


# Returns string value with random dates written in few formats described at the beginning of the file
def get_data(count, **kwargs):
    return core.get_lines([Date(random=True).in_format(**kwargs) for _ in range(count)])


# Command line interface
if __name__ == '__main__':
    print(get_data(cli.number_of_points('dates', 1, 100)))
