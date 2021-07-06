# Hangman.py
**This program is a hangman word game! Guess the letters to a random word before your chances run out.**

We begin by importing the "random" module which will allow us to generate pseudo-random numbers.
WORDLIST_FILENAME is a global variable defined by the hangmanWords.txt file.

Let's create a function called loadwords() which will return a list of valid words to be used by other functions.

        def loadwords():

            print("Loading word list from file...")

            inFile = open(WORDLIST_FILENAME, 'r')

            line = inFile.readline()

            wordlist = line.split()

            print("  ", len(wordlist), "words loaded.")

            return wordlist

This function performs operations to open, read, find the number of words, and return our .txt file.

Let's make a couple more functions that will be used in our hangman() function.

        def chooseWord(wordlist):

            return random.choice(wordlist)

This function chooses a random word from our .txt file prepared by the loadwords() function.

        def isWordGuessed(secretWord, lettersGuessed):

            for i in secretWord:

                if i not in lettersGuessed:

                    return False

            return True

This function determines if secretWord (chosen by chooseword(wordlist)) has been guessed or not.

        def getGuessedWord(secretWord, lettersGuessed):

            str1 = ''

            for i in secretWord:

                if i in lettersGuessed:

                    str1 += i

                else:

                    str1 += '_ '

            return str1

This function returns a string comprised of letters and underscores that represents what letters in secretWord
have been guessed so far.

        def getAvailableLetters(lettersGuessed):

            import string

            remainingLetters = string.ascii_lowercase

            for i in lettersGuessed:

                remainingLetters = remainingLetters.replace(i, '')

            return remainingLetters

This function returns a string of letters that have not yet been guessed. It removes the letters that have been guessed.

        def hangman(secretWord):

            print('Welcome to the game Hangman!')

            print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')

            numGuesses = 8

            lettersGuessed = []

            allGuessedLetters = []

To start this function, we introduce the player to the game and reveal the length of the word that will be guessed.
The player has 8 guesses to make. We define two lists, comprised of lettersGuessed (which will be filled by the getAvailableLetters function), and allGuessedLetters.

            while numGuesses > 0:

                print('-------------')

                print('You have ' + str(numGuesses) + ' guesses left')

                print('Available letters: ' + str(getAvailableLetters(allGuessedLetters)))

                userLetter = input('Please guess a letter: ')

Our while loop will continue running until our number of guesses run out. With each iteration, the player is shown the number of guesses left, the available letters to guess from, and a prompt to input their next guess.

            if userLetter in allGuessedLetters:

                print('Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWord, lettersGuessed)))

            elif userLetter in secretWord:

                lettersGuessed.append(userLetter)

                allGuessedLetters.append(userLetter)

                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))

                if isWordGuessed(secretWord, lettersGuessed) == True:

                    print('-------------')

                    print('Congratulations, you won!')

                    break

If the input variable is already in allGuessedLetters, let the player know they've already guessed it.
And if the player guesses a letter in the chosen word, that letter is added to lettersGuessed and allGuessedLetters.
The player sees where that letter fits into the word. If the full word is guessed, the player wins the game!

            else:

                numGuesses -= 1

                allGuessedLetters.append(userLetter)

                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))

                if numGuesses < 1:

                    print('-------------')

                    print('Sorry, you ran out of guesses. The word was ' + str(secretWord))

If the player's guess is wrong, the number of guesses decreases by one and the letter is added to allGuessedLetters.
The player sees that the guess is wrong. If the number of guesses decreases to 0, the player loses the game and the
word is revealed.

        secretWord = chooseWord(wordlist).lower()

        hangman(secretWord)

Lastly, we define secretWord and run the hangman(secretWord) function. The while loop runs as long as there are guesses left!