file = open("C:/Users/Joe/Downloads/dataset_577108_10.txt")
sequence = file.read()
skew = 0
minskew = 0
minskewpos = []
for i in range(len(sequence)):
    if sequence[i] == 'C':
        skew -= 1
    if sequence[i] == 'G':
        skew += 1
    if skew == minskew:
        minskewpos.append(i+1)
    if skew < minskew:
        minskew = skew
        minskewpos = [i+1]
print(minskewpos)