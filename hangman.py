from random_word import RandomWords
r = RandomWords()

def fillBlanks(array_word, word, guess, solution):
    i=0
    for letter in array_word:
        if letter == guess:
            solution.insert(i, letter)
            print(letter)
        else:
            i+=1
    return solution

word = r.get_random_word()
array_word = word.split(" ")
lives = 7
guessedLetters = []
solution = []
for i in range(0, len(word)):
    solution.append("")

print(f"The word has {len(word)} letters. \n{solution}")
while lives!=0:
    guess = input("\nGuess a letter or word: ")
    for c in guessedLetters:
        if c == guess:
            print(f'{guess} has already been guessed!')
            print(f"Letters guessed: {guessedLetters}")
            solution = fillBlanks(array_word, word, guess, solution)
            print(f"Word: {solution}")
            pass
    if len(guess) == len(word) and guess != word:
        lives-=1
        print(f'Your guess was incorrect, you have {lives} lives remaining.')
        print(f"Letters guessed: {guessedLetters}")
        solution = fillBlanks(array_word, word, guess, solution)
        print(f"Word: {solution}")
        pass
    elif guess == word:
        print('Your guess was correct! You win!')
        break
    if guess not in word:
        lives -=1
        print(f'{guess} was not in the word! You have {lives} lives remaing. ')
        guessedLetters.append(guess)
        print(f"Letters guessed: {guessedLetters}")
        solution = fillBlanks(array_word, word, guess, solution)
        print(f"Word: {solution}")
    else:
        print(f'{guess} was in the word!')
        guessedLetters.append(guess)
        print(f"Letters guessed: {guessedLetters}")
        solution = fillBlanks(array_word, word, guess, solution)
        print(f"Word: {solution}")

if lives == 0:
    print(f"You lose!\nThe word was {word}")
                
                







