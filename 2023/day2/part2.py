
import math
import re

def extractGameId(gameLine: str)->int:
    return int(gameLine.strip().split(":")[0].replace("Game", ""))

def extractGameSet(gameSet: str)->list[int]:
    result = [0, 0, 0]
    gameSetArray = gameSet.split(",")

    for color in gameSetArray:
        if("red" in color):
            result[0] = int(color.replace("red", ""))
        if("green" in color):
            result[1] = int(color.replace("green", ""))
        if("blue" in color):
            result[2] = int(color.replace("blue", ""))
    
    return result

def getGamePower(gameLine: str)->bool:
    gameArray = re.split("[:;]", gameLine.strip())
    minArray = [0, 0, 0]

    for gameSet in gameArray[1:]:
        gameSetColors = extractGameSet(gameSet)

        for i in range(3):
            if(gameSetColors[i]>minArray[i]):
                minArray[i] = gameSetColors[i]
            
    return math.prod(minArray)

def main(filename):
    f = open(filename, "r")
    result = 0
    for gameLine in f:
        result+=getGamePower(gameLine)
    
    return result

print(main(input("filename : ")))