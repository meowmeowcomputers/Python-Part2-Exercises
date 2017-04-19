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
