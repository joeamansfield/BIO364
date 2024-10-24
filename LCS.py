import sys
sys.setrecursionlimit(1500)
def MakeMatrix(len1, len2):
    matrix = [None] * (len1 + 1)
    for i in range(len(matrix)):
        matrix[i] = [None] * (len2 + 1)
        for j in range(len(matrix[i])):
            if i == 0 or j == 0:
                matrix[i][j] = [0, 'source']
            else:
                matrix[i][j] = [sys.maxsize, '']
    return matrix

def FillMatrix(matrix, seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    for i in range(1,len1+1):
        for j in range(1, len2+1):
            max = matrix[i][j-1][0]
            direction = 'down'
            if matrix[i-1][j][0] > max:
                max = matrix[i-1][j][0]
                direction = 'right'
            if seq1[i-1] == seq2[j-1] and matrix[i-1][j-1][0] + 1 > max:
                max = matrix[i-1][j-1][0] + 1
                direction = 'diagonal'
            matrix[i][j] = [max, direction]
    return matrix

def Backtrack(matrix, i, j, common):
    direction = matrix[i][j][1]
    match direction:
        case 'source':
            return common
        case 'down':
            j = j - 1
        case 'right':
            i = i - 1
        case 'diagonal':
            j = j - 1
            i = i - 1
            common = seq1[i] + common
    return Backtrack(matrix, i, j, common)
    


file = open('D:/OneDrive - BYU/BIO 364/Test Data/dataset_577186_5.txt')
seq1 = file.readline()
seq2 = file.readline()
matrix = MakeMatrix(len(seq1), len(seq2))
matrix = FillMatrix(matrix, seq1, seq2)
common = Backtrack(matrix, len(seq1), len(seq2), '')
with open('D:/OneDrive - BYU/BIO 364/Test Data/output.txt', 'w') as f:
    f.write(common)