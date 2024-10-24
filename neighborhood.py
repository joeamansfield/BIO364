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


sequence = "CAATCCCG"
distance = 3
output = ''
for neighbor in GenNeighbors(sequence, distance):
    output = output + neighbor + ' '
print(output)