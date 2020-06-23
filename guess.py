# This is a guess the number game - You can change the range and max guesses allowed
# Plans: Test this from shell execution

import random
import sys

def intInput():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print('Error: You did not enter a valid number.')
            continue

def play(settings):
    print('I am thinking of a number between ' + str(settings[0]) + ' and ' + str(settings[1]) + '.')
    secretNumber = random.randint(settings[0], settings[1])

    guessesTaken = 0
    while True:
        print('Take a guess.')
        guess = intInput()
        if guess < settings[0]  or guess > settings[1]: # If the guess is not in range, it doesn't count and the user must guess again
            print('That number is not in between ' + str(settings[0]) + ' and ' + str(settings[1]) + ', try again.')
            continue
        guessesTaken += 1
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # This condition is for the correct guess!
        if guessesTaken >= settings[2]:
            break # This condition is if the guess limit has been reached

    if guess == secretNumber:
        print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
    return None

def setSettings():
    while True:
        print('Please enter a low value.')
        lowest = intInput()
        print('Please enter a high value.')
        highest = intInput()
        print('Please enter the max number of guess you would like.')
        maxGuesses = intInput()
        if lowest > highest or maxGuesses < 1:
            print("Something isn't right, your lowest(" + str(lowest) + ") cannot be greater than your highest(" + str(highest) + ") and your max guesses(" + str(maxGuesses) + ") must be at least 1.")
        else:
            return (lowest, highest, maxGuesses)

if __name__ == "__main__":
    print('Hello. What is your name?')
    name = input()

    #Settings variables, hardcoded for default, tuple (lowest, highest, maxGuesses)
    settings = (1, 20, 6)

    while True:
        print('Well, ' + name + ', what would you like to do? Enter a number: (1) Play, (2) Change settings, or (0) Quit')
        action = intInput()
        if action == 0:
            print('Goodbye!')
            sys.exit(0)
        elif action == 1:
            play(settings)
            print("That was fun, let's play again!")
        elif action == 2:
            settings = setSettings()
            print('Settings have been updated: Low value=' + str(settings[0]) + ', High value=' + str(settings[1]) + ', Max guesses=' + str(settings[2]))
        else:
            print('Action not found')
