import os
import time

def draw(grid):
    i = 0
    print("")
    print("0 1 2 3 4 5 6")
    print("| | | | | | |")
    for row in grid:
        print(f"{' '.join(row)}")

def update_grid(grid, column, row, player):
    time.sleep(1)
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

def check_diagonal(grid, player):
    top_left_to_bottom_right = {}
    bottom_left_to_top_right = {}

    if player == 1:
        counter = "B"
    else:
        counter = "R"

    for row in range(0, len(grid)):
        for space in range(0, len(grid[0])):
            if space == "0":
                continue
            elif space != counter:
                continue
            else:
                key1 = space - row
                top_left_to_bottom_right[key1] += 1
                
                key2 = space + row
                bottom_left_to_top_right[key2] +=1

                if key1 in top_left_to_bottom_right == 4:
                    return True
                elif key2 in bottom_left_to_top_right == 4:
                    return True
                else:
                    return False

def check_wins(grid, player, turns, board):
    won = check_diagonal(grid, player) or check_vertical(grid) or check_horizontal(grid)
    if won:
        return won
    elif turns == len(board)*len(board[0]):
        return "All spaces filled. Its a draw!!"

def main():
    board = [["0","0","0","0","0","0","0"] for i in range(0,6)]
    won = False
    player = 1
    turns = 1
    c_choice = 0
    lowest_point = 0

    while not won == True:
        draw(board)
       
        if turns == len(board)*len(board[0]):
            print("All spaces filled!\nIt's a draw!.")

        print(f"It is player {player}'s go.")

        c_choice = int(input("Pick a column: "))
        while True:
            try:
                if c_choice not in range(0, len(board[0])):
                    print("Column outside range.")
                    c_choice = int(input("Pick a column: "))
                else:
                    break
            except ValueError:
                print("Column should be a valid number between 0 and 6.")
        
        for row in board:
            if row[c_choice] != "0":
                lowest_point = board.index(row)
                lowest_point-=1
                break       
            else:
                lowest_point = len(board)-1

        board = update_grid(board, c_choice, lowest_point, player)
        won = check_wins(board, player, turns, board)

        if won == True:
            winner = player

        os.system("cls")
        if player == 1:
            player = 2
        else:
            player = 1
        turns+=1
        
    print(f"Player {winner} has won the game.")

if __name__ == "__main__":
    main()

