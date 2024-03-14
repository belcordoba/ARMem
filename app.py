import ARMem as ar
import time
import random

def user_names(dic_players):
    list_base = [0, 0, 0]
    player_amount = 0
    player_list = []
    print("#### Player registration: ####")
    if len(dic_players) > 0:
        for name in dic_players.keys():
            player_list.append(name)
        print(f"Current player list:\n{player_list}")

    while int(player_amount) <= 0:
        player_amount = input("Enter the amount of players that you want to add: ")
        try:
            int_check = int(player_amount)
        except ValueError:
            print("ERROR: That's not a valid number! Make sure to enter an integer.")
            player_amount = 0
        else:
            if int(player_amount) <= 0:
                print("ERROR: The amount of players must be 1 or above!")

    for i in range(int(player_amount)):
        name = input(f"Enter player #{i+1}'s name: ")
        while name in dic_players:
            name = input(f"There is another player with that name! Use a different name.\nEnter player #{i+1}'s name: ")
        list_times = list_base[:]
        dic_players.setdefault(name, list_times)

    for name in dic_players.keys():
        if name not in player_list:
            player_list.append(name)
    print(f"Player registration completed!\nCurrent player list:\n{player_list}\nReturning to main menu...")
    time.sleep(4)
    
    print('\033[2J')

def generate_list(length):
    options = [(0, "pineapple"), (1, "cherry"), (2, "grape"), (3, "pear"), (4, "soursop")]
    generated_list = []

    while len(generated_list) != length:
        number = random.choice(options)
        if number not in generated_list:
            generated_list.append(number)

    return generated_list

def levels(level, players):

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
            #time.sleep(2)
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
                print("3...")
                time.sleep(1)
                print("2...")
                time.sleep(1)
                print("1...")
                time.sleep(1)
                print("Go!")
                time.sleep(1)
                print('\033[2J')

                iteration_time = round(ar.start_sorting(id_elements,flip_image=True,show_images=True, show_coordinates=False, show_ids=False, show_identified_marker=True), 2)
                players[player][i] += iteration_time

                print(f"Great job, {player}!")
                time.sleep(2)
                print('\033[2J')
    return players

def sort_value(item):
    return item[1]

def level_report(data, level):
    data_list = []
    length = len(data)
    for x, y in data.items():
        data_list.append([x,y[level]])

    data_list.sort(key=sort_value)
    print(f"Leaderboard - Level #{level}")
    for i in range(length):
        print(f"#{i+1} - Name: {data_list[i][0]} - Time: {data_list[i][1]}s")

def game():
    for level in range(0, 4):
        levels(level, dic_players)

def main_menu(dic_players):
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
                print("There needs to be at least one player to start the game!\nReturning to main menu...")
                time.sleep(3)
                print('\033[2J')
        elif player_choice == "3":
            quit()
        else:
            print("This is not a valid choice! Enter the number of one of the options.\nReturning to main menu...")
            time.sleep(4)
            print('\033[2J')

dic_players = {}
main_menu(dic_players)