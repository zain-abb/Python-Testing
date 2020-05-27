import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You are a Genius!')
            return True
        else:
            print('Try again!!!')
    else:
        print('Hey Bozo, I said 1~10!')


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError as err:
            print('Pease enter a number')
            continue
