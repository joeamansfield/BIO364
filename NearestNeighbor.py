file = open('D:/OneDrive - BYU/BIO 364/Test Data/test.txt')
path = file.readline().split()
text = file.read()
adjacency = text.split()
for i in range(len(adjacency)):
    adjacency[i] = adjacency[i].split('->')

first = []
second = []

textArray = []
for i in range(len(adjacency)):
    if adjacency[i][0] == path[0]:
        first.append(adjacency[i][1])
    if adjacency[i][0] == path[1]:
        second.append(adjacency[i][1])

first.remove(path[1])
second.remove(path[0])
arbitrary = first[1]
for i in range(len(second)):
    swapText = second[i]
    new = text.replace(arbitrary, 'PLACEHOLDER')
    new = new.replace(swapText, arbitrary)
    new = new.replace('PLACEHOLDER', swapText)
    textArray.append(new)

output = ''
for i in range(2):
    output = output + textArray[i] + '\n'
output = output[:-1]

with open('output.txt', 'w') as f:
    f.write(output)