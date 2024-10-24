def SuffixArrayConstruction(text):
    dictionary = {}
    for i in range(len(text)):
        dictionary[text[i:]] = str(i)
    dictionary = sorted(dictionary.items())
    dictionary = dict(dictionary)
    vals = list(dictionary.values())
    out = (" ".join(vals))
    return out

file = open("D:/OneDrive - BYU/BIO 364/Test Data/test.txt")
fullFile = file.readlines()
file.close()
output = SuffixArrayConstruction(fullFile[0])

with open('output.txt', 'w') as f:
    f.write(output)