def BetterBWMatching(firstOccurence, lastColumn, pattern, count):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if lastColumn[top:bottom + 1].__contains__(symbol):
                top = firstOccurence[symbol] + count[symbol][top]
                bottom = firstOccurence[symbol] + count[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1

#creates a dictionary linking characters to the index of their first occurence in the first column
def CreateFirstOccurence(lastColumn):
    firstOccurence = {}
    firstColumn = sorted(lastColumn)
    for i in range(len(firstColumn)):
        char = firstColumn[i][0]
        if char not in firstOccurence:
            firstOccurence[char] = i
    return firstOccurence

def CreateCounts(lastColumn, alphabet):
    counts = {}
    for letter in alphabet:
        counts[letter] = [0]
    for i in range(len(lastColumn)):
        char = lastColumn[i][0]
        for letter in alphabet:
            if letter == char:
                counts[letter].append(counts[letter][-1] + 1)
            else:
                counts[letter].append(counts[letter][-1])
    return counts



inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/9.11input.txt'
with open(inPath) as input:
    inputs = input.read().split()

BWTText = inputs[0]
#BWTText = 'smnpbnnaaaaa$$a'
patterns = inputs[1:]
lastColumn = []
#break string into an array of characters
for char in BWTText:
    lastColumn.append(char)
#modidy array to store tuples with char and position
lastColumnNonTuple = lastColumn.copy()
location = {}
for i in range(len(lastColumn)):
    char = lastColumn[i]
    if char in location:
        location[char] += 1
    else:
        location[char] = 0
    lastColumn[i] = (char, location[char])
#create first occurence dictionary
firstOccurence = CreateFirstOccurence(lastColumn)
#alphabet makes creating counts dictionary easier
alphabet = list(firstOccurence.keys())
#create counts dictionary
counts = CreateCounts(lastColumn, alphabet)
output = ''
for pattern in patterns:
    bwmatch = BetterBWMatching(firstOccurence, lastColumnNonTuple, pattern, counts)
    output += str(bwmatch) + ' '
output = output[:-1]
print(output)


outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)