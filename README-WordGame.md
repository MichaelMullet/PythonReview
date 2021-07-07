# 6.00wordGame.py
**This program is a more complicated word game that allows us to play against a computer.**

### ps4a.py

Starting off with ps4a.py, we import random and string modules and make some definitions. By defining our VOWELS, CONSONANTS, HAND_SIZE, SCRABBLE_LETTER_VALUES, and WORDLIST_FILENAME, we have a basic set of rules to build our own word game.

Our first function is `loadWords()`, which is similar to the first function of Hangman.py in that it returns our wordList.

Our second function is `getFrequencyDict(sequence)`, which returns the frequency of a value in a sequence.

The third function is `getWordScore(word, n)`, which returns the value of a word according to scrabble letter values. It creates a for loop in the word, and for each letter it determines what its value is in the SCRABBLE_LETTER_VALUES dictionary. The value is added to the wordScore variable and the lettersUsed variable increases by one. The wordScore is then multiplied by the word length, and if all letters are used in the first word, an additional 50 points is awarded.

Next we have the `displayHand(hand)` function. This takes the letters in the hand dictionary defined in the `dealHand(n)` function and prints them out.

The `dealHand(n)` function defines a hand variable as an empty dictionary and establishes that at least a third of the letters in the hand should be vowels. The function populates the hand dictionary with random vowels and consonants from our VOWELS and CONSONANTS variables.

The `updateHand(hand, word)` function returns a copy of the hand that updates as letters are used to input a word. As a letter is added to the word variable, it is subtracted from our hand copy.

The `isValidWord(word, hand, wordList)` function only returns true if the word variable is in the wordList and is entirely composed of letters in the hand.

The `calculateHandlen(hand)` function returns the length (number of letters) in the current hand.

Next up is our `playHand(hand, wordList, n)` function. This is the core function of the program, so everything is explained in the documentation and comments on the code itself. You can view it below:

        def playHand(hand, wordList, n):

            """

            Allows the user to play the given hand, as follows:

            * The hand is displayed.

            * The user may input a word or a single period (the string ".")
            to indicate they're done playing

            * Invalid words are rejected, and a message is displayed asking
            the user to choose another word until they enter a valid word or "."

            * When a valid word is entered, it uses up letters from the hand.

            * After every valid word: the score for that word is displayed,
            the remaining letters in the hand are displayed, and the user
            is asked to input another word.

            * The sum of the word scores is displayed when the hand finishes.

            * The hand finishes when there are no more unused letters or the user
            inputs a "."

            hand: dictionary (string -> int)

            wordList: list of lowercase strings

            n: integer (HAND_SIZE; i.e., hand size required for additional points)

            """

            # Keep track of the total score

            totalScore = 0

            # As long as there are still letters left in the hand:

            while calculateHandlen(hand) > 0:

                # Display the hand

                print('Current Hand:', end = ' ')

                displayHand(hand)

                # Ask user for input

                word = input('Enter word, or a "." to indicate that you are finished: ')

                # If the input is a single period:

                if word == '.':

                    # End the game (break out of the loop)

                    break


                # Otherwise (the input is not a single period):

                else:

                    # If the word is not valid:

                    if not isValidWord(word, hand, wordList):

                        # Reject invalid word (print a message followed by a blank line)

                        print('Invalid word, please try again.')

                        print()

                    # Otherwise (the word is valid):

                    else:

                        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                        totalScore += getWordScore(word, n)

                        print('"' + word + '" earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(totalScore) + ' points')

                        print()

                        # Update the hand

                        hand = updateHand(hand, word)


            # Game is over (user entered a '.' or ran out of letters), so tell user the total score
            if word == '.':

                print('Goodbye! Total score: ' + str(totalScore) + ' points.')

            else:

                print('Run out of letters. Total score: ' + str(totalScore) + ' points.')

            return totalScore

To play an actual game, we have a `playGame(wordList)` function. It creates a while loop that allows the user to input 'n' to play a new (random) hand, 'r' to replay the last hand, or 'e' to exit the game.

### ps4b.py

While ps4a.py ran a perfectly fine game, it doesn't allow the user to play against a computer. That's where ps4b.py comes in. It imports all functions from ps4a.py and adds functions for a computer player.

Our `compChooseWord(hand, wordList, n)` function is the core of our computer player. Given its hand, it will scan the wordList for the word with the best possible score during each round and return the bestWord. This does not necessarily create the best score possible for the whole hand, as the computer cannot be strategic with scores across rounds as it picks words, but it comes close to the best score.

The `compPlayHand(hand, wordList, n)` function is very similar to our `playHand(hand, wordList, n)` function, except it allows for the computer player to play its hand and keep score instead of the user.

Our `playGame(wordList)` function can be updated to include the 'c' option, which allows for the computer to play a hand.

### 6.00wordGame.py

The computer player integration in ps4b.py was not as tight as I wanted it to be, so I created additional functions in a new program with all the old functions imported.

I started off with creating a leaderboard with the `addToLeaderboard(name, Leaderboard)` function. It allows the user to input a name with a score that starts at 0.

Then we have the `showLeaderboard(Leaderboard)` function, which prints out the names and scores within the leaderboard.

Now there is a `gameLoopPlugin(name)` function, which was my modification to the `playGame(wordList)` function, which mostly stays the same otherwise. Quick disclaimer: I did not actually use this function in `playGame(wordList)`, since at the time I couldn't figure out how to call it within the function and make it work. Maybe I will update it as I get better at Python. Instead I copied and pasted the code for the function in two spots, making `playGame(wordList)` more complicated than it has to be.

What the `gameLoopPlugin(name)` function does is allow the user to actually play a hand with the computer player. It also keeps track of the user's high score and updates it in the leaderboard. Finally, it compares the user's score and the computer player's score at the end of a game and determines who won.

I think the code for this word game could definitely be cleaned up and improved upon. However, I am pretty proud of what it is able to do, and I even have fun trying to beat the computer at the game (I've still never won a game against it!). Someday when I am less restricted with time and I'm much more knowledgable and capable with Python, I want to rewrite this program.