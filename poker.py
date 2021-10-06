import time
import os
import random
import sys
a = 0
d = 0
k = 0
suit = 0
suitname=0
callamount = 0
betnum = 0
spades = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hearts = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
diamonds = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
clubs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
os.system("cls")

def bet():
    playerchips[i] = int((playerchips.get(i))) - int(betnum)

def card():
    l = random.randrange(1,5)
    if l == 1:
        suit = spades
        suitname = "spades"
    elif l == 2:
        suit = hearts
        suitname = "hearts"
    elif l == 3:
        suit = diamonds
        suitname = "diamonds"
    elif l == 4:
        suit = clubs
        suitname = "clubs"
    else:
        sys.exit("ERROR")
    l = random.choice(suit)
    position = suit.index(l)
    d = str(suit[position]) + " of " + suitname
    del suit[int(position)]
    return d
    

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
    print("")
    
    i = 0
    d = dealer
    while i < PlayerNum:
        print("Please hand the computer to " + players[d])
        print("Press enter when " + players[d] + " has the computer")
        x = input("")
        clear()
        print("Your hole cards are")
        print(card())
        print(card())
        time.sleep(2)
        print("When you are done reviewing your hole cards, press enter")
        x = input("")
        clear()
        i+=1
        d+=1
    print("Pre-Flop Round starts now")
    print("")
    i = 0
    callamount = 0
    while i < PlayerNum:
        if callamount != 0:
            print("not yet")
        elif callamount == 0:
            print(players[i] + ", what are you going to do? (c)heck or (b)et")
            bet = input ("")
            if bet == "c":
                i+=1
            elif bet == "b":
                print("What do you want to bet?")
                betnum = input("")
                bet()
                chipcount(pot)






if chips == "n":
    virtualchipround()
else:
    nochipround()