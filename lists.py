list = [-2, -1, 1, 2, 3, 4, 5, 6]
list2 = [1, 2 ,3]
list3 = [4, 5, 6]
print(list)
print(list2)
print(list3)

print('Exercise 1')

print(sum(list))

print('Exercise 2')
print(max(list))

print('Exercise 3')
print(min(list))

print('Exercise 4')
for x in list:
    if x % 2 == 0:
        print(x)

print('Exercise 5')
for x in list:
    if x > 0:
        print(x)

print('Exercise 6')
posList = []
for x in list:
    if x > 0:
        posList.append(x)
print(posList)

print('Exercise 7')
mList = list2 * 3
print(mList)

print('Exercise 8')
vList = []
x = 0
for index in range(len(list2)):
    y = list2[x] * list3[x]
    vList.append(y)
    x += 1
print(vList)

print('Exercise 9')
l1 = [[2, 4], [2, 2]]
l2 = [[5, 7], [1, 3]]
l3 = []

for x in range(len(l1)):
    row = []
    for y in range(len(l1[x])):
        row.append(l1[x][y] + l2[x][y])
    l3.append(row)

print('Exercise 10')
l1 = [[2, 4, 100], [2, 2, 200]]
l2 = [[5, 7, 400], [1, 3, 300]]
l3 = []

for x in range(len(l1)):
    row = []
    for y in range(len(l1[x])):
        row.append(l1[x][y] + l2[x][y])
    l3.append(row)

print('Exercise 11')

dupe = [1, 1, 2, 2, 3, 3, 4]
deDupe = []

for i in dupe:
    if i not in deDupe:
      deDupe.append(i)
    dupe = deDupe
print(deDupe)

print('Bonus Exercise')
