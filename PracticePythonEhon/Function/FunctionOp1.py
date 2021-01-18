def addTwoVal(a, b):
    x = a + b
    return x


y = addTwoVal(1, 2)

print('print result for addTwoVal(1, 2)')
print(y)
print('*************')


def subTwoVal(a, b):
    x = a - b
    return x


z = subTwoVal(b=2, a=4)
print('print result for subTwoVal(b = 2, a = 4)')
print(z)
print('*************')


# by タプル
def getAverage(*averg):
    sum = 0
    for x in averg:
        sum += x
    return sum/len(averg)


print('print result for getAverage(1, 2, 3, 4, 5))')
print('Average: ', getAverage(1, 2, 3, 4, 5))
print('*************')

# by 辞書
def printDictionary(**items):
    for s, t in items.items():
        print(s, ':', t)

print('print result for printDictionary(a=\'Apple\', b=2, c=\'orange\')')
printDictionary(a='Apple', b=2, c='orange')
print('*************')


