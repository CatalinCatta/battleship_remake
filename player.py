import os
import string

from board import display_board


def valid_coord(board):
    while True:
        coord = input("Gimme the position (like A3): ")
        if 1 < len(coord) < 4:
            try:
                i = string.ascii_uppercase.find(coord[0].upper())
                j = int(coord[1:]) - 1
                if i < len(board) and 0 <= j < len(board):
                    return i, j
                else:
                    print("There is a mistake(Invalid input)")
            except ValueError:
                print("There is a mistake(Invalid input)")
        else:
            print("There is a mistake(Invalid input)")


def valid_direction():
    while True:
        d = input("Gimme the direction(N, S, E, W): ").upper()
        if d in ["N", "S", "E", "W"]:
            return d


def player_shoot(player_board, enemy_board):
    while True:
        x, y = valid_coord(player_board)
        if player_board[x][y] == "0":
            if enemy_board[x][y] == "X":
                player_board[x][y] = "H"
                print("Nice shot!")
                return player_board
            else:
                player_board[x][y] = "M"
                print("Miss, good luck next time.")
                return player_board
        else:
            print("U alredy tried that spot.")


def check_boats(board, coord, direction, boat_size):
    x, y = coord
    boat_coord = []
    for i in range(boat_size + 1):
        if direction == "N":
            if (x - boat_size) >= 0:
                if board[x - i][y] == "X" or x < len(board) - 1 and board[x - i + 1][y] == "X" or x > 0 and board[x - i - 1][y] == "X" or y < len(board) - 1 and board[x - i][y + 1] == "X" or y >= 1 and board[x - i][y - 1] == "X":
                    break
                if i == boat_size:
                    boat_coord = [[x - boat_size, x], [y, y]]
            else:
                break
        elif direction == "S":
            if (x + boat_size) <= len(board):
                if board[x + i][y] == "X" or x > 0 and board[x + i - 1][y] == "X" or x < len(board) - 1 and board[x + i + 1][y] == "X" or y >= 1 and board[x + i][y - 1] == "X" or y < len(board) - 1 and board[x + i][y + 1] == "X":
                    break
                if i == boat_size:
                    boat_coord = [[x, x + boat_size], [y, y]]
            else:
                break
        elif direction == "W":
            if (y - boat_size) >= 0:
                if board[x][y - i] == "X" or x < len(board) - 1 and board[x + 1][y - i] == "X" or x > 0 and board[x - 1][y - i] == "X" or y < len(board) - 1 and board[x][y - i + 1] == "X" or y >= 1 and board[x][y - i - 1] == "X":
                    break
                if i == boat_size:
                    boat_coord = [[x, x], [y - boat_size, y]]
            else:
                break
        elif direction == "E":
            if (y + boat_size) <= len(board):
                if board[x][y + i] == "X" or x < len(board) - 1 and board[x + 1][y + i] == "X" or x > 0 and board[x - 1][y + i] == "X" or y < len(board) - 1 and board[x][y + i + 1] == "X" or y >= 1 and board[x][y + i - 1] == "X":
                    break
                if i == boat_size:
                    boat_coord = [[x, x], [y, y + boat_size]]
            else:
                break
    return boat_coord


def player_boats(board, position, player_1, player_2, empty_map):
    boats_list = [[3, 2], [4, 2], [4, 3, 2], [5, 3, 2], [5, 4, 3, 2], [5, 4, 3, 3, 2]]
    boats_list = boats_list[len(board) - 5]
    b_c = []
    while len(boats_list) > 0:
        for elem in boats_list:
            print(f"Boat len is: {elem}")
            coord = valid_coord(board)
            direction = valid_direction()
            if position == 0:
                print(f"{player_1}, place your boats")
            else:
                print(f"{player_2}, place your boats")
            boats_coord = check_boats(board, coord, direction, elem)
            if len(boats_coord) != 0:
                if direction == "W":
                    for i in range(boats_coord[0][0], boats_coord[0][1] + 1):
                        for j in range(boats_coord[1][0] + 1, boats_coord[1][1] + 1):
                            board[i][j] = "X"
                elif direction == "E":
                    for i in range(boats_coord[0][0], boats_coord[0][1] + 1):
                        for j in range(boats_coord[1][0], boats_coord[1][1]):
                            board[i][j] = "X"
                elif direction == "S":
                    for j in range(boats_coord[1][0], boats_coord[1][1] + 1):
                        for i in range(boats_coord[0][0], boats_coord[0][1]):
                            board[i][j] = "X"
                elif direction == "N":
                    for j in range(boats_coord[1][0], boats_coord[1][1] + 1):
                        for i in range(boats_coord[0][0] + 1, boats_coord[0][1] + 1):
                            board[i][j] = "X"
                boats_list.remove(elem)
                b_c .append(boats_coord)
                os.system("clear")
                if position == 0:
                    print(display_board(board, empty_map, player_1, player_2))
                else:
                    print(display_board(empty_map, board, player_1, player_2))
            else:
                print("To close!")
    return board, b_c


def sunk_check(shooting_board, enemy_boats):
    for elem in enemy_boats:
        n = 0
        for i in range(elem[0][0], elem[0][1] + 1):
            for j in range(elem[1][0], elem[1][1]):
                if shooting_board[i][j] == "H":
                    n += 1
        if n == elem[0][1] - elem[0][0] != 0:
            for i in range(elem[0][0], elem[0][1]):
                for j in range(elem[1][0], elem[1][1] + 1):
                    shooting_board[i][j] = "S"
            print("U sunk my batleship")
            enemy_boats.remove(elem)
        elif n == elem[1][1] - elem[1][0] != 0:
            for i in range(elem[0][0], elem[0][1] + 1):
                for j in range(elem[1][0], elem[1][1]):
                    shooting_board[i][j] = "S"
            print("U sunk my batleship")
            enemy_boats.remove(elem)
        else:
            for i in range(elem[0][0], elem[0][1]):
                for j in range(elem[1][0], elem[1][1] + 1):
                    if shooting_board[i][j] == "H":
                        n += 1
            if n == elem[0][1] - elem[0][0] != 0:
                for i in range(elem[0][0], elem[0][1]):
                    for j in range(elem[1][0], elem[1][1] + 1):
                        shooting_board[i][j] = "S"
                print("U sunk my batleship")
                enemy_boats.remove(elem)
            elif n == elem[1][1] - elem[1][0] != 0:
                for i in range(elem[0][0], elem[0][1]) + 1:
                    for j in range(elem[1][0], elem[1][1]):
                        shooting_board[i][j] = "S"
                print("U sunk my batleship")
                enemy_boats.remove(elem)
    return shooting_board, enemy_boats
