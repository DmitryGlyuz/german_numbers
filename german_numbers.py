import core

# Simple interface where we can check how our function works
# Enter any non-Int to exit
if __name__ == '__main__':
    while True:
        try:
            n = int(input('Number: '))
            print(core.int_to_german(n))
        except ValueError:
            print('Tschüss!')
            exit()

