# Declare list variable
from builtins import print

a = [0, 1, 2]
# Print the value in list
print(a[0])
print(a[1])
# Replacing value in the list
a[0] = 'zero'
a[2] = 'two'
print(a[0])
print(a[2])

# Find the number of values in the list
lenNo = len(a)
print(lenNo)

# Assert whether specific value is in the list
chkVal = 'two' in a
print(chkVal)

# Reinserting values in list
a = list('ABCDE')
print(a[1])
print(a[4])

# Insert values in the list: add the new item is append(), add in specific location is insert(x, y)
b = [1, 2, 3, 4, 5]
b.append(6)
b.insert(2, 'c')
print(b[5])
print(b[2])

# Combine two lists
c = a + b

d = ['o', 'k']
d += a
d.extend(b)
