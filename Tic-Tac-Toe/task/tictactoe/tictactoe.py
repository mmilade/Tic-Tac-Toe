game_is_running = True
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
marker = "X"
player_one = True


def print_field():
    # print("-------------------")
    print(" ")
    print("Coordinates:\n")
    print("1 3  |  2 3  |  3 3")
    print(" ")
    print("1 2  |  2 2  |  3 2")
    print(" ")
    print("1 1  |  2 1  |  3 1")
    # print("-------------------")
    print(" ")
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|", )
    print("|", cells[3], cells[4], cells[5], "|", )
    print("|", cells[6], cells[7], cells[8], "|", )
    print("---------")


print_field()

options = [
['1', '3'], ['2', '3'], ['3', '3'],
['1', '2'], ['2', '2'], ['3', '2'],
['1', '1'], ['2', '1'], ['3', '1']]

while game_is_running == True:

    if player_one == True:
        marker = "X"
        print("\nPlayer X, enter the coordinates: ")
    else:
        marker = "O"
        print("\nPlayer O, enter the coordinates: ")

    # print("Enter the coordinates:")
    user_input = input()
    coordinates = list(user_input.split())
    # print(coordinates)
    if coordinates[0].isnumeric() == False or coordinates[1].isnumeric() == False:
        print("You should enter numbers!")
    elif coordinates[0] not in ['1', '2', '3'] or coordinates[1] not in ['1', '2', '3']:
        print("Coordinates should be from 1 to 3!")
    elif coordinates in options:
        # print(coordinates)
        coordinate_index = options.index(coordinates)
        # print(coordinate_index)

        if cells[coordinate_index] == "_" or cells[coordinate_index] == " ":
            cells[coordinate_index] = marker
            # print(cells[coordinate_index])

            print_field()

            player_one = not player_one
            # print(player_one)

            x_count = cells.count("X")
            o_count = cells.count("O")
            winner = []

            if cells[0] == cells[1] == cells[2] and cells[0] in ["X", "O"]:
                winner.append(cells[0])
            if cells[3] == cells[4] == cells[5] and cells[3] in ["X", "O"]:
                winner.append(cells[3])
            if cells[6] == cells[7] == cells[8] and cells[6] in ["X", "O"]:
                winner.append(cells[6])
            if cells[0] == cells[3] == cells[6] and cells[0] in ["X", "O"]:
                winner.append(cells[0])
            if cells[1] == cells[4] == cells[7] and cells[1] in ["X", "O"]:
                winner.append(cells[1])
            if cells[2] == cells[5] == cells[8] and cells[2] in ["X", "O"]:
                winner.append(cells[2])
            if cells[2] == cells[4] == cells[6] and cells[2] in ["X", "O"]:
                winner.append(cells[2])
            if cells[0] == cells[4] == cells[8] and cells[0] in ["X", "O"]:
                winner.append(cells[0])

            if "X" in winner and "O" in winner:
                # print("Impossible")
                pass
            elif abs(x_count - o_count) > 1:
                # print("Impossible")
                pass
            elif len(winner) > 0:
                print(winner[0], "wins")
                game_is_running = False
            elif " " in cells or "_" in cells:
                # print("Game not finished")
                pass
            elif len(winner) == 0:
                print("Draw")
                game_is_running = False

        else:
            print("This cell is occupied! Choose another one!")

    else:
        print("something is wrong")
