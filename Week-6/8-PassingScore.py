fileIn = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')
# k = int(input())
students = []
for line in fileIn:
    students.append(tuple(map(str, line.split())))
print(students)

for i in range(len(students)):
    if int(students[i][2])<40 or int(students[i][3])<40 or int(students[i][4])<40:
        students.pop(i)
        i-=1
    else:

print(students)
