timeout = None

from Words import word_lis
import random
import time
from Coloring import set_green, set_yellow, set_grey

answer = list(random.choice(word_lis))


def test(answer, tries=0, win=0, attempt=1, win_attempts={'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}, again=True):
    if again == False:
        return
    if tries == 6:
        print('Wrong')
        time.sleep(2)
        print('Sorry You Suck!')
        print('Correct answer was', end=' ')
        for i in range(5):
            print(answer[i], end='')
        print()
        print()
        time.sleep(2)
        response = input('Would you like to play again?(Y/N):')
        print()
        if response.upper() == 'Y':
            attempt += 1
            return test(list(random.choice(word_lis)), 0, win, attempt=attempt)
        else:
            print(f'\nYour Win Percent Is: %{int(100 * (win / (attempt + 1))):.2f}')
            return
    guess = list(input(f'Enter A Five Letter Guess(Attempt #{tries + 1}): ').upper())
    lis = [' ', ' ', ' ', ' ', ' ']
    check = answer.copy()
    green = 0

    try:
        for i in range(5):
            if check[i] == guess[i]:
                lis[i] = set_green(guess[i])
                check[i] = ' '
                green += 1

        for i in range(5):
            if guess[i] in check and lis[i] == ' ':
                check[check.index(guess[i])] = ' '
                lis[i] = set_yellow(guess[i])
        for i in range(5):
            if lis[i] == ' ':
                lis[i] = set_grey(guess[i])
        print(*lis)
        print()
    except IndexError:
        print('Answer Must Be Five Letters!')
        print('Try Again')
        test(answer, tries, win, attempt)
    if green == 5:
        win_attempts[str(tries + 1)] = win_attempts[str(tries + 1)] + 1
        win += 1
        time.sleep(2)
        print()
        print(f'{"WINNER":^75}')
        print()
        time.sleep(1)
        print('\nWin Distribution')
        for i in win_attempts:
            print(i, '|' + str(win_attempts[i] * '️🟩'))
        print()
        while again == True:
            response = input('Would you like to play again?(y/n):').upper()
            print()
            if response == 'Y' or response == 'YES':
                return test(list(random.choice(word_lis)), 0, win, attempt + 1)
            elif response == 'N' or response == 'NO':
                print(f'\nYour Win Percent Is: %{100 * (win / (attempt)):.2f}')
                again = False
                return again
            else:
                print('Invalid Response')
    else:
        test(answer, tries + 1, win, attempt)


test(list(random.choice(word_lis)))