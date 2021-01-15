# write your code here
def nesting():  # transform list_symbols to a list of two dimension
    m = 0
    n = 3
    for i in range(3):
        nested_list_symbols.append([])  # of columns
        for j in range(m, n):
            nested_list_symbols[i].append(list_symbols[j])
        n = n + 3
        m = m + 3


def display():
    print("---------")
    print(f"| {nested_list_symbols[0][0]} {nested_list_symbols[0][1]} {nested_list_symbols[0][2]} |")
    print(f"| {nested_list_symbols[1][0]} {nested_list_symbols[1][1]} {nested_list_symbols[1][2]} |")
    print(f"| {nested_list_symbols[2][0]} {nested_list_symbols[2][1]} {nested_list_symbols[2][2]} |")
    print("---------")


def win():
    # Case ONE : if the diagonal ( left to right ) contain 3 X or 3 O
    if nested_list_symbols[0][0] == nested_list_symbols[1][1] == nested_list_symbols[2][2] :
        if nested_list_symbols[0][0] == "X" or nested_list_symbols[0][0] == "O":
            print(f"{nested_list_symbols[0][0]} wins")
            return True
        else:
            return False
    # Case TWO : if the diagonal ( right to left ) contain 3 X or 3 O
    elif nested_list_symbols[0][2] == nested_list_symbols[1][1] == nested_list_symbols[2][0] :
        if nested_list_symbols[0][2] == "X" or nested_list_symbols[0][2] == "O":
            print(f"{nested_list_symbols[0][0]} wins")
            return True
        else:
            return False
    # Case THREE : if it exists a row or a column that has 3 X or 3 O
    else:
        for i in range(3):
            if nested_list_symbols[i][0] == nested_list_symbols[i][1] == nested_list_symbols[i][2]:
                if nested_list_symbols[0][0] == "X" or nested_list_symbols[0][i] == "O":
                    print(f"{nested_list_symbols[i][0]} wins")
                    return True
                else:
                    return False
            if nested_list_symbols[0][i] == nested_list_symbols[1][i] == nested_list_symbols[2][i]:
                if nested_list_symbols[0][i] == "X" or nested_list_symbols[0][i] == "O":
                    print(f"{nested_list_symbols[0][0]} wins")
                    return True
                else:
                    return False
        return False


# the insertion of cells depends on the matrix of coordination : ( as the exercise want )
# (col,row)
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)

def insert_move():
    coors = input("Enter the coordinates: > ").split()
    if len(coors) < 2:
        print("You should enter 2 numbers between 1 and 3!")
        insert_move()  # recursive
    elif len(coors[0]) > 1 or len(coors[1]) > 1 :
        print("You should enter 2 numbers between 1 and 3!")
        insert_move()  # recursive
    else:
        if 49 <= ord(coors[0]) <= 57 and 49 <= ord(coors[1]) <= 57:
            if 49 <= ord(coors[0]) <= 51 and 49 <= ord(coors[1]) <= 51:
                col = int(coors[0]) - 1
                row = int(coors[1]) - 1
                x = nested_list_symbols[row][col]
                if x == "X" or x == "O":
                    print("This cell is occupied! Choose another one!")
                    insert_move()  # recursive
                else:
                    nested_list_symbols[row][col] = move
            else:
                print("Coordinates should be from 1 to 3!")
                insert_move()  # recursive
        else:
            print("You should enter numbers!")
            insert_move()  # recursive


symbols = "         "
list_symbols = list(symbols)
nested_list_symbols = []
nesting()

# Start playing:
steps = 1
move = "X"
stop = False
display()
while not stop:

    insert_move()
    nested_list_symbols.reverse()
    display()
    steps += 1
    if win():
        stop = True
    elif steps == 10:
        print("Draw")
        stop = True
    if steps % 2:
        move = "O"
    else:
        move = "X"

