# In this document I will write a python code to play rock,paper,scissors

import sys
import random


#Getting an the input of users

def yourChoice():
    print("Press 'R' for Rock.")
    print("Press 'P' for Paper.")
    print("Press 'S' for Scissors.")
    print("Press 'Q' to Quit.")
    #print("Press 'X' for Score reset.")   <-- for a later implementation of scorepoints if the simple program works
    
    user_choice = input("What do you wanna choose?").lower()

    if user_choice == "r":
        return "Rock"
    elif user_choice == "p":
        return "Paper"
    elif user_choice == "s":
        return "Scissors"
    elif user_choice == "q":
        sys.exit(0)
    else:
        yourChoice()


#Random Choice of the python programm

def pythonRandom():
    rps = ["Rock", "Paper", "Scissors"]
    randChoice = random.randint(0,2)
    return rps[randChoice]

#Comparison of the users input and the random choice of the python program

def






