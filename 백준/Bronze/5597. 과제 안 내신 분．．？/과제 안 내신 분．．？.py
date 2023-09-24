students = dict(zip([i+1 for i in range(30)], [i+1 for i in range(30)]))


for i in range(28):
    students.pop(int(input()))
for i in students.keys():
    print(i)