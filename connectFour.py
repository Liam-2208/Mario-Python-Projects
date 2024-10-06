import os
import time

WIN_LENGTH = 4
COLUMNS = 6
ROWS = 5

def draw(grid):
    print("")
    print(" ".join(str(i) for i in range(COLUMNS)))
    print("|" + " |" * (int(COLUMNS)-1))
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

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_horizontal(grid):
    for row in grid:
        for row_index in range(ROWS-3):
            temp = "".join(row[row_index:row_index+WIN_LENGTH])

            if temp == "BBBB":
                return True
            elif temp == "RRRR":
                return True
            row_index+=1 
    return False

def check_vertical(grid):
    column = ""
    for column_top in range(COLUMNS):
        for row in range(ROWS):
            column+=grid[row][column_top]

        for column_index in range(COLUMNS-3):
            temp = column[column_index:column_index+WIN_LENGTH]
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
        for column in range(COLUMNS):
            if grid[row][column] != counter:
                continue

            key1 = column - row
            if key1 not in top_left_to_bottom_right:
                top_left_to_bottom_right[key1] = 0
            top_left_to_bottom_right[key1] += 1
            
            if top_left_to_bottom_right[key1] >= WIN_LENGTH:
                return True

            key2 = column + row
            if key2 not in bottom_left_to_top_right:
                bottom_left_to_top_right[key2] = 0
            bottom_left_to_top_right[key2] += 1
            
            if bottom_left_to_top_right[key2] >= WIN_LENGTH:
                return True

    return False

def check_wins(grid, player, turns, board):
    won = check_diagonal(grid, player) or check_vertical(grid) or check_horizontal(grid)
    if won:
        return won
    elif turns == len(board)*len(board[0]):
        return "All spaces filled. Its a draw!!"

def main():
    board = [["0" for _ in range(COLUMNS)] for _ in range(ROWS)]
    won = False
    player = 1
    turns = 1
    column_choice = 0
    lowest_point = 0

    while not won == True:
        draw(board)
       
        if turns == COLUMNS*ROWS:
            print("All spaces filled!\nIt's a draw!.")

        print(f"It is player {player}'s go.")

        while True:
            column_choice = input("Pick a column: ")
            
            try:
                column_choice = int(column_choice)
                
                if column_choice < 0 or column_choice >= COLUMNS:
                    print(f"Column outside range. Please pick a column between 0 and {COLUMNS - 1}.")
                else:
                    break
            except ValueError:
                print("Input must be a valid number.")
            
            time.sleep(1)
            clear_console()
            draw(board)

        lowest_point = len(board) - 1
        for row in reversed(range(ROWS)):
            if row[column_choice] != "0":
                lowest_point = row

        if lowest_point == -1:
            print(f"Column {column_choice} is full. Please choose another.")
        else:
            board = update_grid(board, column_choice, lowest_point, player)

        won = check_wins(board, player, turns, board)

        if won == True:
            winner = player
        elif won == type(str):
            print(won)
            break

        clear_console()
        if player == 1:
            player = 2
        else:
            player = 1
        turns+=1
    
    draw(board)
    print(f"Player {winner} has won the game.")

if __name__ == "__main__":
    main()

