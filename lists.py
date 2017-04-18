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
