import core

# Simple interface where we can check how our function works
# Enter any non-Int to exit
print('Enter any integer number to get it in German.\nEnter any non-integer to exit.')
while True:
    try:
        n = int(input('\nNumber: '))
        print(f'German: {core.GermanNumeral(n)}')
    except ValueError:
        print('Tschüss!')
        exit()
