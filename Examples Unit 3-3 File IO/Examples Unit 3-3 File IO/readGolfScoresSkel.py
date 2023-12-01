#readGolfScoresSkel.py
def main():
    golfScoresFile = open('golf.txt', 'r')
    totalscore =0
    counter =0 

    for line in golfScoresFile:
        playerdata=line.rstrip().split(',')
        playername=playerdata[0]
        playerscore=int(playerdata[1])
        totalscore += playerscore
        counter+=1
        print("player :",playername,"score",playerscore)
    golfScoresFile.close()
    average=totalscore/counter
    print("average score is", average)
if __name__ == "__main__":
    main()