import re

def getWinningArray(lines):
    return list(map(lambda element: [el for el in element.strip().split(" ") if el!=""], re.split(r'[\:\|\n]', "".join(lines))[1::3]))

def getOwnArray(lines):
    return list(map(lambda element: [el for el in element.strip().split(" ") if el != ""], re.split(r'[\:\|\n]', "".join(lines))[2::3]))

def main(filename):
    f = open(filename, "r")

    data = f.readlines()
    winnings = getWinningArray(data)
    own = getOwnArray(data)
    occurences = [1 for i in range(len(data))]
    
    for idCard, winning in enumerate(winnings):
        cardResult = 0
        for winningNb in winning:
            if(winningNb in own[idCard]):
                for time in range(own[idCard].count(winningNb)):
                    cardResult += 1
                    occurences[idCard+cardResult] += occurences[idCard]
        
    return sum(occurences)

print(main(input("filename : ")))