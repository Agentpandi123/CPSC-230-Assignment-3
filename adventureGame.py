'''The player starts at the entrance to the castle. They are then asked what room they would like to visit. When they visit that room, 
a brief description of the room and what they found there is printed, and then they are asked to choose another room to visit next. If 
they player chooses to visit the exit, then the game ends. Similarly, if the player finds the treasure in a room, the game ends. You 
may have as many rooms as you like, within the following constraints: 1) You must have at least 6 rooms 2) Not every room is reachable 
from every other room. 3) The game must have several alternative endings.'''

import random

X = str(input("You are at an entrance to a castle. There are two rooms in front of you. Do you want to go to the left or right room: "))
# This program is literally just way too many if else statements

while X != "left" or "right": # can't have a different answer then left or right
    X = str(input("You need to choose either left or right: "))
    if X == "left":
        A = random.randint(1,10) #random number
        if A == 5:
            print("Bad Luck. You died.") # if the random number is 50, you die
            exit() # Without exit it becomes an infinte loop
        Y = str(input("You walk into the left room. This room is just a hallway and has nothing in it. You see 2 different rooms in front of you (One left and one right). Choose one: "))
        while Y != "left" or "right": # can't have a different answer then left or right
            Y = str(input("You need to choose either left or right: "))
            if Y == "left": # End of path where you die
                print("You walk into the left room.  This room has a dragon in it and you die.")
                exit() # Without exit it becomes an infinte loop
            elif Y == "right":
                A = random.randint(1,10) #random number
                if A == 5:
                    print("Bad Luck. You died.") # if the random number is 50, you die
                    exit() # Without exit it becomes an infinte loop
                Z = str(input("You walk into the right room.  This is a room full of food.  You take a minute to eat and stock up on food. Then you see a path in front of you with two doors.  Choose either the left or right one: "))
                while Z != "left" or "right": # can't have a different answer then left or right
                    Z = str(("You need to choose either left or right: "))
                    if Z == "left": # End of path where you die
                        print("You walk into the left room. You walk into the dungeon where the prisoners kill you and eat your body")
                        exit() # Without exit it becomes an infinte loop
                    elif Z == "right": # End of path where you live, but don't get anything
                        print("You go into the right room. You find the stables and take a horse for your escape. You escape the castle with a big bag of food.")
                        exit() # Without exit it becomes an infinte loop
    elif X =="right":
        A = random.randint(1,10) #random number
        if A == 5:
            print("Bad Luck. You died.") # if the random number is 50, you die
            exit() # Without exit it becomes an infinte loop
        Y = str(input("You walk into the right room.  You find a gun then you see 2 different rooms in front of you (One left and one right). Choose one: "))
        while Y != "left" or "right": # can't have a different answer then left or right
            A = random.randint(1,10) #random number
            if A == 5:
                print("Bad Luck. You died.") # if the random number is 50, you die
                exit() # Without exit it becomes an infinte loop
            Y = str(input("You need to choose either left or right: "))
            if Y == "left":
                Z = str(input("You walk into the left room. You are faced with soldiers, but you defeat them with your gun. You find a key to the treasure and see a path before you.  Choose either left, right, or middle: "))
                while Z != "left" or "right" or "middle": # can't have a different answer then left or right or middle
                    Z = str(input("You need to choose either left or right or middle: "))
                    if Z == "left": # End of path where you are trapped
                        print("You walk into the left room. The door shuts behind you and you're now trapped. Soldiers walk towards you and let you rot in there to die.")
                        exit() # Without exit it becomes an infinte loop
                    elif Z == "right": # End of path where you die
                        print("You walk into the right room. This room has a dragon and you die. Your gun is useless against it.")
                        exit() # Without exit it becomes an infinte loop
                    elif Z == "middle": # YOU FOUND THE TREASURE + GOOD ENDING
                        print("You found the room with the treasure and you escape with a lot of riches.")
                        exit() # Without exit it becomes an infinte loop
            elif Y == "right": # You live, but no treasure
                print("You walk into a mysterious room and see the moat of the castle. You find a boat and escape with nothing but a gun in hand.")
                exit() # Without exit it becomes an infinte loop
