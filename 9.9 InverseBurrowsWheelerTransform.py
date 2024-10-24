def InverseBurrowsWheeler(string):
    lastChars = []
    firstChars = []

    #break string into an array of characters
    for char in string:
        lastChars.append(char)

    #append location index to characters
    location = {}
    for i in range(len(lastChars)):
        char = lastChars[i]
        if char in location:
            location[char] += 1
        else:
            location[char] = 0
        lastChars[i] = (char, location[char])

    firstChars = sorted(lastChars)

    #create output using first-last property + rotations
    outString = ''
    currentChar = firstChars[0]
    for i in range(len(firstChars)):
        index = lastChars.index(currentChar)
        currentChar = firstChars[index]
        outString += currentChar[0]
    return outString

inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/9.9input.txt'
with open(inPath) as input:
    transform = input.readline().strip()
#transform = 'TTCCTAACG$A'
output = InverseBurrowsWheeler(transform)
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)