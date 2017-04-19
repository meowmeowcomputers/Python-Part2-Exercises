import random
guess = random.randint(1, 100)
yn = 'n'
guessCount = 0

while yn == 'n':
    yn = input('Is {0} your number? (y/n) '.format(guess))
    if yn == 'n':
        hilo = input('Is your number higher or lower than my guess? (hi/lo) ')
        if hilo == 'hi':
            guess = random.randint(guess, 100)
        elif hilo == 'lo':
            guess = random.randint(1, guess)
        else:
            print('Gotta enter hi or lo')
        guessCount += 1

    elif yn == 'y':
        print("Glad I got it! It only took {0} tries!".format(guessCount))

    else:
        print('Please input y or n')
        yn = 'n'
