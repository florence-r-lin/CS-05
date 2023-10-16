# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Florence Lin
# Problem description: Sleepwalking student

import random  

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])


import time

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)


import sys

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge
    """

    """ Welcome to rwsteps hangry student who wants boba edition. 
        The hangry student doesn't know where to go and is just wandering around right now.
        If the hangry student makes it all the way to the right
        they will recieve boba after their long calculus class!
        If the hangry student wanders to the left
        they accidentally wandered all the way to Pomona's campus and did not recieve boba today :(
    """

    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our hungry student's location, start-low

    walkway = walkway[:S] + "૮₍ ˃ ⤙ ˂ ₎ა" + walkway[S:]  # put our hungry student, "૮₍ ˃ ⤙ ˂ ₎ა", there

    walkway = "(>•<)💭🧋" + walkway + "(≧▽≦)🧋🧁🍡🧃🍨🧋ᰔ"              # yummy food on right, no food on left

    print(walkway)     # print everything to keep track...
    time.sleep(0.05)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!



def bobaRace(playerA, playerB, BOBA):
    """
        This simulator includes playerA and playerB who are trying to find the last free boba
        avaiable on campus at the Women in Math social

        playerA:  the location of the first student (who wanders), always starts on the left side of campus
        playerB:  the location of the second student (who wanders), always starts on the right side of campus  
        BOBA:  3rd floor SHAN

        The last free boba is on the table at 3rd floor SHAN.
        The endpoints are always at low=0 and hi=50.  (We don't need them as inputs)
   
        Good values to run:  bobaRace( 10, 20, 15)  # evenly spaced
        bobaRace( 5, 30, 25 )  #  spacing: playerB is much closer to the BOBA!
        """ 

    walkway = "_"*(50)
    walkway = walkway[0:playerA] + "(>•<)💭🧋" + walkway[playerA:BOBA] + "🧋🧋🧋🧋🧋" + walkway[BOBA:playerB] + "(>•<)💭🧋" + walkway[playerB:50]


    print(walkway, "    ", playerA, playerB, BOBA)
    time.sleep(0.05)


    if playerA <= 0 or playerA > BOBA:
        print("oh no! student A got lost, student B got the free boba!")
        return 0
    if playerB >= 50 or playerB < BOBA:
        print("oh no! student B got lost, student A got the free boba!")
        return 0
    if playerA == BOBA:
        print("Student A got the boba!")
        return 0
    if playerB == BOBA:
        print("Student B got the boba!")
        return 0
    else:
        A = playerA + rs()
        B = playerB + rs()       
        return 1 + bobaRace(A, B, BOBA)  

    """
    In [14]: bobaRace( 5, 30, 25 )
    _____(>•<)💭🧋____________________🧋🧋🧋🧋🧋_____(>•<)💭🧋____________________      5 30 25
    ____(>•<)💭🧋_____________________🧋🧋🧋🧋🧋____(>•<)💭🧋_____________________      4 29 25
    _____(>•<)💭🧋____________________🧋🧋🧋🧋🧋_____(>•<)💭🧋____________________      5 30 25
    ____(>•<)💭🧋_____________________🧋🧋🧋🧋🧋______(>•<)💭🧋___________________      4 31 25
    _____(>•<)💭🧋____________________🧋🧋🧋🧋🧋_______(>•<)💭🧋__________________      5 32 25
    ____(>•<)💭🧋_____________________🧋🧋🧋🧋🧋______(>•<)💭🧋___________________      4 31 25
    ___(>•<)💭🧋______________________🧋🧋🧋🧋🧋_____(>•<)💭🧋____________________      3 30 25
    __(>•<)💭🧋_______________________🧋🧋🧋🧋🧋____(>•<)💭🧋_____________________      2 29 25
    _(>•<)💭🧋________________________🧋🧋🧋🧋🧋_____(>•<)💭🧋____________________      1 30 25
    (>•<)💭🧋_________________________🧋🧋🧋🧋🧋____(>•<)💭🧋_____________________      0 29 25
    oh no! student A got lost, student B got the free boba!
    Out[14]: 9 

    In [4]: bobaRace( 10, 20, 15)
    __________(>•<)💭🧋_____🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      10 20 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      11 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      13 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      13 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋__(>•<)💭🧋_________________________________      11 17 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      11 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      12 20 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋______(>•<)💭🧋_____________________________      11 21 15
    __________(>•<)💭🧋_____🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      10 20 15
    _________(>•<)💭🧋______🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      9 19 15
    ________(>•<)💭🧋_______🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      8 20 15
    _________(>•<)💭🧋______🧋🧋🧋🧋🧋______(>•<)💭🧋_____________________________      9 21 15
    __________(>•<)💭🧋_____🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      10 20 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋______(>•<)💭🧋_____________________________      11 21 15
    __________(>•<)💭🧋_____🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      10 20 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋______(>•<)💭🧋_____________________________      11 21 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋_____(>•<)💭🧋______________________________      12 20 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      13 19 15
    ______________(>•<)💭🧋_🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      14 18 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      13 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋____(>•<)💭🧋_______________________________      11 19 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋__(>•<)💭🧋_________________________________      13 17 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋___(>•<)💭🧋________________________________      12 18 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋__(>•<)💭🧋_________________________________      13 17 15
    ______________(>•<)💭🧋_🧋🧋🧋🧋🧋_(>•<)💭🧋__________________________________      14 16 15
    _____________(>•<)💭🧋__🧋🧋🧋🧋🧋__(>•<)💭🧋_________________________________      13 17 15
    ____________(>•<)💭🧋___🧋🧋🧋🧋🧋_(>•<)💭🧋__________________________________      12 16 15
    ___________(>•<)💭🧋____🧋🧋🧋🧋🧋(>•<)💭🧋___________________________________      11 15 15
Student B got the boba!
Out[4]: 33


"""