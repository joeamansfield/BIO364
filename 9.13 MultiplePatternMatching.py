

inPath = 'D:/OneDrive - BYU/BIO 364/Test Data/9.13input.txt'
with open(inPath) as input:
    inputs = input.read().split()

output = ''
output = output[:-1]
print(output)


outPath = 'output.txt'
with open(outPath, 'w') as out:
    out.write(output)