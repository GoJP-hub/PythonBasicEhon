# First class '絵本'
class Ehon:
    title = '絵本'
    price = 1680

    def costOfBookBy(self, amtNo):
        print(self.title + ':', amtNo, ' books will cost: (YEN)', self.price * amtNo)

    def closeCase(self):
        print('*********************')

# Customer buying Ehon
cust1 = Ehon()
cust1.costOfBookBy(2)
cust1.closeCase()

# Second class--flexible insert
class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p

    def costOfBookBy(self, amtNo):
        print(self.title + ':', amtNo, ' books will cost: (YEN)', self.price * amtNo)

    def closeCase(self):
        print('*********************')

# Customer buying book of their preference
textbook = Book('教科書', 3000)
textbook.costOfBookBy(3)
textbook.closeCase()

# Inheriting the class
class LanguageJap(Book):
    lang = 'Japanese'

    def showLang(self):
        print('the language for ' + self.title + ' is: ' + self.lang)

myText = LanguageJap('歴史書', 2490)
myText.costOfBookBy(1)
myText.showLang()
myText.closeCase()

# Overriding the class
class TitleColor(Book):
    color = 'orange'

    def costOfBookBy(self, amtNo):
        super().costOfBookBy(amtNo)
        print(('color is: ' + self.color))

hisText = TitleColor('Comic', 490)
hisText.costOfBookBy(3)
hisText.closeCase()


