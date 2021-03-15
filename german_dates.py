# This file generates string value with random dates written in few formats
# You can get them as two values from the outside via the function get_data(count, short, us, ru, short_de, de)
#       count - number of required elements
#       Next boolean variables define the output formats and are enabled by default
#       short - DD.MM.YYYY
#       us - US format
#       ru - Russian format
#       short_de - German format
#       de - everything is written as German words
import datetime

import cli
import core


class Date:
    """' Contains the date, its components, and all the logic for output in the required form """

    class Day(int):
        """ Contains a dictionary with ordinal form of numbers and method which converts integers to German ordinals"""
        # Dictionary with ordinal numbers in German
        ORDINAL_NUMBERS = {
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
                if self.value in self.ORDINAL_NUMBERS.keys():
                    ord_number = self.ORDINAL_NUMBERS[self.value]
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
        MONTHS = [
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
            self.days_number, self.english, self.german, self.russian = [lst[self.position] for lst in self.MONTHS]

        # This method is used for show month as a part of some date in format DD.MM.YYYY
        def __str__(self):
            result = str(self.value)
            if self.value < 10:
                result = '0' + result
            return result

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
                result = f'{core.GermanNumeral(first_part)}hundert'
                if second_part:
                    result += core.GermanNumeral(second_part)
                return result

    class Century(int):
        # Dictionary with centuries, and the years included in them
        CENTURIES = {
            19: (1800, 1899),
            20: (1900, 1990),
            21: (2000, 2030)
        }

        def __init__(self, value):
            super().__init__()
            self.value = value
            # Take range of years from dictionary
            self.min_year, self.max_year = self.CENTURIES[value]

    def __init__(self, day=1, month=1, year=2000, century=21, get_random=False, get_today=False):
        # Data object can take custom values or generate randoms or current date
        if get_random:
            self.month = self.Month(core.unique_randint(1, 12, 'months'))
            self.day = self.Day(core.unique_randint(1, self.month.days_number, 'days'))
            self.century = self.Century(core.unique_randint(19, 21, 'centuries'))
            self.year = self.Year(core.unique_randint(self.century.min_year, self.century.max_year, 'years'))
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
    def formatted_output(self, short='short', us='us', ru='ru', short_de='short_de', de='de'):
        output = self.__str__() if short else ''
        if us:
            output = output and output + ' / '
            output += f'{self.american()}'
        tab = '\t  ' if short else ''
        formats = {
            ru: self.russian(),
            short_de: self.short_german(),
            de: self.german()
        }
        for mode, current_format in formats.items():
            if mode:
                output += f'\n{tab}{current_format}'
        return output


# Returns string value with random dates written in few formats described at the beginning of the file
def get_data(count, **kwargs):
    dates_list = [Date(get_today=True).formatted_output(**kwargs)]
    if count > 1:
        dates_list += [Date(get_random=True).formatted_output(**kwargs) for _ in range(count - 1)]
    return core.get_lines(dates_list)


# Command line interface
if __name__ == '__main__':
    # String variable with the list of dates in all avaiale formats
    all_formats = get_data(cli.number_of_points('dates', 1, 100))

    # Print & Save to file
    print(all_formats)
    cli.save_file(all_formats, 'dates.txt')
