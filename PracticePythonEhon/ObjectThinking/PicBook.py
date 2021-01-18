# property (capsulation)
class PicBook:
    def __init__(self, t, p):
        self.title = t
        self.__price = p

    def getPrice(self):
        return self.__price

    def setPrice(self, p):
        self.__price = p

    def delPrice(self):
        self.__price = 0

    price = property(fget=getPrice, fset=setPrice, fdel=delPrice, doc='価格プロパティ')

    def costOfBookBy(self, amtNo):
        print(self.title + ':', amtNo, ' books will cost: (YEN)', self.price * amtNo)

    def closeCase(self):
        print('*********************')


picBook = PicBook('絵本1', 2000)
picBook.costOfBookBy(1)
picBook.price = 3000
print(picBook.price)
del(picBook.price)
print(picBook.price)
picBook.closeCase()

class TextBook:
    def __init__(self, t, p):
        self.title = t
        self.__price = p

    @property
    def price(self):
        # setting property and getter
        return self.__price

    @price.setter
    def price(self, p):
        self.__price = p

    @price.deleter
    def price(self):
        self.__price = 0

    def costOfBookBy(self, amtNo):
        print(self.title + ':', amtNo, ' books will cost: (YEN)', self.price * amtNo)

    def closeCase(self):
        print('*********************')

histBook = TextBook('US Hist', 5900)
histBook.costOfBookBy(2)
histBook.price = 1000
histBook.costOfBookBy(1)
del(histBook.price)
histBook.costOfBookBy(1)
histBook.closeCase()


