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
import datetime


class Date:
    """' Contains the date, its components, and all the logic for output in the required form """
    class Day(int):
        """ Contains a dictionary with ordinal form of numbers and method which converts integers to German ordinals"""
        # Dictionary with ordinal numbers in German
        ordinal_numbers = {
            1: 'erste',
            2: 'zweite',
            3: 'dritte',
            7: 'siebte',
            8: 'achte',
        }

        def __init__(self, value):
            super().__init__()
            self.value = value

        # Returns German ordinal number
        def german(self):
            if 1 <= self.value <= 19:
                # Take directly from a dictionary
                if self.value in self.ordinal_numbers.keys():
                    ord_number = self.ordinal_numbers[self.value]
                # Or do simple transformation
                else:
                    ord_number = f'{core.GermanNumeral(self.value)}te'
            elif 20 <= self.value <= 31:
                ord_number = f'{core.GermanNumeral(self.value)}ste'
            # We work only with numbers which could be a day in month: 1- 31
            else:
                raise ValueError
            return 'der ' + ord_number

    class Month(int):
        """ Contains lists of months to get translation and info about number of days included in month"""
        month_lists = [
            # Number of days in each month
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            # English
            ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December'],
            # German
            ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober',
             'November', 'Dezember'],
            # Russian
            ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
             'ноября', 'декабря']
        ]

        def __init__(self, value):
            super().__init__()
            self.value = value
            self.position = value - 1

            # Take few attributes from month_lists
            self.days_number, self.english, self.german, self.russian = [lst[self.position] for lst in self.month_lists]

        # This method is used for show month as a part of some date in format DD.MM.YYYY
        def __str__(self):
            return f'0{self.value}' if self.value < 10 else str(self.value)

    class Year(int):
        def __init__(self, value):
            super().__init__()
            self.value = value

        def german(self):
            """ Objects of this class store a year and have a method which show these year in German """
            # There are two ways how to write the date in German: For 21st century and before
            if self.value > 1999:
                return core.GermanNumeral(self.value)
            else:
                first_part = self.value // 100
                second_part = self.value % 100
                return f'{core.GermanNumeral(first_part)}hundert' \
                       f'{core.GermanNumeral(second_part) if second_part > 0 else ""}'

    class Century(int):
        # Dictionary with centuries, and the years included in them
        centuries_dict = {
            19: (1800, 1899),
            20: (1900, 1990),
            21: (2000, 2030)
        }

        def __init__(self, value):
            super().__init__()
            self.value = value
            # Take range of years from dictionary
            self.min, self.max = self.centuries_dict[value]

    def __init__(self, day=1, month=1, year=2000, century=21, get_random=False, get_today=False):
        # Data object can take custom values or generate randoms or current date
        if get_random:
            self.month = self.Month(core.unique_randint(1, 12, 'months'))
            self.day = self.Day(core.unique_randint(1, self.month.days_number, 'days'))
            self.century = self.Century(core.unique_randint(19, 21, 'centuries'))
            self.year = self.Year(core.unique_randint(self.century.min, self.century.max, 'years'))
        elif get_today:
            self.today = datetime.date.today()
            self.day = self.Day(self.today.day)
            self.month = self.Month(self.today.month)
            self.year = self.Year(self.today.year)
        else:
            self.day = self.Day(day)
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

    # Returns a string with a date in several formats defined in the parameters. All formats by default
    def in_format(self, short=True, us=True, ru=True, short_de=True, de=True):
        # Function using in f-string. Returns specified value or mpt depends on selected mode
        def optional_out(mode, val, tab=False):
            return f'{"   " if tab else ""}{val if mode else ""}'

        # The same for new line
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
    dates_list = [Date(get_today=True).in_format(**kwargs)]
    if count > 1:
        dates_list += [Date(get_random=True).in_format(**kwargs) for _ in range(count - 1)]
    return core.get_lines(dates_list)


# Command line interface
if __name__ == '__main__':
    dates_list = get_data(cli.number_of_points('dates', 1, 100))
    print(dates_list)
    cli.save_file(dates_list, 'dates.txt')
