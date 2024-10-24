inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/10.7input.txt'
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
for i in range(len(outcome)):
    pathProbabilities.append([])
    for j in range(len(pathAlphabet)):
        pathProbabilities[i].append(None)
for i in range(len(outcome)):
    currentOutput = outcome[i]
    currentOutputIndex = outcomeAlphabet.index(currentOutput)
    for j in range(len(pathAlphabet)):
        toChar = pathAlphabet[j]
        if i == 0:
            prob = 1/len(pathAlphabet) * emission[toChar][currentOutputIndex]
            pathProbabilities[i][j] = prob
        else:
            totalprob = 0
            trace = pathAlphabet[0]
            for k in range(len(pathAlphabet)):
                fromChar = pathAlphabet[k]
                prob = pathProbabilities[i-1][k]
                prob *= transmission[fromChar][j]
                prob *= emission[toChar][currentOutputIndex]
                totalprob += prob
            pathProbabilities[i][j] = totalprob


probability = 0
for i in range(len(pathProbabilities[-1])):
    probability += pathProbabilities[-1][i]
output = str(probability)
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)