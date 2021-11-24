
from computer_moves import Computer_moves
import random

comp_x = []
comp_y = []
player_x = [ ]
player_y = [ ]


# defining initial variables
game_over = False
move_count = 0

combined_symbol_status = [False, False, False,False, False, False, False, False, False]
computer = Computer_moves(combined_symbol_status, comp_x, comp_y, move_count)

player_symbol = input("Enter X or O: ")
if player_symbol == "X":
    computer_symbol = "O"
else:
    computer_symbol = "X"



def combined_symbol_data():
    n = 0
    p = 0
    i = 0
    for k in range(3):
        if comp_x[move_count] == p:
            if comp_y[move_count] == 0:
                combined_symbol_status[n] = "comp"

            elif comp_y[move_count] == 1:
                combined_symbol_status[n + 1] = "comp"
            elif comp_y[move_count] == 2:
                combined_symbol_status[n + 2] = "comp"
        n = n + 3
        p = p + 1


def combined_symbol_data2():
    n = 0
    p = 0
    i = 0
    for k in range(3):
        if player_x[move_count] == p:
            if player_y[move_count] == 0:
                combined_symbol_status[n] = "user"
            elif player_y[move_count] == 1:
                combined_symbol_status[n + 1] = "user"
            elif player_y[move_count] == 2:
                combined_symbol_status[n + 2] = "user"
        n = n + 3
        p = p + 1


def print_board_combined():    # this function is used for printing the board and it prints symbol at required places
    i = 0
    while (i < 9):
        if i == 3 or i == 6:
            print(" ")
        if combined_symbol_status[i] == "comp":
            print(computer_symbol, end=" ")
        if combined_symbol_status[i] == "user":
            print(player_symbol, end=" ")
        if combined_symbol_status[i] == False:
            print("_", end=" ")
        i = i + 1
    print("")


def check_winner():
    over = False
    i = 0
    k = 0
    str = ["user", "comp"]
    win_msg = ["Congrats, you win!!", "Uh-oh, looks like you lost"]
    for p in range(2):
        if combined_symbol_status[0] == str[p] and combined_symbol_status[4] == str[p] and combined_symbol_status[8] == str[p]:
            print(win_msg[p])
            over = True
        elif combined_symbol_status[2] == str[p] and combined_symbol_status[4] == str[p] and combined_symbol_status[6] == str[p]:
            print(win_msg[p])
            over = True
        while (i <= 6):
            if combined_symbol_status[i] == str[p] and combined_symbol_status[i + 1] == str[p] and combined_symbol_status[i + 2] == str[p]:
                print(win_msg[p])
                over = True
            elif combined_symbol_status[k] == str[p] and combined_symbol_status[k + 3] == str[p] and combined_symbol_status[k + 6] == str[p]:
                print(win_msg[p])
                over = True
            i = i + 3
            k = k + 1

    return over


x_coords = [0, 1, 2]
y_coords = [0, 1, 2]

coords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]


def random_moves():
    j = random.choice(coords)
    comp_x.append(j[0])
    comp_y.append(j[1])
    coords.remove(j)
    combined_symbol_data()


c = "Uh-oh looks like you lost."
u = "Congrats, you WIN!!"

random_moves()

move_count = 0

while game_over == False:

    print_board_combined()
    # players x and y atributes are appended
    player_x.append(int(input("\nEnter x-coordinate: ")))
    player_y.append(int(input("Enter y-coordinate: ")))

    combined_symbol_data2()

    player_coords = player_x[move_count], player_y[move_count]

    
    coords.remove(player_coords)
  
    print_board_combined()

    move_count = move_count + 1
    if move_count == 8:
        print("Game over")
        break

    print("Board after computer's move: ")

    game_over = check_winner()

    if game_over is True:
        break

    row_opp = computer.row_oppurtunity()
    if row_opp == True:
        print(c, "row won")
        break
    col_opp = computer.column_oppurtunity()
    if col_opp == True:
        print(c, "column won")
        break
    dia_opp = computer.diagonal_oppurtunity()
    if dia_opp == True:
        print(c, "diagonal won")
        break

    rt = computer.row_threat_checker()
    if rt == True:
        continue
    ct = computer.column_threat_checker()
    if ct == True:
        continue
    dt = computer.diagonal_threat_checker()
    if dt == True:
        continue

    random_moves()
    game_over = check_winner()

print_board_combined()
