# Input integer and repeat if something goes wrong
def input_int(prompt, min_n, max_n):
    def print_error(message):
        print(f'Error: {message}. Try again.')

    number = 0
    while number < min_n or number > max_n:
        try:
            number = int(input(prompt))
            if number < min_n:
                print_error(f'Yor number less than {min_n}')
            elif number > max_n:
                print_error(f'Your number more than {max_n}')
        except ValueError:
            print_error('That is not integer value')
    return number


# This function shows random content from another modules
def generator(func, things, show_second_list=False, min_num=1, max_num=30, second_list_header=''):
    if show_second_list is True:
        second_list = []
        first_output = func()[0]
    else:
        first_output = func()

    # Enter the number of things to prtint
    num_of_outputs = input_int(f'Enter the number of {things} (from {min_num} to {max_num}): ', min_num, max_num)

    # Output
    for i in range(1, num_of_outputs + 1):
        print(f'{i}. {first_output}')
        if show_second_list is True:
            second_list.append(func()[1])

    # Print separated list
    if show_second_list is True:
        print(second_list_header)
        for line in second_list:
            print(f'{second_list.index(line) + 1}. {line}')

