from random import randint
import sys
try:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
except IndexError:
    try:
        first = int(input('Enter the starting number: '))
        second = int(input('Enter the ending number: '))
    except ValueError:
        print('Please enter number only')
finally:
    random_num = randint(first, second)
    # print(f'number to guess is {random_num}') #for testing if needed to know the number to be guessed
while True:
    try:
        guess_num = int(
            input(f'\n Make a guess between {first} and {second}: '))
    except ValueError:
        print('\n Input a number and not string')
        continue
    if guess_num <= second and guess_num >= first:
        if guess_num == random_num:
            print('\n You guessed correctly')
            break
        print('\n Incorrect guess!! Try Again')
    else:
        print(
            f' \n Enterr a number between {first} and {second} numbers')
