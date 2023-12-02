litteralNumbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def extractNumber(line: str) -> int:
    numberArray = []
    for idx in range(len(line)):
        if(line[idx].isnumeric()):
            numberArray.append(line[idx])
            continue
        
        foundLitteralNumber = [litteralNumbers[litteralNumber] for litteralNumber in litteralNumbers.keys() if line[idx:].find(litteralNumber)==0]
        if(len(foundLitteralNumber)>0):
            numberArray.append(foundLitteralNumber[0])
    
    return int(numberArray[0]+numberArray[-1])

def main(filename):
    f = open(filename, "r")
    result = 0
    for line in f:
        result += extractNumber(line)
    
    return result

print(main(input("filename : ")))