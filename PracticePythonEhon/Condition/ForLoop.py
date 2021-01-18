from builtins import print, range

w = {'月','火','水','木','金'}
for wday in w:
    print(wday)
else:
    print('weekend')

pDict = {'月':'monday','火':'tuesday','水':'wednesday','木':'thursday','金':'friday'}
for keyDic in pDict:
    print(keyDic)
for valDic in pDict.values():
    print(valDic)
for itemDic in pDict.items():
    print(itemDic)
else:
    print('close loop')

for numA in range(7):
    print(numA)
else:
    print('end of loop numA')

for numB in range(10, 5, -1):
    print(numB)
else:
    print('end of loop numB')

for numC in range(20, 31, 2):
    print(numC)
else:
    print('end of loop numC')

liA = list(range(0, 15, 2))
for numD in liA:
    print(numD)
else:
    print('end of loop numD')