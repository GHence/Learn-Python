'''
 分支和函数

 -----------------------------测试用例--------------------------------------
 D:\software\python\python.exe E:/dev/code/笨方法学python3/ex35.py
You are in a dark room.
There is a door to you right and left.
Which one do you take?
> left
There is bear here.
The bear has a bunch of honey.
The bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has move from the door
You can go through it now.
> open door
This room is full of gold. How much do you take?
> 23
Man,learn to type a number. Good job!

'''
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man,learn to type a number.")

    if how_much < 50:
        print("Nice,you're not greedy,you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is bear here.")
    print("The bear has a bunch of honey.")
    print("The bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you the slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has move from the door")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the greet evil Cthulhu.")
    print("He,it,whatever stares at you and you go instance.")
    print("Do you flee for your life or eat you head.")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was testy!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to you right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
