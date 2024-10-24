def GenNeighbors(pattern, distance):
    if distance == 0:
        return pattern
    if len(pattern) == 1:
        return ['A','C','G','T']
    neighbors = []
    suffixNeighbors = GenNeighbors(pattern[1:], distance)
    for text in suffixNeighbors:
        if HammingDistance(pattern[1:], text) < distance:
            for nucleotide in ['A','C','G','T']:
                neighbors.append(nucleotide + text)
        else:
            neighbors.append(pattern[0] + text)
    return neighbors

def HammingDistance(pattern, pattern2):
    distance = 0
    for i in range(len(pattern)):
        if pattern[i] != pattern2[i]:
            distance += 1
    return distance

def FrequentWordsWithMismatches(text, k, d):
    patterns = []
    freqDic = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        neighborhood = GenNeighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor in freqDic:
                freqDic[neighbor] += 1
            else:
                freqDic[neighbor] = 1
    m = freqDic[max(freqDic, key=freqDic.get)]
    for key in freqDic:
        if freqDic[key] == m:
            patterns.append(key)
    return patterns

file = open("C:/Users/Joe/Downloads/dataset_577109_9.txt")
sequence = file.readline()
file.close()
#sequence = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 7
d = 3
output = ''
for word in FrequentWordsWithMismatches(sequence, k, d):
    output = output + word + ' '
print(output)
