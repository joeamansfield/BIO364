inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/10.5input.txt'
with open(inPath) as input:
    path = input.readline().strip()
    input.readline()
    tfisthis = input.readline().strip()
    input.readline()
    matrixdata = input.read().split()
    alphabet = []
    transition = {}
    alphabetComplete = False
    for cell in matrixdata:
        if cell not in alphabet and not alphabetComplete:
            alphabet.append(cell)
        else:
            alphabetComplete = True
            if cell.isalpha():
                currentLetter = cell
                transition[currentLetter] = []
            else:
                transition[currentLetter].append(float(cell))

probability = 1/len(alphabet)
for i in range(1, len(path)):
    char = path[i]
    lastChar = path[i-1]
    transitionChance = transition[lastChar][alphabet.index(char)]
    probability = probability * transitionChance

output = str(probability)
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)