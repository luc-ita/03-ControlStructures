#6.14
###
#
ean = input('Enter EAN: ')
y = ''
z = 0
for x in ean:
    y = y + x
    z += 1
    if y == '590':
        print('Poland')
        break
    if z > 3:
        break
