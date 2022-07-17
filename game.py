import os
from board import board, display_board, lenght
from player import player_boats, player_shoot, sunk_check


def player_shooting(player_map, enemy_map, enemy_boats):
    my_list = player_map
    my_list = player_shoot(player_map, enemy_map)
    my_list = sunk_check(player_map, enemy_boats)
    return my_list


def ask_for_gamemode():
    gamemode = input("""
    1. Human vs Human
    2. Nothing yet
    3. Nothing yet
    """)
    while True:
        if gamemode == "1":
            return 1
        elif gamemode == "2":
            gamemode = input("There is nothing implemented yet, please press 1: ")
        elif gamemode == "3":
            gamemode = input("Here is also nothing, press 1: ")
        else:
            gamemode = input("I can't uderstand that, there is a hint, press 1: ")


def ask_for_turns():
    while True:
        turns = input("How many turns do u want to play?(5 - 50)\n")
        try:
            turns = int(turns)
            if 4 < turns < 51:
                return turns
            else:
                print("5-50 means between 4 and 51...")
        except ValueError:
            print("I can understand only numbers between 5 and 50")


def main():
    os.system("clear")
    print("            BATLESHIP")
    gamemode = ask_for_gamemode()
    total_turns = ask_for_turns()
    my_lenght = lenght()
    turns = 0
    if gamemode == 1:
        os.system("clear")
        player_1_main_map = board(my_lenght)
        player_2_main_map = board(my_lenght)
        player_1_shooting_map = board(my_lenght)
        player_2_shooting_map = board(my_lenght)
        player_1_name = input("Who is the first player?\n")[:20]
        player_2_name = input("And who is the second player?\n")[:20]
        os.system("clear")
        print(display_board(player_1_main_map, player_2_main_map, player_1_name, player_2_name))
        player_1_main_map, player_1_boats = player_boats(player_1_main_map, 0, player_1_name, player_2_name, player_1_shooting_map)
        input("Press RETURN to change to the next player")
        os.system("clear")
        print(display_board(player_2_main_map, player_2_main_map, player_1_name, player_2_name))
        player_2_main_map, player_2_boats = player_boats(player_2_main_map, 1, player_1_name, player_2_name, player_2_shooting_map)
        input("Press RETURN to clear board and start the game!\n")
    while turns < total_turns:
        turns += 1
        if gamemode == 1:
            os.system("clear")
            print(display_board(player_1_shooting_map, player_2_shooting_map, player_1_name, player_2_name))
            print(f"Turn: {turns}")
            print(f"{player_1_name} turn:")
            player_1_shooting_map, player_2_boats = player_shooting(player_1_shooting_map, player_2_main_map, player_2_boats)
            if len(player_2_boats) == 0:
                os. system("clear")
                print(display_board(player_1_shooting_map, player_2_shooting_map, player_1_name, player_2_name))
                print(f"{player_1_name} has won!")
                if input("Wanna play again?\n").upper() in ["YES", "Y"]:
                    main()
                else:
                    return
            os.system("clear")
            print(display_board(player_1_shooting_map, player_2_shooting_map, player_1_name, player_2_name))
            print(f"Turn: {turns}")
            print(f"{player_2_name} turn:")
            player_2_shooting_map, player_1_boats = player_shooting(player_2_shooting_map, player_1_main_map, player_1_boats)
            print(f"Turn: {turns - 1}")
            if len(player_1_boats) == 0:
                os. system("clear")
                print(display_board(player_1_shooting_map, player_2_shooting_map, player_1_name, player_2_name))
                print(f"{player_2_name} has won!")
                if input("Wanna play again?\n").upper() in ["YES", "Y"]:
                    main()
                else:
                    return
    print("Finished turn limit!")
    if input("Wanna play again?\n").upper() in ["YES", "Y"]:
        main()
    else:
        return


if __name__ == "__main__":
    main()
