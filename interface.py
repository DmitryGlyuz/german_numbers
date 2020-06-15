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
def generator(func, things, show_second_list=False, second_list_header='', min_num=1, max_num=30):
    # Enter the number of things to prtint
    num_of_outputs = input_int(f'Enter the number of {things} (from {min_num} to {max_num}): ', min_num, max_num)

    # Output
    second_list = [] if show_second_list is True else None
    print()
    for i in range(1, num_of_outputs + 1):
        if show_second_list is True:
            (first_out, second_out) = func()
            second_list.append(second_out)
        else:
            first_out = func()
        print(f'{i}. {first_out}')

    # Print separated list
    if show_second_list is True:
        print(f'\n{second_list_header}')
        for line in second_list:
            print(f'{second_list.index(line) + 1}. {line}')

