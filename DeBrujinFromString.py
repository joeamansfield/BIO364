def Composition(sequence, k):
    composition = []
    for i in range(len(sequence) - k + 1):
        composition.append(sequence[i:i+k])
    return composition

#def GenomeFromPath(path):
#    genome = path[0]
#    for i in range(1, len(path)):
#        genome = genome + path[i][-1]
#    return genome

file = open("C:/Users/Joe/Downloads/dataset_577139_6.txt")
variables = file.read().split()
k = int(variables[0])
sequence = variables[1]
kmers = Composition(sequence, k)
kmers.sort()
debrujin = {}

#add all prefixes as dictionary keys
for kmer in kmers:
    debrujin[kmer[:-1]] = []

#if a kmer has a given prefix, add its postfix to the dictionary
for prefix in debrujin.keys():
    for kmer in kmers:
        if prefix == kmer[:-1]:
            debrujin[prefix].append(kmer[1:])
    debrujin[prefix].sort()

#output formatting
output = ''
for prefix in debrujin.keys():
    output = output + prefix + ' -> '
    for postfix in debrujin[prefix]:
        output = output + postfix + ','
    output = output[:-1] + '\n'

with open('output.txt', 'w') as f:
    f.write(output)

hasValuesLeft = True
path = [dic.keys()[0]]
while hasValuesLeft:
    while True:
        currentNode = path[-1]
        if len(dic[currentNode]) > 0:
            newNode = dic[currentNode][0]
            path.append(newNode)
            dic[path[currentNode]] = dic[path[currentNode]].remove(newNode)
        else:
            break

    hasValuesLeft = False
    newStart = ''
    for key in dic:
        if len(dic[key]) > 0:
            hasValuesLeft = True
            newStart = key
            break
    index = path.index(newStart)
    path = path[index:].append(path[:index])