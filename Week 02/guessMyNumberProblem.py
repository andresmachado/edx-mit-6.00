# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

high = 100
low = 0
possible = ['h', 'l', 'c']
ans = ''
guessing = True

print('Please think of a number between {} and {}!\n'.format(low, high))
while guessing:
    guess = (low + high) // 2
    print("Is your secret number {}?\n".format(guess))
    ans = input("Enter 'h' to indicate the guess is too high."
                "Enter 'l' to indicate the guess is too low."
                "Enter 'c' to indicate I guessed correctly: ")
    if ans not in possible:
        print('Sorry, I did not understand your input\n')
    else:
        if ans == 'h':
            high = guess
        elif ans == 'l':
            low = guess
        else:
            print('Game over. Your secret number was: ', guess)
            break