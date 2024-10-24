class Node: 
    def __init__(self):
        self.character = None
        self.children = []
        self.leaf = 0
        self.num = 0

def BuildTrie(patterns):
    root = Node()
    numNodes = 0
    for pattern in patterns:
        patternLength = len(pattern)
        currentNode = root
        for i in range(patternLength):
            currentChar = pattern[i]
            foundNode = False
            for node in currentNode.children:
                if node.character == currentChar:
                    currentNode = node
                    foundNode = True
                    break
            if not foundNode:
                currentNode.children.append(Node())
                currentNode = currentNode.children[-1]
                currentNode.character = currentChar
                numNodes += 1
                currentNode.num = numNodes
            if i == (patternLength - 1):
                currentNode.leaf += 1 
    return root

def BuildAnswer(node):
    list = []
    if len(node.children) > 0:
        for child in node.children:
            childList = BuildAnswer(child)
            list = list + childList
            list[-1] = (node.num, list[-1][1], list[-1][2])
    list.append((None, node.num, node.character))
    return list

inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/test.txt'
with open(inPath) as input:
    patterns = input.read().split()

root = BuildTrie(patterns)
answer = BuildAnswer(root)
answer = answer[:-1]
output = ''
for path in answer:
    strPath = str(path[0]) + " " + str(path[1]) + " " + str(path[2]) + '\n'
    output += strPath
output = output[:-1]
outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)