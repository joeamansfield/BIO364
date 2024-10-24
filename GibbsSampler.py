import random

def CreateProfile(motifs):
    length = len(motifs[0])
    profile = [None] * 4
    for i in range(4):
        profile[i] = [1] * length
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

def LoadedRandom(numbers):
    total = sum(numbers)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] / total
    r = random.random()
    for i in range(len(numbers)):
        r = r-numbers[i]
        if r <= 0:
            return i

def RandomKmer(sequence, k):
    r = random.randint(0, len(sequence) - k)
    return sequence[r:r+k]

def ProfileRandomKmer(sequence, profile, k):
    probs = []
    for i in range(len(sequence) - k):
        probs.append(ProbabilityCalc(sequence[i:i+k], profile))
    r = LoadedRandom(probs)
    return sequence[r:r+k]


def GibbsSampler(dna, k, t, N):
    motifs = []
    for sequence in dna:
        motifs.append(RandomKmer(sequence, k))
    bestMotifs = motifs
    for i in range(N):
        j = random.randint(0, t-1)
        profile = CreateProfile([x for y,x in enumerate(motifs) if y!=j])
        motifs[j] = ProfileRandomKmer(dna[j], profile, k)
        if ScoreMotif(motifs) < ScoreMotif(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

k = 8
t = 5
N = 100
sequences = ['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
motifs = GibbsSampler(sequences, k, t, N)
output = "Score: " + str(ScoreMotif(motifs)) + "\n"
for motif in motifs:
    output = output + motif + ' '
print(output)