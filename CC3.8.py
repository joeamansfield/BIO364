def DeBruijn(sequence, k):
    graph = {}
    revGraph = {}
    edges = []
    for kmer in sequence:
        edges.append(kmer)

    for kmer in sequence:
        node = kmer[:-1]
        node2 = kmer[1:]
        graph[node] = []
        revGraph[node2] = []
        for kmer in edges:
            if kmer[:-1] == node:
                graph[node].append(kmer[1:k])
            if kmer[1:] == node2:
                revGraph[node2].append(kmer[:-1])

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
        path = path[index:] + path[:index]
    startNodeIndex = path.index(nodeList[startNode])
    path = path[startNodeIndex:] + path[:startNodeIndex]
    return path


def PathToGenome(path):
    string = path[0]
    for i in range(1,len(path)):
        string = string + path[i][-1]

    return string


def StringReconstruction(Patterns, k):
    list = DeBruijn(Patterns, len(Patterns[0]))
    path = EulerianPath(list[0], list[1])
    text = PathToGenome(path)
    return text


file = open("C:/Users/Joe/Downloads/dataset_577143_7.txt")
k = int(file.readline())
kmers = file.read().split()
output = StringReconstruction(kmers, k)
with open('output.txt', 'w') as f:
    f.write(output)