def BWMatching(lastColumn, pattern, lastToFirst):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol, pattern = pattern[-1], pattern[:-1]
            foundTop = False
            topIndex = None
            bottomIndex = None
            for i in range(top, bottom + 1):
                if lastColumn[i][0] == symbol:
                    if not foundTop:
                        topIndex = i
                        foundTop = True
                    bottomIndex = i
            if not foundTop:
                return 0
            top = lastToFirst[topIndex]
            bottom = lastToFirst[bottomIndex]
        else:
            return bottom - top + 1

#create last to first dictionary to deliver into function
def CreateLastToFirst(lastColumn):
    location = {}
    for i in range(len(lastColumn)):
        char = lastColumn[i]
        if char in location:
            location[char] += 1
        else:
            location[char] = 0
        lastColumn[i] = (char, location[char])
    firstColumn = sorted(lastColumn)
    lastToFirst = {}
    for i in range(len(lastColumn)):
        f = firstColumn.index(lastColumn[i])
        lastToFirst[i] = f
    return lastToFirst

#get input from file
inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/9.10input.txt'
with open(inPath) as input:
    inputs = input.read().split()
BWTText = inputs[0]
patterns = inputs[1:]
lastColumn = []
#break string into an array of characters
for char in BWTText:
    lastColumn.append(char)
lastToFirst = CreateLastToFirst(lastColumn)
numMatches = []

#for testing
firstColumn = sorted(lastColumn)

for pattern in patterns:
    matches = BWMatching(lastColumn, pattern, lastToFirst)
    numMatches.append(matches)
    
    

output = ''
for num in numMatches:
    output += str(num) + ' '
output = output[:-1]
print(output)

#write output to file
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)

