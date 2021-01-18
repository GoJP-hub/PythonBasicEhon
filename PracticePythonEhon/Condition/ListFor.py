liA = [1, 2, 3, 4]
liB = []
for numA in liA:
    liB.append(numA * 2)
else:
    print('value insert is completed')

liC = [numB*2 for numB in liA]

for numB in liB:
    print(numB)
else:
    print('comp display for LiB. Should be same with LiC')

for numC in liC:
    print(numC)
else:
    print('comp display for LiC. Should be same with LiB')