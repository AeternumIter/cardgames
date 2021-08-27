import time
import os
a = 0

os.system("cls")

def clear():
    os.system("cls")

def chipcount(pot):
    i = 0
    while i < PlayerNum:
        print(players[i] + " has " + str(playerchips[i]) + " chips")
        i+=1
    print("The pot contains " + str(pot))

print("Please note that this will be a simulation of Texas Hold 'Em, not any other variation of poker.")
time.sleep(5)
print("If you are unfamiliar with the rules, you must look it up, because a tutorial will not be included in this program (I would recommend this tutorial:https://playingcarddecks.com/blogs/how-to-play/texas-holdem-game-rules)")
time.sleep(5)
print("If you do not have physical poker chips or money, the program will provide you with digital chips that WILL be voided if you stop the program at any point")
print("Are you using physical poker chips? (y/n)")
while a == 0:
    chips = input("")
    if chips == "y":
        print("Digital chips will no longer be provided. If that was a mistake please restart the program.")
        a = 1
    elif chips == "n":
        print("Digital chips will be provided.")
        a = 1
    else:
        print("Not a Valid Answer. Try again")

startamount = 500
ante = 1
players = {}
playerchips = {}
i = 0
a = 0

print("How many people will be playing?")
while a == 0:
    a = 1
    PlayerNum = input("")
    PlayerNum = int(PlayerNum)
    if PlayerNum < 4:
        print("You can't play poker with that amount of players. If you typed that wrong, please try again.")
        a = 0
print("Enter the names in clockwise order")
while i < PlayerNum:
    players[i] = input("")
    playerchips[i] = startamount
    i+=1

dealer = 0
pot = 0

def nochipround():
    print("not done yet")

def virtualchipround():
    x = 0
    pot = 0
    leftblind = dealer + 1
    rightblind = dealer + 2
    clear()
    print(players[dealer] + " is the dealer")
    time.sleep(1)
    print(players[leftblind] + ", what is your initial bet (" + players[rightblind] + " will be forced to double that)")
    ibet = input("")
    playerchips[leftblind] = int((playerchips.get(leftblind))) - (int(ibet) - 1)
    playerchips[rightblind] = int((playerchips.get(rightblind))) - ((int(ibet)*2)-1)
    pot += (int(ibet) - 1)
    pot += ((int(ibet)*2)-1)

    i = 0
    while i < PlayerNum:
        playerchips[i] = (playerchips.get(i)) - ante
        pot += ante
        i+=1
    chipcount(pot)
    print("Please hand the computer to " + players[leftblind])
    print("Press enter when " + players[leftblind] + " has the computer")
    x = input("")
    





if chips == "n":
    virtualchipround()
else:
    nochipround()