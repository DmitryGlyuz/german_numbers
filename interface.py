
def input_int(prompt, min_n, max_n):
    number = 0
    while number < min_n or number > max_n:
        try:
            number = int(input(prompt))
        except:
            print('Error. Try again')
    return number


def generator(func, things, show_second_list=False, min_num=1, max_num=30, second_list_header=''):
    second_list = [] if show_second_list is True else None
    num_of_outputs = input_int(f'Enter the number of {things} (from {min_num} to {max_num}): ', min_num, max_num)
    for i in range(1, num_of_outputs + 1):
        print(f'{i}. {func()[0]}')
        if show_second_list is True:
            second_list.append(func()[1])
    if show_second_list is True:
        print(second_list_header)
        for line in second_list:
            print(f'{second_list.index(line) + 1}. {line}')

