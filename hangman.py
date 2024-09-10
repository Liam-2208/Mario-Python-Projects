from random_word import RandomWords
r = RandomWords()

word = r.get_random_word()
array_word = word.split("")
lives = 7
guessedLetters = []
solution = []
for i in range(0, len(word)):
    solution.append("")

print("The word has {len(word)} letters. \n{solution}")
while lives<=7:
    guess = input("\nGuess a letter or word: ")
    if guess in guessedLetters == True:
        print(f'{guess} has already been guessed!')
        pass
    if guess != word:
        lives-=1
        print(f'Your guess was incorrect, you have {lives} lives remaining.')
    elif guess == word:
        print('Your guess was correct! You win!')
        break
    if letter not in word:
        lives -=1
        print(f'{guess} was not in the word! You have {lives} lives remaing. ')
        guessedLetters.append(guess)
    else:
        print(f'{guess} was in the word!')
        guessedLetters.append(guess)
        for letter in word_array:
            if letter == guess:
                
                







