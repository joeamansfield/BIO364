inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/10.5input.txt'
with open(inPath) as input:
    outcome = input.readline().strip()
    input.readline()
    outcomeAlphabet = input.readline().split()
    input.readline()
    path = input.readline().strip()
    input.readline()
    pathAlphabet = input.readline().split()
    input.readline()
    input.readline() #skip row with ouput columnn names under assumption they are given in same order as alphabet
    matrixdata = input.read().split()
    emission = {}
    alphabetComplete = False
    for cell in matrixdata:
        if cell.isalpha():
            currentLetter = cell
            emission[currentLetter] = []
        else:
            emission[currentLetter].append(float(cell))

def outcomeProbability(path, outcome, emission, outcomeAlphabet):
    probability = 1
    for i in range(len(path)):
        pathChar = path[i]
        outChar = outcome[i]
        emissionProb = emission[pathChar][outcomeAlphabet.index(outChar)]
        probability = probability * emissionProb
    return probability

probability = outcomeProbability(path, outcome, emission, outcomeAlphabet)
output = str(probability)
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)