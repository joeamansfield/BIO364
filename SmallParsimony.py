import re

class Node: 
    def __init__(self, num):
        self.num = num
        self.leaf = False
        self.left = None
        self.right = None

file = open('D:/OneDrive - BYU/BIO 364/Test Data/test.txt')
n = int(file.readline())
adjacency = file.read().split()
alphabet = ['A', 'C', 'T', 'G']
rootnum = 0
for i in range(len(adjacency)):
    adjacency[i] = re.split(r'->', adjacency[i])
    adjacency[i][0] = int(adjacency[i][0])
    if adjacency[i][0] > rootnum:
        rootnum = adjacency[i][0]
adjacencyDic = {}

for i in range(len(adjacency)):
    node = adjacency[i][0]
    child = adjacency[i][1]
    last = child
    if node not in adjacencyDic:
        adjacencyDic[node] = [child]
    else:
        adjacencyDic[node].append(child)
length = len(adjacency[0][1])
#initialize scores
scores = [None] * (len(adjacency)+1)
for i in range(len(scores)):
    scores[i] = [None] * length
    for j in range(len(scores[i])):
        scores[i][j] = [None] * len(alphabet)
#scores = [[[None] * 4] * length] * (len(adjacency)+1) - this makes later entires to the table duplicate, no idea why
chars = [None] * (len(adjacency)+1)
for i in range(len(chars)):
    chars[i] = [None] * length
sequences = [None] * (len(adjacency)+1)
tags = [0] * (len(adjacency) + 1)

def FillTree(node):
    left = adjacencyDic[node.num][0]
    right = adjacencyDic[node.num][1]
    if left.isnumeric():
        node.left = Node(int(left))
        FillTree(node.left)
        node.right = Node(int(right))
        FillTree(node.right)
    else:
        global n
        n = n-1
        node.left = Node(n)
        sequences[n] = left
        node.left.leaf = True
        adjacencyDic[node.num][0] = n
        n = n-1
        node.right = Node(n)
        sequences[n] = right
        node.right.leaf = True
        adjacencyDic[node.num][1] = n

root = Node(rootnum)
FillTree(root)

def SmallParsimony(node):
    x = node.num
    if node.leaf == True:
        for char in range(len(alphabet)):
            for i in range(length):
                sequence = sequences[x]
                character = alphabet[char]
                if sequence[i] == character:
                    scores[x][i][char] = 0
                else:
                    scores[x][i][char] = 999999999999999999
        tags[x] = 1
        return
    left = node.left
    xL = left.num
    right = node.right
    xR = right.num
    SmallParsimony(left)
    SmallParsimony(right)
    tags[x] = 1
    for i in range(length):
        minscore = 999999999999999999
        minCharL = 0
        minCharR = 0
        for j in range(len(alphabet)):
            minL = 999999999999999999
            charL = 0
            minR = 999999999999999999
            charR = 0
            for k in range(len(alphabet)):
                if j != k:
                    if scores[xL][i][k] < minL:
                        minL = scores[xL][i][k] + 1
                        charL = k
                    if scores[xR][i][k] < minR:
                        minR = scores[xR][i][k] + 1
                        charR = k
                else:
                    if scores[xL][i][k] < minL:
                        minL = scores[xL][i][k]
                        charL = k
                    if scores[xR][i][k] < minR:
                        minR = scores[xR][i][k]
                        charR = k
            score = minL + minR
            if score < minscore:
                minscore = score
                minCharL = charL
                minCharR = charR
            scores[x][i][j] = score
        chars[xL][i] = minCharL
        chars[xR][i] = minCharR
    return
                
SmallParsimony(root)

finalscores = [None] * (len(adjacency)+1)
for i in range(len(scores)):
    seqscore = 0
    for j in range(len(scores[i])):
        min = 999999999999999999
        for k in range(len(scores[i][j])):
            score = scores[i][j][k]
            if score < min:
                min = score
        seqscore = seqscore + min
    finalscores[i] = seqscore

for i in range(len(scores[rootnum])):
    min = 999999999999999999
    for j in range(len(scores[rootnum][i])):
        if scores[rootnum][i][j] < min:
            min = scores[rootnum][i][j]
            chars[rootnum][i] = j

for i in range(len(chars)):
    seq = ''
    for j in range(len(chars[i])):
        seq = seq + alphabet[chars[i][j]]
    sequences[i] = seq
        
def HammingDistance(pattern, pattern2):
    distance = 0
    for i in range(len(pattern)):
        if pattern[i] != pattern2[i]:
            distance += 1
    return distance

newAdjacency = []
for i in range(len(sequences)):
    sequence = sequences[i]
    if i in adjacencyDic:
        otherseqs = adjacencyDic[i]
        for seqdex in otherseqs:
            sequence2 = sequences[int(seqdex)]
            distance = HammingDistance(sequence, sequence2)
            newAdjacency.append([sequence, sequence2, distance])
    else:
        continue
totalMinScore = finalscores[rootnum]
output = str(totalMinScore) + '\n'
outputArray = []
for adjacency in newAdjacency:
    outputArray.append(adjacency[0] + '->' + adjacency[1] + ':' + str(adjacency[2]))
for adjacency in newAdjacency:
    outputArray.append(adjacency[1] + '->' + adjacency[0] + ':' + str(adjacency[2]))
#outputArray.sort()
for path in outputArray:
    output = output + path + '\n'
output = output[:-1]

with open('output.txt', 'w') as f:
    f.write(output)