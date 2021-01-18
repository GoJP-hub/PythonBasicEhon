from builtins import print

drink = ['tea', 'coffee', 'soda', 'beer']
# ops for deleting
print('location for drink[1] is: ' + drink[1])
drink.pop(1)
print('After popping by index 1, location for drink[1] is: ' + drink[1])
drink.remove('soda')
print('After removing by name soda, location for drink[1] is: ' + drink[1])
drink.append('coke')
drink.append('water')
del drink[1]
print('After deleting by index 1, location for drink[1] is: ' + drink[1])

# dividing the list
drink2 = drink
boy1, boy2, girl1 = drink2
print('boy1 has: ' + boy1)
print('boy2 has: ' + boy2)
print('when dividing, value in list and variable must be one-to-one')