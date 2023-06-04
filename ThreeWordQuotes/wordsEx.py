import random
import time
from threeWordList import threeWordsList

def randomSen():
    rnd = random.randint(0, len(threeWordsList) - 1)
    selectedSen = threeWordsList[rnd]
    print(selectedSen)
    return selectedSen

def main():
    selectedSen = randomSen()
    blankSen = ['_' * len(word) for word in selectedSen]
    startTime = time.time()
    userPoints = 0

    while blankSen != selectedSen:
        currentTime = time.time()
        elapsedSeconds = currentTime - startTime
        print(elapsedSeconds)
        usrInput = input("Enter a letter: ").lower()
        update = False

        for i in range(len(selectedSen)):
            for j in range(len(selectedSen[i])):
                if selectedSen[i][j].lower() == usrInput:
                    blankSen[i] = blankSen[i][:j] + usrInput + blankSen[i][j + 1:]
                    update = True
                    userPoints += 5

        if not update:
            print("Wrong!!! Try Again")
            userPoints -= 1

        if selectedSen[0][0] != '_':
            blankSen[0] = blankSen[0][0].upper() + blankSen[0][1:]

        print(blankSen)

    if elapsedSeconds <= 30 and blankSen == selectedSen:
        userPoints += 100
        print('WOWWW less than 30 seconds?! +100 points!')

    print(f'Good Job! You scored {userPoints} points!')

main()
