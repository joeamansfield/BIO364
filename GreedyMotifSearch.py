def CreateProfile(motifs):
    length = len(motifs[0])
    profile = [None] * 4
    for i in range(4):
        profile[i] = [0] * length
    for motif in motifs:
        for i in range(length):
            base = motif[i]
            match base:
                case 'A':
                    profile[0][i] += 1
                case 'C':
                    profile[1][i] += 1
                case 'G':
                    profile[2][i] += 1
                case 'T':
                    profile[3][i] += 1
    for i in range(4):
        for j in range(length):
            profile[i][j] = profile[i][j] / len(motifs)
    return profile

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

def ScoreMotif(motifs):
    score = 0
    numMotifs = len(motifs)
    length = len(motifs[0])
    count = [None] * 4
    for i in range(4):
        count[i] = [0] * length
    for motif in motifs:
        for i in range(length):
            base = motif[i]
            match base:
                case 'A':
                    count[0][i] += 1
                case 'C':
                    count[1][i] += 1
                case 'G':
                    count[2][i] += 1
                case 'T':
                    count[3][i] += 1
    for i in range(length):
        column = []
        for j in range(4):
            column.append(count[j][i])
        score = score + numMotifs - max(column)
    return score

def GreedyMotifSearch(dna, k, t): #array of multiple dna sequences, kmer length, number of dna sequences?
    bestMotifs = []
    #initialize first set of motifs
    for sequence in dna:
        bestMotifs.append(sequence[:k])
    firstSequence = dna[0]
    #runs this loop for each kmer in the first DNA string
    for i in range(len(firstSequence)-k+1):
        motifs = []
        motifs.append(firstSequence[i:i+k])
        for i in range(1,t):
            profile = CreateProfile(motifs)
            ithSequence = dna[i]
            mostProb = ithSequence[:k]
            maxProb = 0
            for j in range(len(ithSequence)-k+1):
                kmer = ithSequence[j:j+k]
                p = ProbabilityCalc(kmer, profile)
                if p > maxProb:
                    mostProb = kmer
                    maxProb = p
            motifs.append(mostProb)
        if ScoreMotif(motifs) < ScoreMotif(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

file = open("C:/Users/Joe/Downloads/dataset_577123_5.txt")
variables = file.readline().split()
k = int(variables[0])
t = int(variables[1])
sequences = file.readline().split()
motifs = GreedyMotifSearch(sequences, k, t)
output = ''
for motif in motifs:
    output = output + motif + ' '
print(output)