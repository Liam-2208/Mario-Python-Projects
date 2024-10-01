import os
import time

def draw(grid):
    i = 0
    print("")
    print("0 1 2 3 4 5 6")
    print("| | | | | | |")
    for row in grid:
        print(f"{" ".join(row)} -- {i}")
        i+=1

def add_piece(grid, column, row, player):
    if player == 1:
        piece = "B"
    else:
        piece = "R"
    grid[row][column] = piece
    return grid

def check_horizontal(grid):
    for row in grid:
        for i in range(len(row)-1):
            temp = "".join(row[i:i+4])
            if temp == "BBBB":
                return 1
            elif temp == "RRRR":
                return 2
            i+=1 
    return False

def check_vertical(grid):
    column = ""
    for column_top in range(0, len(grid[0])):
        for space in grid[0][0:len(grid)]:
            column+=space
        for i in range(0, len(column)-1):
            temp = "".join(column[i:i+4])
            print(temp)
            if temp == "BBBB":
                return 1
            elif temp == "RRRR":
                return 2
    return False
#def check_diagonal(grid):
    #

def main():
    board = [["0","0","0","0","0","0","0"] for i in range(0,6)]
    won = False
    player = 1
    turns = 1

    while not won == True:
        draw(board)

        print(f"It is player {player}'s go.")
        c_choice = int(input("Enter the column number: "))
        r_choice = int(input("Enter the row number: "))
        choice = board[c_choice][r_choice]
    
        validMove = False
        row = len(board) - 1
        while not validMove:
            if board[row][c_choice] == "0":
                if r_choice > row or r_choice < row:
                    print("Invalid move. Your turn has been forfieted.")
                    time.sleep(1)
                    break
                elif board[r_choice][c_choice] != "0":
                    print("Invalid move. Your turn has been forfieted.")
                    time.sleep(1)
                    break
                else:
                    board = add_piece(board, c_choice, r_choice, player)
                    validMove = True
            else:
                row-=1

        print(check_vertical(board))


        #os.system("cls")
        if player == 1:
            player = 2
        else:
            player = 1
        turns+=1

main()


