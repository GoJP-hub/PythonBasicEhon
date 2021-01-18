from builtins import print
# Format
print('%d' % 3)
print('%d is bigger than %d' % (3, 2))
print('%4d' % 23)
print('%-4d' % 23)
print('%04d' % 23)
# Using teh function Format
a = 123456
b = 789
c = 91
print('the number is {}'.format(a))
print('the format int is {:d}'.format(a))
print('the number a {} and the number b {}'.format(a, b))
print('the number b {1} and the number b {0}'.format(a, b))
print('location of number{:>4}'.format(c))
print('location of number{:<4}'.format(c))
print('location of number{:^4}'.format(c))
print('location of number{:>04}'.format(c))


