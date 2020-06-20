# This is a guess the number game
# Plans: allow choosing the range, make out of range exception, make game a function and infinite loop "would you like to play again or quit(sys.exit())", have game bully you if you input several invalid guesses(error counter, maybe even punish you/increment guessesTaken)

import random


if __name__ == "__main__":
    print('Hello. What is your name?')
    name = input()

    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    secretNumber = random.randint(1, 20)

    guessesTaken = 0
    while True:
        print('Take a guess.')
        try:
            guess = int(input())
            if guess < 1 or guess > 20:
                raise ValueError    # I plan to make this a custom exception "Out of Range"
        except ValueError:
            print('Error: You did not enter a valid number.')
            continue
        guessesTaken += 1
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # This condition is for the correct guess!
        if guessesTaken > 6:
            break # This condition is if the guess limit has been reached

    if guess == secretNumber:
        print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
