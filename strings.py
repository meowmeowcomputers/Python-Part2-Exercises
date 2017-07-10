print('E1')
'lowercase string'.upper()

print('E2')
'lowercase string'.title()

print('E3')
'reverse string'[::-1]

print('E4')
p = input("Enter your paragraph here: ")
lp = list(p.upper())
#'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O':'0', 'S':'5', 'T':'7'
elim = []
for x in range(len(lp)):
    if lp[x] == 'A':
        elim.insert(x, '4')
    elif lp[x] == 'E':
        elim.insert(x, '3')
    elif lp[x] == 'G':
        elim.insert(x, '6')
    elif lp[x] == 'I':
        elim.insert(x, '1')
    elif lp[x] == 'O':
        elim.insert(x, '0')
    elif lp[x] == 'S':
        elim.insert(x, '5')
    elif lp[x] == 'T':
        elim.insert(x, '7')
    else:
        elim.insert(x, lp[x])


print(''.join(elim))

print('E5')
#Exercise 5: Increasing letter pairs to five 
s = input("Enter your string here: ")
s = list(s)
p = []

for x in range(len(s)):
    if s[x:x+1] == s[x+1:x+2]:
        #s.insert(x, s[x])
        #holder = s[x]+s[x]+s[x]+s[x]+s[x]
        p.insert(x, s[x]*4)
        #p.insert(x, holder)
        #s.insert(x, holder+holder+holder+holder+holder)
    else:
        p.insert(x, s[x])

print(''.join(p))

print('E6')
#Exercise 6: Caesar Cipher
rot = input('How many spaces do you want to rotate by using the Caesar Cipher? ')

def caesar(rot):
    ide = input('Enter Ceasar cipher here: ')
    ide = ide.upper()
    ide = list(ide)
    out = []
    outTxt = []

    for x in range(len(ide)):
        out.insert(x, ord(ide[x])-rot)
        if out[x] < 65:
            out[x] = out[x] + 26

    for y in range(len(out)):
        out[y] = chr(out[y])

    print(''.join(out))
#    outTxt.insert(chr(out[y]))
