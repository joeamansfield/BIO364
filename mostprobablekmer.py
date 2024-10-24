def NucConvert(n):
    if n == 0:
        return 'A'
    if n == 1:
        return 'C'
    if n == 2:
        return 'G'
    if n == 3:
        return 'T'

def ProbabilityCalc(sequence, profile):
    probability = 1
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            probability = probability * profile[0][i]
        if sequence[i] == 'C':
            probability = probability * profile[1][i]
        if sequence[i] == 'G':
            probability = probability * profile[2][i]
        if sequence[i] == 'T':
            probability = probability * profile[3][i]
    return probability

file = open("C:/Users/Joe/Downloads/dataset_577123_3.txt")
sequence = file.readline()
k = int(file.readline())
profile = [None] * k
profile[0] = file.readline()
profile[1] = file.readline()
profile[2] = file.readline()
profile[3] = file.readline()
profile[0] = profile[0].split()
profile[1] = profile[1].split()
profile[2] = profile[2].split()
profile[3] = profile[3].split()
for i in range(k):
    profile[0][i] = float(profile[0][i])
    profile[1][i] = float(profile[1][i])
    profile[2][i] = float(profile[2][i])
    profile[3][i] = float(profile[3][i])
#mostProbableNucleotides = [None] * k
#for i in range(k):
#    maxProb = 0
#    for j in range(4):
#        if (profile[j][i] == maxProb) & (profile[j][i] != 0):
#            mostProbableNucleotides[i].append(j)
#        if profile[j][i] > maxProb:
#            maxProb = profile[j][i]
#            mostProbableNucleotides[i] = [j]
#mostProbableKmers = []
#tempKmers = []
#for i in range(k):
#    for j in range(len(mostProbableNucleotides[i])):
#        if len(mostProbableKmers) == 0:
#            tempKmers.append(NucConvert(mostProbableNucleotides[i][j]))
#        for l in range(len(mostProbableKmers)):
#            tempKmers.append(mostProbableKmers[l] + NucConvert(mostProbableNucleotides[i][j]))
#    mostProbableKmers = tempKmers
#    tempKmers = []
maxProb = 0
mostProb = ''
for i in range(len(sequence)-k+1):
    kmer = sequence[i:i+k]
    p = ProbabilityCalc(kmer, profile)
    if p > maxProb:
        mostProb = kmer
        maxProb = p
print(mostProb)
        

#kmer = MostProbableKmer(sequence, k)