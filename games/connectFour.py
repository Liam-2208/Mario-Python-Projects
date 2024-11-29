import os
import time

WIN_LENGTH: int = 4
COLUMNS: int = 6
ROWS: int = 5

def draw(grid: list) -> None:
    print("")
    print(" ".join(str(i) for i in range(COLUMNS)))
    print("|" + " |" * (int(COLUMNS)-1))
    for row in grid:
        print(f"{' '.join(row)}")

def update_grid(grid: list, column: int, row: int, player: int) -> list[str]:
    time.sleep(1)
    if player == 1:
        piece: str = "B"
    else:
        piece: str = "R"
    grid[row][column] = piece
    return grid

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def check_horizontal(grid: list) -> bool:
    for row in grid:
        for row_index in range(ROWS-3):
            temp: str = "".join(row[row_index:row_index+WIN_LENGTH])

            if temp == "BBBB":
                return True
            elif temp == "RRRR":
                return True
            row_index+=1 
    return False

def check_vertical(grid: list) -> bool:
    column: str = ""
    for column_top in range(COLUMNS):
        for row in range(ROWS):
            column+=grid[row][column_top]

        for column_index in range(COLUMNS-3):
            temp: str = column[column_index:column_index+WIN_LENGTH]
            if temp == "BBBB":
                return True
            elif temp == "RRRR":
                return True
    return False

def check_diagonal(grid: list, player: list) -> bool:
    top_left_to_bottom_right: dict[int, int] = {}
    bottom_left_to_top_right: dict[int, int] = {}

    counter: str = "B" if player == 1 else "R"

    for row in range(len(grid)):
        for column in range(COLUMNS):
            if grid[row][column] != counter:
                continue

            key1: int = column - row
            if key1 not in top_left_to_bottom_right:
                top_left_to_bottom_right[key1] = 0
            top_left_to_bottom_right[key1] += 1
            
            if top_left_to_bottom_right[key1] >= WIN_LENGTH:
                return True

            key2: int = column + row
            if key2 not in bottom_left_to_top_right:
                bottom_left_to_top_right[key2] = 0
            bottom_left_to_top_right[key2] += 1
            
            if bottom_left_to_top_right[key2] >= WIN_LENGTH:
                return True

    return False

def check_wins(grid: list, player: int, turns: int) -> bool | str:
    won: bool = check_diagonal(grid, player) or check_vertical(grid) or check_horizontal(grid)
    if won:
        return won
    elif turns == COLUMNS*ROWS:
        return "All spaces filled. Its a draw!!"

def main() -> None:
    board: list = [["0" for _ in range(COLUMNS)] for _ in range(ROWS)]
    won: bool = False
    player: int = 1
    turns: int = 1
    column_choice: int = 0
    lowest_point: int = 0

    while not won == True:
        draw(board)
       
        if turns == COLUMNS*ROWS:
            print("All spaces filled!\nIt's a draw!.")

        print(f"It is player {player}'s go.")

        while True:   
            try:
                column_choice: int = int(input("Pick a column: "))
        
                if column_choice < 0 or column_choice >= COLUMNS:
                    print(f"Column outside range. Please pick a column between 0 and {COLUMNS - 1}.")
                else:
                    break
            except ValueError:
                print("Input must be a valid number.")
            
            time.sleep(1)
            clear_console()
            draw(board)

        lowest_point: int = len(board) - 1
        for row in reversed(range(ROWS)):
            if board[row][column_choice] != "0":
                lowest_point = int(row) - 1

        if lowest_point == -1:
            print(f"Column {column_choice} is full. Please choose another.")
            time.sleep(1)
            clear_console()
        else:
            board: list = update_grid(board, column_choice, lowest_point, player)

        won: bool = check_wins(board, player, turns)

        if won:
            winner: int = player
        elif type(won) == str:
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

