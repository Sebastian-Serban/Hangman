from random import choice

words = ['coder', 'decoder', 'recoder', 'recorder', 'encoder', 'python', 'palton', 'program', 'reprogram']

word = choice(words)

guessed, lives, gameover = [], 7, False

guesses = ['_ ']*len(word)

while not gameover:
    hiddenword = ''.join(guesses)
    print("Your guessed letters are: {}".format(guessed))
    print("Word to guess is: {}".format(hiddenword))
    print("You have {} more tries!".format(lives))

    answer = input("Type 'quit' to leave the game or a letter to guess! \n").lower()
    letter = answer[0]

    if answer=='quit':
        print("Thank you for the game!")
        gameover = True
    elif letter in word and letter not in guessed:
        print("  You guessed correctly!")
        for i in range(len(word)):
            if word[i] == letter:
                guesses[i] = letter
    elif letter in guessed:
        print("Letter {} was already guessed!".format(letter))
    else:
        lives = lives - 1
        print("  Wrong choice! you lost a life")
    
    if letter not in guessed:
        guessed.append(letter)

    if lives < 1:
        gameover = True
    elif word == ''.join(guesses):
        print("Congrats! You guessed the word. It was {}".format(word))
        gameover = True