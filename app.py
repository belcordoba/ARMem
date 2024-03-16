import ARMem as ar
import time
import random

def user_names(dic_players):
    """Requests user input to add the names of the players in a dictionary.

    Args:
        dic_players (_type_): Dictionary where the names of the players will be stored.
    """
    list_base = [0, 0, 0]
    player_amount = 0
    player_list = []
    for player in dic_players.keys():
        player_list.append(player)
    while int(player_amount) <= 0:
        print('\033[2J')
        print("#### Player registration: ####")
        player_amount = input("Enter the amount of players that you want to add: ")
        try:
            int_check = int(player_amount)
        except ValueError:
            cont = input("ERROR: That's not a valid amount! Make sure to enter an integer.\nPress the enter key to try again.\n")
            player_amount = 0
        else:
            if int(player_amount) <= 0:
                cont = input("ERROR: The amount of players must be 1 or above!\nPress the enter key to try again.\n")
    print('\033[2J')

    for i in range(int(player_amount)):
        print("#### Player registration: ####")
        print(f"Current player list:\n{player_list}")
        name = input(f"Enter player #{i+1}'s name: ")
        while name in dic_players:
            cont = input(f"There is another player with that name! Use a different name.\nPress the enter key to try again.\n")
            print('\033[2J')
            name = input(f"#### Player registration: ####\nCurrent player list:\n{player_list}\nEnter player #{i+1}'s name: ")
        list_times = list_base[:]
        dic_players.setdefault(name, list_times)
        for player in dic_players.keys():
            if player not in player_list:
                player_list.append(player)
        print('\033[2J')
    cont = input(f"\n#### Player registration: ####\nPlayer registration completed!\nCurrent player list:\n{player_list}\nPress the enter key to continue.\n")
    print('\033[2J')

def generate_list(length):
    """Generates a random list of elements that the player will have to sort.

    Args:
        length (_type_): Defines the amount of elements that need to be added to the randomized list.

    Returns:
        _type_: Returns the randomized list with the amount of elements that were requested.
    """
    options = [(0, "pineapple"), (1, "cherry"), (2, "grape"), (3, "pear"), (4, "soursop")]
    generated_list = []
    while len(generated_list) != length:
        number = random.choice(options)
        if number not in generated_list:
            generated_list.append(number)
    return generated_list

def levels(level, players):
    """Shows the instructions and executes each different level with their respective iterations.

    Args:
        level (_type_): Defines the level that is currently being executed.
        players (_type_): Dictionary with the names and times of the player, where the total time for each player will be stored.

    Returns:
        _type_: Returns the modified dictionary with the times for each player after the execution of a level.
    """
    if level == 0:
        cont = input("Instructions:\nA list of elements are going to be shown in your screen. You will have 5 seconds to memorize all of the X (elements).\nThen you will have to show the markers to the camera, arranging them in the order that was shown to you previously.\nEach player will have their turn and each level will have five turns per player.\nYou can take your time but try to do it as fast as you can!\nGood luck!\n\nPress the enter key to continue.\n")
        print('\033[2J')

    if level >= 1:
        if level == 1:
            cont = input("Level 1:\nFor this level, you will have to arrange a total of three markers.\nReady to start?\n\nPress the enter key to continue.\n")
        elif level == 2:
            cont = input("Level 2:\nIt's time for a new challenge. For this level, you will have to arrange a total of four markers.\nReady to start?\n\nPress the enter key to continue.\n")
        elif level == 3:
            cont = input("Level 3:\nDid you think that was all? For this level, you will have to arrange a total of five markers.\nReady to start?\n\nPress the enter key to continue.\n")
        print('\033[2J')
        i = -1 + level
        for iteration in range(1, 6):
            print(f"Round {iteration} is about to start!")
            time.sleep(2)
            for player in players.keys():
                elements = generate_list(i+3)
                name_elements = []
                id_elements = []
                for element in elements:
                    name_elements.append(element[1])
                    id_elements.append(element[0])

                print(f"{player}, it's your turn!")
                time.sleep(2)
                print(f"Memorize the following elements:\n{name_elements}")
                time.sleep(2)
                for i in (range(0,4)):
                        print(f"{3-i}...")
                        time.sleep(1)
                print("Go!")
                time.sleep(1)
                print('\033[2J')
                iteration_time = round(ar.start_sorting(id_elements,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=False), 2)
                players[player][i] += iteration_time
                print(f"Great job, {player}!")
                time.sleep(2)
                print('\033[2J')
    return players

