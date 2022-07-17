import string


def lenght():
    print("""
    Bord size of 5x5 have the boats: 3 (Cruiser), 2 (Destroyer)
    Bord size of 6x6 have the boats: 4 (Battleship), 2 (Destroyer)
    Bord size of 7x7 have the boats: 4 (Battleship), 3 (Cruiser), 2 (Destroyer)
    Bord size of 8x8 have the boats: 5 (Carrier), 3 (Cruiser), 2 (Destroyer)
    Bord size of 9x9 have the boats: 5 (Carrier), 4 (Battleship), 3 (Cruiser), 2 (Destroyer)
    Bord size of 10x10 have the boats: 5 (Carrier), 4 (Battleship), 3 (Cruiser), 3 (Submarine), 2 (Destroyer)
    """)
    while True:
        my_len = input("Pls gimme the dimenson of the board: ")
        try:
            my_len = int(my_len)
            if 4 < my_len < 11:
                return my_len
            else:
                print("The nr need to be between 5 and 10")
        except ValueError:
            print("I don't understand that")


def board(lenght):
    b = []
    for _ in range(lenght):
        b.append([])
    for i in range(lenght):
        for _ in range(lenght):
            b[i].append("0")
    return b


def display_board(a, b, a_name, b_name):
    s = f"{a_name}:          "
    s += " " * ((len(b) * 4) - len(a_name))
    s += f" {b_name}:\n"
    s += "\n   "
    for e in range(len(b)):
        s += f"| {e+1} "
    s += "            "
    for e in range(len(b)):
        s += f"| {e+1} "
    for i in range(len(b)):
        s += "\n-"
        s += "--+-" * len(b)
        s += "--         -"
        s += "--+-" * len(b)
        s += "--\n"
        s += f" {string.ascii_uppercase[i]} "
        for elem in a[i]:
            if elem == "0":
                s += "|   "
            elif elem == "X":
                s += "| \033[1;32;48mX\033[0;37;48m "
            elif elem == "H":
                s += "| \033[1;33;48mH\033[0;37;48m "
            elif elem == "M":
                s += "| \033[1;31;48mM\033[0;37;48m "
            elif elem == "S":
                s += "| \033[1;32;48mS\033[0;37;48m "
        s += f"          {string.ascii_uppercase[i]} "
        for elem in b[i]:
            if elem == "0":
                s += "|   "
            elif elem == "X":
                s += "| \033[1;32;48mX\033[0;37;48m "
            elif elem == "H":
                s += "| \033[1;33;48mH\033[0;37;48m "
            elif elem == "M":
                s += "| \033[1;31;48mM\033[0;37;48m "
            elif elem == "S":
                s += "| \033[1;32;48mS\033[0;37;48m "
    return s
