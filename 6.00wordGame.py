from ps4b import *

#LEADERBOARD_FILENAME = "leaderboard.txt"

#def loadLeaderboard():
#    inFile = open(LEADERBOARD_FILENAME, 'r')


def addToLeaderboard(name, leaderboard):
    while True:
        name = input('Enter your name: ')
        if name == '':
            print('That is not a valid name.')
        elif name not in leaderboard:
            leaderboard[name] = 0
            print('Welcome, ' + name + '!')
            print()
            break
        else:
            print('Hey ' + name + ', welcome back!')
            print()
            break
    return name


def showLeaderboard(leaderboard):
    print('Leaderboard:')
    for key, value in leaderboard.items():
        print(key, value)


def gameLoopPlugin(name):
    print()
    while True:
        playerChoice = input('Enter u to have yourself play, c to play with computer: ')
        if playerChoice == 'u':
            totalScore = playHand(hand, wordList, HAND_SIZE)
            if totalScore > leaderboard[name]:
                leaderboard[name] = totalScore
                print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
            break
        elif playerChoice == 'c':
            print('Your turn:')
            totalScore = playHand(hand, wordList, HAND_SIZE)
            if totalScore > leaderboard[name]:
                leaderboard[name] = totalScore
                print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
            print()
            print('Computer\'s turn:')
            compTotalScore = compPlayHand(hand, wordList, HAND_SIZE)
            if totalScore == compTotalScore:
                print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                print('You tied with the computer!')
            elif totalScore > compTotalScore:
                print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                print('You just beat the computer, great job!')
            else:
                print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                print('You lost. Better luck next time!')
            break
        else:
            print('Invalid command.')
    print()


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    gameCount = 0
    while True:
        name = input('Enter your name: ')
        if name == '':
            print('That is not a valid name.')
        elif name not in leaderboard:
            leaderboard[name] = 0
            print()
            print('Welcome, ' + name + '!')
            print()
            break
        else:
            print()
            print('Hey ' + name + ', welcome back!')
            print()
            break
    while HAND_SIZE >= 0:
        gameLoop = input('Enter n to deal a new hand, r to replay the last hand, l to view leaderboard, p to add new player, or e to end game: ')
        if gameLoop == 'n':
            hand = {}
            hand = dealHand(HAND_SIZE)
            print()
            while True:
                playerChoice = input('Enter u to have yourself play, c to play with computer: ')
                if playerChoice == 'u':
                    totalScore = playHand(hand, wordList, HAND_SIZE)
                    if totalScore > leaderboard[name]:
                        leaderboard[name] = totalScore
                        print()
                        print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
                    break
                elif playerChoice == 'c':
                    print('Your turn:')
                    totalScore = playHand(hand, wordList, HAND_SIZE)
                    if totalScore > leaderboard[name]:
                        leaderboard[name] = totalScore
                        print()
                        print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
                    print()
                    print('Computer\'s turn:')
                    compTotalScore = compPlayHand(hand, wordList, HAND_SIZE)
                    if totalScore == compTotalScore:
                        print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                        print('You tied with the computer!')
                    elif totalScore > compTotalScore:
                        print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                        print('You just beat the computer, great job!')
                    else:
                        print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                        print('You lost. Better luck next time!')
                    break
                else:
                    print('Invalid command.')
            print()
            gameCount += 1
        elif gameLoop == 'r':
            if gameCount == 0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                print()
                while True:
                    playerChoice = input('Enter u to have yourself play, c to play with computer: ')
                    if playerChoice == 'u':
                        totalScore = playHand(hand, wordList, HAND_SIZE)
                        if totalScore > leaderboard[name]:
                            leaderboard[name] = totalScore
                            print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
                        break
                    elif playerChoice == 'c':
                        print('Your turn:')
                        totalScore = playHand(hand, wordList, HAND_SIZE)
                        if totalScore > leaderboard[name]:
                            leaderboard[name] = totalScore
                            print('Wow ' + name + ', you beat your high score! You new high score is: ' + str(totalScore))
                        print()
                        print('Computer\'s turn:')
                        compTotalScore = compPlayHand(hand, wordList, HAND_SIZE)
                        if totalScore == compTotalScore:
                            print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                            print('You tied with the computer!')
                        elif totalScore > compTotalScore:
                            print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                            print('You just beat the computer, great job!')
                        else:
                            print('You scored ' + str(totalScore) + ', and the computer scored ' + str(compTotalScore) + '.')
                            print('You lost. Better luck next time!')
                        break
                    else:
                        print('Invalid command.')
                print()
        elif gameLoop == 'l':
            showLeaderboard(leaderboard)
        elif gameLoop == 'p':
            addToLeaderboard(name, leaderboard) #bug: does not update score for any player but first one
        elif gameLoop == 'e':
            break
        else:
            print('Invalid command.')



leaderboard = {}    # want to locate this on a word document for permanent storage
name = ''
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)