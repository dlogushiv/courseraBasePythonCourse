fileIn = open('5-input.txt', 'r', encoding='utf8')
fileOut = open('5-output.txt', 'w', encoding='utf8')
resList = []
for line in fileIn.readlines():
    resList.append(list(line.split()))
resList.sort()
for st in resList:
    st.pop(2)
    resLine = ' '.join(map(str, st)) + '\n'
    fileOut.write(resLine)
fileIn.close()
fileOut.close()
