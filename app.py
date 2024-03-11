import ARMem as ar
import time

def user_names(name):
    dic_names = {}
    list_times = [0, 0, 0]

    if (name == "") and (dic_names == {}):
        while name == "":
            name = input("You need at least one player to continue!\nEnter the player's name or press enter to continue: ")
            
    while name != "":
        while name in dic_names:
            name = input("There is another player with that name! Use a different name.\nEnter the player's name or press enter to continue: ")
        if name != "":
            dic_names.setdefault(name, list_times)
            name = input("Enter the player's name or press enter to continue: ")
    
    print('\033[2J')
    return dic_names

def levels(level, players):
    cont = "-"
    elements = [0,1,2,3,4]

    if level == 0:
        cont = input("Instructions:\nA list of elements are going to be shown in your screen. You will have 5 seconds to memorize all of the X (elements).\nThen you will have to show the markers to the camera, arranging them in the order that was shown to you previously.\nEach player will have their turn and each level will have five turns per player.\nYou can take your time but try to do it as fast as you can!\nGood luck!\n\nPress the enter key to continue.\n")
    if cont == "":
        print('\033[2J')

    if level == 1:
        cont = input("Level 1:\nFor this level, you will have to arrange a total of three markers.\nReady to start?\n\nPress the enter key to continue.\n")
        if cont == "":
            print('\033[2J')
        for iteration in range(1, 6):
            print(f"Round {iteration} is about to start!")

            for player in players.keys():
                print(f"{player}, it's your turn!")
                print(f"Memorize the following elements:\n{elements}")
                print('\033[2J')

                iteration_time = 1
                players[player][0] += iteration_time # Fix pending.

                print(f"Great job, {player}!")
                print('\033[2J')
        print(players)

dic_players = user_names(input("Player registration:\nEnter the player's name or press enter to continue: "))
levels(0, dic_players)
levels(1, dic_players)