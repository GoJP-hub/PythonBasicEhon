from builtins import print

numA = 0
while numA <=5:
    print(numA)
    numA += 1
else:
    print("comp looping numA")

numB = 0
numC = 5
while numB <= 10:
    if (numC - numB) <= 0:
        print("comp looping numB by Break")
        break
    print(numC - numB)
    numB += 1
else:
    print("comp looping numB by while condition")

liD = [1, 3, 5, '七', 9]
for numD in liD:
    if type(numD) == str:
        print(numD, ': is string')
        continue
    print(numD)
else:
    print("comp looping numD")