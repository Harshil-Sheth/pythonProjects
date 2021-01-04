import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('DAMN!!! You are genius')
            return True
    else:
        print('I said 1~10 ONLY!!!!')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('PLEASE ENTER A NUMBER FOR A GOD\'S SAKE')
            continue
