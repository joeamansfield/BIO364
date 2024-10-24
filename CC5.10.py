import blosum as bl

import sys
sys.setrecursionlimit(1500)

def lcs_backtrack(v, w):
    global mat
    s = []
    penalty = 0
    init = []
    for i in range(len(w)+1):
        init.append(penalty)
        penalty = penalty - 5
    s.append(init)
    penalty = -5
    for i in range(len(v)):
        col = []
        col.append(penalty)
        penalty = penalty -5
        for j in range(len(w)):
            col.append(0)
        s.append(col)

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
            match = mat[curr_pairing]

            s[i][j] = max(s[i-1][j] + deletion, s[i][j-1] + insertion, s[i-1][j-1] + match)

            current_spot = s[i][j]

            if s[i][j] == s[i-1][j]+ deletion:

                backtrack_1[i][j] = 1
            elif s[i][j] == s[i][j-1]+ insertion:
                backtrack_1[i][j] = 2

            elif s[i][j] == s[i-1][j-1] + match:
                backtrack_1[i][j] = 0

    return (backtrack_1, s[-1][-1])


def output_lcs(bt, v, w, newSeqv, newSeqw, i, j):
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

file = open("D:/OneDrive - BYU/BIO 364/Test Data/dataset_577188_3.txt")
mat = bl.BLOSUM(62)

seq1 = file.readline().strip()
seq2 = file.readline().strip()

emptySeq1 = ''
emptySeq2 = ''

back_t = lcs_backtrack(seq1, seq2)
score = int(back_t[1])
alignment = output_lcs(back_t[0], seq1, seq2, emptySeq1, emptySeq2,len(seq1), len(seq2))

string = str(score) + '\n' + alignment[0] + '\n' + alignment[1]
print(string)
with open('D:/OneDrive - BYU/BIO 364/Test Data/output.txt', 'w') as f:
    f.write(string)


