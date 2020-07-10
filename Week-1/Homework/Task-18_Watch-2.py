inNumber = int(input())
inSeconds = inNumber % (24 * 60 * 60)
hours = inSeconds // (60 * 60)
minutes = (inSeconds - hours * 60 * 60) // 60
seconds = inSeconds % 60
print(hours, minutes, seconds, sep=':')
