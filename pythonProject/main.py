from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input('Guess a number 1~10 : '))
        if 0 < guess < 11:
            if guess == answer:
                print('Damn!!! You are Genius')
                break
        else:
            print('Please enter a number 1~10 only!!!!')
    except ValueError:
        print('Please enter a number')
        continue
