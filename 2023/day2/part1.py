
import re

limits = [12, 13, 14]

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

def isPossible(gameLine: str)->bool:
    gameArray = re.split("[:;]", gameLine.strip())

    for gameSet in gameArray[1:]:
        gameSetColors = extractGameSet(gameSet)

        for i in range(3):
            if(gameSetColors[i]>limits[i]):
                return False
            
    return True

def main(filename):
    f = open(filename, "r")
    result = 0
    for gameLine in f:
        if(isPossible(gameLine)):
            result += extractGameId(gameLine)
    
    return result

print(main(input("filename : ")))