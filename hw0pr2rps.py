# coding: utf-8
#
# hw0pr2rps.py
#

import random          # imports the library named random

def rps():
    """This plays a game of rock-paper-scissors
       (or a variant of that game)
       Arguments: none     (prompted text doesn't count as an argument)
       Results: none       (printing doesn't count as a result)
    """
    user = input("Choose your weapon: ")
    comp = random.choice(['rock', 'paper', 'scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', comp)
    print()

    if user == 'rock' and comp == 'scissors':
        print('Uh oh.. you crushed my scissors..')

    elif user == 'rock' and comp == 'paper':
        print('My paper beat your rock')

    elif user == 'rock' and comp == 'rock':
        print('We tied! Play me again! I also chose rock')

    elif user == 'scissors' and comp == 'paper':
        print('Oh no! you won! You cut up my paper')

    elif user == "scissors" and comp == 'scissors':
        print('We tied! Play me again!I also chose scissors')
    
    elif user == "scissors" and comp == "rock":
        print('I won hehe. too bad. My rock crushed ur scissors')
    
    elif user == "paper" and comp == 'scissors':
        print('I won too bad for you. I cut up ur paper with scissors')
    
    elif user == "paper" and comp == 'rock':
        print('ugh you won.. your paper beats my rock')
    
    else :
        print('We tied! play again? I also chose paper')


