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

for i in range(1,rowNum*2,2):
    space = rowNum - int(i/2 +.5)
    star = i
    print(' '*space+'*'*star)

print('E8')

rowNum = input('How many rows do you want the triangle? ')

for i in range(1,rowNum*2,2):
    space = rowNum - int(i/2 +.5)
    star = i
    print(' '*space+'*'*star)

print('E9')

for i in range(1, 11):
    for j in range(1, 11):
        a = i*j
        print('{0} x {1} = {2}'.format(i, j, a))

print('B A N N E R')

msg = input("Please input a message to put in the banner: ")
banTB = []
banMid = []
msg = list(msg)

for i in range(len(msg)+2):
    banTB.append('*')
#Opening Star
banMid.append('*')

for j in range(len(msg)):
    banMid.append(msg[j])

#Closing Star
banMid.append('*')

print(''.join(banTB))
print(''.join(banMid))
print(''.join(banTB))

print('Triangle Numbers')

uTri = input('Enter the Triangle number sequence you want: ')
uTri = int(uTri)

def tri(x):
    return(int(x*(x+1)/2))

tri(uTri)

print('Factors')

def fac(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

uFac = input('Enter the number you want the factors of: ')
uFac = int(uFac)

fac(uFac)
