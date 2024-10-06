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

    counter = "B" if player == 1 else "R"

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] != counter:
                continue

            key1 = column - row
            if key1 not in top_left_to_bottom_right:
                top_left_to_bottom_right[key1] = 0
            top_left_to_bottom_right[key1] += 1
            
            if top_left_to_bottom_right[key1] >= 4:
                return True

            key2 = column + row
            if key2 not in bottom_left_to_top_right:
                bottom_left_to_top_right[key2] = 0
            bottom_left_to_top_right[key2] += 1
            
            if bottom_left_to_top_right[key2] >= 4:
                return True

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
        
        lowest_point = len(board) - 1
        for row in reversed(board):
            if row[c_choice] != "0":
                lowest_point = board.index(row) -1

        board = update_grid(board, c_choice, lowest_point, player)
        won = check_wins(board, player, turns, board)

        if won == True:
            winner = player

        os.system('cls' if os.name == 'nt' else 'clear')
        if player == 1:
            player = 2
        else:
            player = 1
        turns+=1
        
    print(f"Player {winner} has won the game.")

if __name__ == "__main__":
    main()

