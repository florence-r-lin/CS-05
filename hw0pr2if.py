# coding: utf-8
#
# hw0pr2if.py
#

""" 
Title for your adventure:   Sweet factory.

Notes on how to explore adventure: choose your favorite of each item!
"""

import time

def adventure():

    #own story

    name = input("Hello what is your name? Today we are going on a tour of a sweets factory")
    print()
    print("Hello,", name, " to the sweets factory. I hope you have fun today!")
    print()

    #if elif and else
    flavor = input("We will first tour the icecream section. What is your favorite flavor?")
    if flavor == "strawberry":
        print("Yuck. I don't like strawberry")
    elif flavor == "chocolate":
        print("oooo yummy. well chosen!")
    else:
        print("oh. I guess thats alright")
    print()
    print()

    #if, elif, elif, ... and else
    cupcake = input("We will now tour the cupcake section. What is your favorite flavor?")
    if cupcake == "strawberry":
        print("Yuck. I don't like strawberry")
    elif cupcake == "chocolate":
        print("I love chocolate!")
    elif cupcake == "vanilla":
        print("wow thats classic!")
    else:
        print("right. we have so many other flavors to choose from here!")
    print()
    print()

    #if, else
    foundue = input("Do you like foundue? Yes or no?")
    if foundue == "yes":
        print("So yummm. I love foundue too! We have so many types of chocolate fondues for you")
    else:
        print("why are you here then")
    print()
    print()

    #if
    fun = input("Did you have fun touring the factory?")
    if fun != "no":
        print("I had so much fun being your tour guide today! I hope you come back")


