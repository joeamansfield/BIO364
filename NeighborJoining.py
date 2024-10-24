file = open("D:/OneDrive - BYU/BIO 364/Test Data/test.txt")

def NeighborMatrix(matrix):
    sums = []
    n = len(matrix)
    for i in range(n):
        sum = 0
        for value in matrix[i]:
            sum = sum + value
        sums.append(sum)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (n-2)*matrix[i][j] - sums[i] - sums[j]
    for i in range(n):
        matrix[i][i] = 0
    return matrix

def NeighborJoining(matrix):
    n = len(matrix)
    neighbor = NeighborMatrix(matrix)
    mini = 0
    minj = 0
    minval = 0
    for i in range(n):
        for j in range(n):
            if neighbor[i][j] < minval:
                minval = neighbor[i][j]
                mini = i
                minj = j
    newMatrix
n = file.readline().strip()
data = file.read()
data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split('\t')
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
matrix = NeighborMatrix(data)
print('n')


