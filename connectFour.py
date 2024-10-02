import os
import time

def draw(grid):
    i = 0
    print("")
    print("0 1 2 3 4 5 6")
    print("| | | | | | |")
    for row in grid:
        print(f"{' '.join(row)} -- {i}")
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
        for i in range(len(row)-3):
            temp = "".join(row[i:i+4])

            if temp == "BBBB":
                return True
            elif temp == "RRRR":
                return True
            i+=1 
    return False

def check_vertical(grid):
    column = ""
    for column_top in range(0, len(grid[0])):
        for row in range(0, len(grid)):
            column+=grid[row][column_top]

        for i in range(0, len(column)-3):
            temp = column[i:i+4]
            print(temp)
            if temp == "BBBB":
                return True
            elif temp == "RRRR":
                return True
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

        while c_choice not in range(len(board[0])-1):
            c_choice = int(input("Enter the column number: "))
            print(f"{c_choice} is not a valid column.")

        while r_choice not in range(0, len(board) - 1):
            r_choice = int(input("Enter the row number: "))
            print(f"{r_choice} is not a valid column.")
    
        validMove = False
        row = len(board) - 1
        while not validMove:
            if board[row][c_choice] == "0":
                if r_choice > row or r_choice < row:
                    print("Invalid move. You cannot place your token where there is none below it.")
                    time.sleep(1)
                elif board[r_choice][c_choice] != "0":
                    print("Invalid move. You cannot place your token in the same place as another players.")
                    time.sleep(1)
                else:
                    board = add_piece(board, c_choice, r_choice, player)
                    validMove = True
            else:
                row-=1

        print(check_vertical(board))

        horizontal = check_horizontal(board)
        vertical = check_vertical(board)
        #diagonal = check_diagonal(board)

        #won = horizontal or vertical or diagonal
        if won == True:
            winner = player

        #os.system("cls")
        if player == 1:
            player = 2
        else:
            player = 1
        turns+=1

    print(f"{winner} has won the game.")

main()


