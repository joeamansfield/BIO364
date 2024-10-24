inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/10.8input.txt'
with open(inPath) as input:
    inputArray = input.read().split('--------')
threshold = float(inputArray[0].strip())
alphabet = inputArray[1].split()
alignment = inputArray[2].split()
proteinLength = len(alignment[0])
skip = []
for i in range(proteinLength):
    missing = 0
    for protein in alignment:
        if protein[i] == '-':
            missing += 1
    missing = missing/len(alignment)
    if missing > threshold:
        skip.append(i)
nodes = ['S', 'I0']
for i in range(proteinLength - len(skip)):
    x = str(i+1)
    nodes.append('M' + x)
    nodes.append('D' + x)
    nodes.append('I' + x)
nodes.append('E')
transmission = {}
emission = {}
for node in nodes:
    transmission[node] = []
    for counter in nodes:
        transmission[node].append(0)
    emission[node] = []
    for letter in alphabet:
        emission[node].append(0)
for protein in alignment:
    previous = 0
    section = 0
    for i in range(proteinLength):
        mod = 3
        if  i in skip:
            if protein[i] != '-': #insert
                mod = 1
            else:
                continue
        else:
            section += 1
            if protein[i] != '-': #match
                mod = -1
            else: #delete
                mod = 0
        previousNode = nodes[previous]
        dex = (section) * 3 + mod
        transmission[previousNode][dex] += 1
        if protein[i] != '-':
            emission[nodes[dex]][alphabet.index(protein[i])] += 1
        previous = dex
        if i == proteinLength - 1:
            transmission[nodes[previous]][-1] += 1

for node in transmission:
    total = 0
    for i in range(len(transmission[node])):
        total += transmission[node][i]
    if total > 0:
        for i in range(len(transmission[node])):
            if transmission[node][i] != 0:
                transmission[node][i] = round(transmission[node][i]/total, 3)

for node in emission:
    total = 0
    for i in range(len(emission[node])):
        total += emission[node][i]
    if total > 0:
        for i in range(len(emission[node])):
            if emission[node][i] != 0:
                emission[node][i] = round(emission[node][i]/total, 3)

output = ''
for node in nodes:
    output += '\t' + node
for node in transmission:
    output += '\n' + node
    for edge in transmission[node]:
        output += '\t' + str(edge)
output += '\n--------\n'
for letter in alphabet:
    output += '\t' + letter
for node in emission:
    output += '\n' + node
    for edge in emission[node]:
        output += '\t' + str(edge)
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)