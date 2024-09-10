import random

def printRules():
    print("""\nThe computer will think of rock, paper or scissors.
Enter r for rock, s for scissors and p for paper.
The computer will reveal its choice and the winner.""")

def playGame():
    choices = ["Rock","Paper","Scissors"]
    playerChoice = input("\nEnter r for rock, s for scissors and p for paper: ")
    computerChoice = choices[random.randint(0,2)]
    print(f'The computer chose {computerChoice}')
    computerChoice = computerChoice[1].lower()

    if computerChoice == playerChoice:
        print('Its a draw!')
    elif computerChoice == 'r' and playerChoice.lower() == 'p':
        print('Player wins!')
    elif computerChoice == 'p' and playerChoice.lower() == 's':
        print('Player wins!')
    elif computerChoice == 's' and playerChoice.lower() == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')

def main():
    print('Welcome to the rock, paper, scissors game!')
    printRules()
    playGame()
    input('Press enter to exit.')

main()


