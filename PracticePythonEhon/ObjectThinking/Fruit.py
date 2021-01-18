# class method: call CLASS rather than OBJECT
class Fruit:
    taste = 'おいしい！'

    def __init__(self):
        self.name = 'Fruit'
        self.weight = 0
        self.color = '?'

    def printData(self):
        print('{}:　Color= {}, weight = {} g'.format(self.name, self.color, self.weight))

    def closeCase(self):
        print('*********************')


class Apple(Fruit):
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    @classmethod
    def printTaste(cls):
        print('Sweet and ' + cls.taste)


class Orange(Fruit):
    def __init__(self, weight):
        self.name = 'Orange'
        self.weight = weight
        self.color = 'Orange'

    @classmethod
    def printTaste(cls):
        print('Sour and ' + cls.taste)


# using an instance
fruit = Fruit()
fruit.printData()
fruit.closeCase()

redApple = Apple('Red apple', 280, 'red')
redApple.printData()
redApple.printTaste()
Apple.printTaste()  #class method
redApple.closeCase()

greenApple = Apple('Green apple', 250, 'green')
greenApple.printData()
greenApple.printTaste()
Apple.printTaste()  #class method
greenApple.closeCase()

orange = Orange(160)
orange.printData()
orange.printTaste()
Orange.printTaste()
orange.closeCase()