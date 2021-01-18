def multBy2(n, t=2):
    x = n * t
    return x


# creating default value in Function
print('print result for multBy2(5))')
print(multBy2(5))
print('*************')


# put function into variable
def printHello(name):
    print('Hello: ', name)


funcHello = printHello
print('print result for funcHello(\'Go\')')
funcHello('Go')
print('*************')


# function defined in the function can be called by parent function only
def printAB():
    def printB():
        print('B')
        print('can call printB() via printAB()')
    print('A')
    printB()

print('print result for printAB()')
printAB()
print('*************')