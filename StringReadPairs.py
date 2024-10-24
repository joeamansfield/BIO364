import re

def DeBruijn(reads, k):
    graph = {}
    revGraph = {}
    for i in range(len(reads)):
        read = reads[i]
        frontNode = (read[0][:-1], read[1][:-1])
        if not frontNode in graph:
            graph[frontNode] = [(read[0][1:], read[1][1:])]
        else:
            graph[frontNode].append((read[0][1:], read[1][1:]))
        backNode = (read[0][1:], read[1][1:])
        if not backNode in revGraph:
            revGraph[backNode] = [(read[0][:-1], read[1][:-1])]
        else:
            revGraph[backNode].append((read[0][:-1], read[1][:-1]))
        #for j in range(len(reads)):
        #    edge = reads[j]
        #    if frontNode == (edge[0][:-1], edge[1][:-1]):
        #        graph[frontNode].append((edge[0][1:], edge[1][1:]))
        #    if backNode == (edge[0][1:], edge[1][1:]):
        #        revGraph[backNode].append((edge[0][:-1], edge[1][:-1]))
    return [graph, revGraph]

def EulerianPath(adjList, revList):
    keys1 = list(adjList.keys())
    keys1 = keys1 + list(revList.keys())

    nodeList = list(set(keys1))
    nodeList.sort()

    nodeDifference = [0] * len(nodeList)

    for i in range(len(nodeList)):
        nodeIn = 0
        nodeOut = 0
        if nodeList[i] in adjList:
            nodeOut = len(adjList[nodeList[i]])
        if nodeList[i] in revList:
            nodeIn = len(revList[nodeList[i]])
        nodeDifference[i] = nodeIn - nodeOut

    endNode = nodeDifference.index(max(nodeDifference))
    startNode = nodeDifference.index(min(nodeDifference))

    if not nodeList[endNode] in adjList:
        adjList[nodeList[endNode]] = [nodeList[startNode]]
    else:
        adjList[nodeList[endNode]].append(nodeList[startNode])
    firstKey = list(adjList.keys())[0]
    path = [adjList[firstKey][0]]
    adjList[firstKey].remove(path[0])

    hasValuesLeft = True
    while hasValuesLeft:
        while True:
            currentNode = path[-1]
            if len(adjList[currentNode]) > 0:
                newNode = adjList[currentNode][0]
                adjList[currentNode].remove(newNode)
                path.append(newNode)
            else:
                break

        hasValuesLeft = False
        newStart = nodeList[endNode]
        for key in adjList:
            if len(adjList[key]) > 0:
                hasValuesLeft = True
                newStart = key
                break
        index = path.index(newStart)
        path = path[index+1:] + path[:index+1]
    startNodeIndex = path.index(nodeList[startNode])
    path = path[startNodeIndex:] + path[:startNodeIndex]
    return path


def PathToGenome(path, k, d):
    genomeStart = path[0][0]
    genomeEnd = path[0][1]
    pathLength = len(path)
    for i in range(1,pathLength):
        genomeStart = genomeStart + path[i][0][-1]
        genomeEnd = genomeEnd + path[i][1][-1]
    genome = genomeStart[:k+d] + genomeEnd
    return genome

def StringReconstruction(Reads, k, d):
    list = DeBruijn(Reads, k)
    path = EulerianPath(list[0], list[1])
    text = PathToGenome(path, k, d)
    return text


file = open('D:/OneDrive - BYU/BIO 364/Test Data/dataset_577186_5.txt')
numbers = file.readline().split()
k = int(numbers[0])
d = int(numbers[1])
readPairs = file.read().split()
for i in range(len(readPairs)):
    readPairs[i] = tuple(re.split(r"\|", readPairs[i]))
output = StringReconstruction(readPairs, k, d)
with open('D:/OneDrive - BYU/BIO 364/Test Data/output.txt', 'w') as f:
    f.write(output)