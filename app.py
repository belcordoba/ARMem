import ARMem as ar
import time

def user_names(name):
    dic_names = {}
    list_base = [0, 0, 0]

    if (name == "") and (dic_names == {}):
        while name == "":
            name = input("You need at least one player to continue!\nEnter the player's name or press enter to continue: ")
            
    while name != "":
        while name in dic_names:
            name = input("There is another player with that name! Use a different name.\nEnter the player's name or press enter to continue: ")
        if name != "":
            list_times = list_base[:]
            dic_names.setdefault(name, list_times)
            name = input("Enter the player's name or press enter to continue: ")
    
    print('\033[2J')
    return dic_names

def levels(level, players):
    cont = "-"
    elements = [0,1,2,3,4] # Temporary list for tests until the real lists are made.

    if level == 0:
        cont = input("Instructions:\nA list of elements are going to be shown in your screen. You will have 5 seconds to memorize all of the X (elements).\nThen you will have to show the markers to the camera, arranging them in the order that was shown to you previously.\nEach player will have their turn and each level will have five turns per player.\nYou can take your time but try to do it as fast as you can!\nGood luck!\n\nPress the enter key to continue.\n")
    if cont != "-":
        print('\033[2J')

    if level >= 1:
        while cont == "-":
            if level == 1:
                cont = input("Level 1:\nFor this level, you will have to arrange a total of three markers.\nReady to start?\n\nPress the enter key to continue.\n")
            
            elif level == 2:
                cont = input("Level 2:\nIt's time for a new challenge. For this level, you will have to arrange a total of four markers.\nReady to start?\n\nPress the enter key to continue.\n")

            elif level == 3:
                cont = input("Level 3:\nDid you think that was all? For this level, you will have to arrange a total of five markers.\nReady to start?\n\nPress the enter key to continue.\n")

        if cont == "":
            print('\033[2J')

        i = -1 + level
        if cont == "":
            print('\033[2J')
        for iteration in range(1, 6):
            print(f"Round {iteration} is about to start!")
            #time.sleep(2)
            for player in players.keys():
                print(f"{player}, it's your turn!")
                #time.sleep(2)
                print(f"Memorize the following elements:\n{elements}")
                #time.sleep(2)
                print("3...")
                #time.sleep(1)
                print("2...")
                #time.sleep(1)
                print("1...")
                #time.sleep(1)
                print("Go!")
                #time.sleep(1)
                print('\033[2J')

                iteration_time = 1 # This is a temporary variable for tests, AR needs to be implemented.
                players[player][i] += iteration_time

                print(f"Great job, {player}!")
                #time.sleep(2)
                print('\033[2J')
    return players

dic_players = user_names(input("Player registration:\nEnter the player's name or press enter to continue: "))
dic_players = levels(0, dic_players)
dic_players = levels(1, dic_players)
dic_players = levels(2, dic_players)
dic_players = levels(3, dic_players)

print(dic_players) # This is here temporarily to check the final dictionary with the player's times.