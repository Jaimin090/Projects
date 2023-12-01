#CreateGolfFile.py
def main():
    golfScoresFile = open('golf.txt', 'w')
    numberPlayers = int(input('Enter number of players: '))
    for count in range(1, numberPlayers+1):
        playerName = input('Enter name of player number ' + str(count) + ': ')
        playerScore = input('Enter score of player number ' + str(count) + ': ')
        golfScoresFile.write(playerName + ',' + str(playerScore) + '\n')
    golfScoresFile.close()

if __name__ == "__main__":
    main()
