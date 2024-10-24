import sys
sys.setrecursionlimit(1500)
letters = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
PAMinput = ['A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3',
'C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0',
'D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4',
'E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4',
'F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7',
'G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5',
'H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0',
'I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1',
'K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4',
'L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1',
'M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2',
'N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2',
'P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5',
'Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4',
'R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4',
'S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3',
'T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3',
'V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2',
'W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0',
'Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10']
PAM = {}
for i in range(len(PAMinput)):
    PAMinput[i] = PAMinput[i].split()
    letter = PAMinput[i][0]
    for j in range(len(letters)):
        letter2 = letters[j]
        score = PAMinput[i][j+1]
        PAM[letter+letter2] = int(score)

def lcs_backtrack(v, w):
    s = [None] * (len(v) + 1)
    for i in range(len(s)):
        s[i] = [0] * (len(w) + 1)

    backtrack_1 = []

    for i in range(len(v)+1):
        col = []
        for j in range(len(w)+1):
            col.append(0)
        backtrack_1.append(col)

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            curr_v = v[i-1]
            curr_w = w[j-1]
            curr_pairing = curr_v + curr_w

            deletion = -5
            insertion = -5
            match = PAM[curr_pairing]

            s[i][j] = max(s[i-1][j] + deletion, s[i][j-1] + insertion, s[i-1][j-1] + match)

            current_spot = s[i][j]

            if s[i][j] == s[i-1][j]+ deletion:

                backtrack_1[i][j] = 1
            elif s[i][j] == s[i][j-1]+ insertion:
                backtrack_1[i][j] = 2

            elif s[i][j] == s[i-1][j-1] + match:
                backtrack_1[i][j] = 0

            if s[i][j] < 0:
                s[i][j] = 0
                backtrack_1[i][j] = 3

    return (backtrack_1, s)


def output_lcs(bt, v, w, newSeqv, newSeqw, i, j):
    if bt[i][j] == 3:
        return [newSeqv, newSeqw]

    if (i == 0) & (j != 0):
        newSeqw = w[j-1] + newSeqw
        newSeqv = '-' + newSeqv
        return output_lcs(bt, v, w, newSeqv, newSeqw, i, j-1)

    if (i != 0) & (j == 0):
        newSeqw = '-' + newSeqw
        newSeqv = v[i -1 ] + newSeqv
        return output_lcs(bt, v, w, newSeqv, newSeqw, i-1, j)

    if (i == 0) & (j == 0):
        return [newSeqv, newSeqw]

    if bt[i][j] == 1:
        newSeqv = v[i-1] + newSeqv
        newSeqw = '-' + newSeqw

        return output_lcs(bt, v, w, newSeqv, newSeqw, i-1, j)
    elif bt[i][j] == 2:
        newSeqv =  '-' + newSeqv
        newSeqw = w[j-1] + newSeqw
        return output_lcs(bt, v, w, newSeqv, newSeqw, i, j-1)
    else:
        newSeqv = v[i-1] + newSeqv
        newSeqw = w[j-1] + newSeqw
        return output_lcs(bt, v, w, newSeqv, newSeqw, i-1, j-1)

file = open("D:/OneDrive - BYU/BIO 364/Test Data/dataset_577188_10.txt")

seq1 = file.readline().strip()
seq2 = file.readline().strip()

matrices = lcs_backtrack(seq1, seq2)
maxScore = 0
maxIndices = (-1,-1)
for i in range(len(matrices[1])):
    for j in range(len(matrices[1][0])):
        if matrices[1][i][j] > maxScore:
            maxScore = matrices[1][i][j]
            maxIndices = (i,j)

alignment = output_lcs(matrices[0], seq1, seq2, '', '',maxIndices[0], maxIndices[1])

string = str(maxScore) + '\n' + alignment[0] + '\n' + alignment[1]
print(string)
with open('D:/OneDrive - BYU/BIO 364/Test Data/output.txt', 'w') as f:
    f.write(string)