def sort_value(value_list):
    """Takes the lists with each player name along their total time during a level (or total game time) and extracts the time so it can be used as the point of reference while sorting.

    Args:
        value_list (_type_): List that contains nested lists with the player's name and total time during a level (or their total game time).

    Returns:
        _type_: Returns the times that will be needed while sorting the player's scores.
    """
    return value_list[1]

def level_report(level, data):
    """Generates the report with each of the player's performance after the execution of a level.

    Args:
        level (_type_): Defines the level that is currently being executed.
        data (_type_): Dictionary with the names and times of the players.
    """
    if level > 0:
        data_list = []
        length = len(data)
        for x, y in data.items():
            data_list.append([x,y[level-1]])
        data_list.sort(key=sort_value)
        print(f"#### Leaderboard - Level #{level-0} ####")
        for i in range(length):
            print(f"#{i+1} - Name: {data_list[i][0]} - Time: {data_list[i][1]}s")
        cont = input("Press the enter key to continue.\n")

def game_report(data):
    """Generates the report with each of the player's performance after the execution of the whole game.

    Args:
        data (_type_): Dictionary with the names and times of the players.
    """
    data_list = []
    length = len(data)
    for x, y in data.items():
        data_sum = y[0] + y[1] + y[2]
        data_list.append([x,data_sum])
        data_sum = 0
    data_list.sort(key=sort_value)
    print(f"#### Leaderboard - Full game ####")
    for i in range(length):
        print(f"#{i+1} - Name: {data_list[i][0]} - Time: {data_list[i][1]}s")
    cont = input("Press the enter key to continue.\n")

def restart():
    """After finishing a game, lets the players choose whether they want to play again (with the same players o a new list) or if they want to leave the game.

    Returns:
        _type_: Returns different results according to the choice made by the players, clearing data and/or calling the respective function that does what the player requested.
    """
    while True:
            print("#### Thank you for playing ARMem #### \nWould you like to play again? If you do, you will return to the main menu.\n1 > Yes, using a new player list\n2 > Yes, using the same player list\n3 > No")
            player_choice = str(input("Enter the number of the option that you would like to choose: "))
            print('\033[2J')
            if player_choice == "1":
                dic_players = {}
                cont = input("Player list cleared!\nYou will be able to add new players with the player registration menu.\nPress the enter key to continue.\n")
                main_menu()
            elif player_choice == "2":
                player_list = []
                for name in dic_players.keys():
                    player_list.append(name)
                cont = input((f"The current player list is:\n{player_list}\nYou will be able to add more players with the player registration menu.\nPress the enter key to continue.\n"))
            elif player_choice == "3":
                quit()
            else:
                cont = input("This is not a valid choice! Enter the number of one of the options.\nPress the enter key to return to the end screen.\n")
                print('\033[2J')   

def game():
    """Calls the functions that will be needed during the execution of a game.
    """
    while True:
        for level in range(0, 4):
            levels(level, dic_players)
            level_report(level, dic_players)
        game_report(dic_players)
        restart()

def main_menu(dic_players):
    """Allows the player to choose the action that they want to do within the game.

    Args:
        dic_players (_type_): Dictionary with the names and times of the players.
    """
    while True:
        print("#### ARMem #### \n1 > Player registration\n2 > Start game\n3 > Leave game")
        player_choice = str(input("Enter the number of the option that you would like to choose: "))
        print('\033[2J')
        if player_choice == "1":
            user_names(dic_players)
        elif player_choice == "2":
            if len(dic_players) > 0:
                game()
            else:
                cont = input("There needs to be at least one player to start the game!\nPress the enter key to return to the main menu.\n")
                print('\033[2J')
        elif player_choice == "3":
            quit()
        else:
            cont = input("This is not a valid choice! Enter the number of one of the options.\nPress the enter key to return to the main menu.\n")
            print('\033[2J')

dic_players = {}
main_menu(dic_players)