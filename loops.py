print('E1')

for x in range(10):
    x += 1
    print(x)

print('E2')

s = input('Enter a number to start with: ')
e = input('Enter a number to finish on: ')
s = int(s)
e = int(e)
ran = e - s + 1
if s < e:
    for x in range(ran):
        print(s)
        s += 1
elif s==e:
    print('E N D')
else:
    print('Starting number must be smaller than ending number!')

print('E3')

for x in range(10):
    if x % 2 == 1:
        print(x)

print('E4')

for x in range(5):
    print('*****')

print('E5')

square = input('How big is the square? ')
square = int(square)
row = []
for x in range(square):
    row.append('*')

rowDisp = ''.join(row)

for x in range(square):
    print(rowDisp)

print('E6')

box = input('How big is the box? ')
box = int(box)
row = []
rowCap = []
for x in range(box):
    rowCap.append('*')
for x in range(box):
    if x == 0:
        row.append('*')
    elif x == box - 1:
        row.append('*')
    else:
        row.append(' ')

rowDisp = ''.join(row)
rowCapDisp = ''.join(rowCap)

print(rowCapDisp)

for x in range(box-2):
    print(rowDisp)

print(rowCapDisp)

print('E7')
# tri = []
rowNum = 4

for i in range(rowNum+1):
    space = rowNum - (i + 1)
    print((' ' * space + ('*' * (i+1))))

#i=1 3 space 1 star rownum is 4, to get 3 spaces rownum - 1
#i=3 2 space 3 star rownum is 4, to ger 2 spaces rownum - 2
#i=5 1 space 5 star rownum is 4, to get 1 space rownum - 3
#i=7 0 space 7 star

for i in range(1,rowNum*2,2):
    space = rowNum - int(i/2 +.5)
    star = i
    print(' '*space+'*'*star)

    #i=1 3 space 1 star
    #i=2 1 space 3 star
