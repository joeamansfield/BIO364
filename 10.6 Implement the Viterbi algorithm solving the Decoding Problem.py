inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/10.6input.txt'
with open(inPath) as input:
    inputArray = input.read().split('--------')
outcome = inputArray[0].strip()
outcomeAlphabet = inputArray[1].split()
pathAlphabet = inputArray[2].split()
transmissionMatrixData = inputArray[3].strip()
transmissionMatrixData = transmissionMatrixData[transmissionMatrixData.find('\n'):].split()
transmission = {}
for cell in transmissionMatrixData:
    if cell.isalpha():
        currentLetter = cell
        transmission[currentLetter] = []
    else:
        transmission[currentLetter].append(float(cell))
emissionMatrixData = inputArray[4].strip()
emissionMatrixData = emissionMatrixData[emissionMatrixData.find('\n'):].split()
emission = {}
for cell in emissionMatrixData:
    if cell.isalpha():
        currentLetter = cell
        emission[currentLetter] = []
    else:
        emission[currentLetter].append(float(cell))
pathProbabilities = []
backtrack = []
for i in range(len(outcome)):
    pathProbabilities.append([])
    backtrack.append([])
    for j in range(len(pathAlphabet)):
        pathProbabilities[i].append(None)
        backtrack[i].append(None)
for i in range(len(outcome)):
    currentOutput = outcome[i]
    currentOutputIndex = outcomeAlphabet.index(currentOutput)
    for j in range(len(pathAlphabet)):
        toChar = pathAlphabet[j]
        if i == 0:
            prob = 1/len(pathAlphabet) * emission[toChar][currentOutputIndex]
            pathProbabilities[i][j] = prob
            backtrack[i][j] = 'S'
        else:
            maxprob = 0
            trace = pathAlphabet[0]
            for k in range(len(pathAlphabet)):
                fromChar = pathAlphabet[k]
                prob = pathProbabilities[i-1][k]
                prob *= transmission[fromChar][j]
                prob *= emission[toChar][currentOutputIndex]
                if prob > maxprob:
                    maxprob = prob
                    trace = fromChar
            pathProbabilities[i][j] = maxprob
            backtrack[i][j] = trace


probability = 0
lastLetter = None
for i in range(len(pathProbabilities[-1])):
    if pathProbabilities[-1][i] > probability:
        probability = pathProbabilities[-1][i]
        lastLetter = pathAlphabet[i]
output = lastLetter
backIndex = pathAlphabet.index(lastLetter)
for i in range(len(backtrack)):
    lastLetter = backtrack[len(backtrack) - i - 1][pathAlphabet.index(lastLetter)]
    output = lastLetter + output
output = output[1:]
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)