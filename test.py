word = 'TAATGCCATGGGATGTT'
words = []
for i in range(len(word)-7):
    threetwomer = word[i:i+3] + '|' + word[i+5:i+8]
    words.append(threetwomer)
output = ''
words.sort()
for worde in words:
    output = output + '(' + worde + ') '
print(output)