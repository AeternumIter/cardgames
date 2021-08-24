import os
import time
cont = 0
AvailableGames = ["poker",]

os.system("cls")
while cont == 0:
    print("Please enter the card game that you would like to play below")
    print("")
    print("Our current options for games are:")
    print(AvailableGames)
    game = input("")
    if game in AvailableGames:
        print("You want to play " + game + "? (y/n)")
        confirmation = input("")
        if confirmation == "y":
            cont = 1
        elif confirmation == "n":
            cont = 0
        else:
            print("I'm sorry, that's not a valid response. Please try again.")
            cont = 0
    else:
        print("Whoops, it doesn't look like we have that game. Please try a different game.")
        print("")
        time.sleep(.5)
        cont = 0
os.system("py " + game + ".py")
