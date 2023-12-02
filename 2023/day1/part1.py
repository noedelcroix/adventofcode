def extractNumber(line: str) -> int:
    numberArray = [char for char in line if char.isnumeric()]
    return int(numberArray[0]+numberArray[-1])

def main(filename):
    f = open(filename, "r")
    result = 0
    for line in f:
        result += extractNumber(line)
    
    return result

print(main(input("filename : ")))