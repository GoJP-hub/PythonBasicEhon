# This is example of using multiple lines via '''
from builtins import print

a = '''Hi
I am writing in multiple lines
in one variable
'''
# This is for using escape sequence
b ='I am using one variable, single line. \n\t However, I am using escape sequences like \\n'
# this is for combining the variables
c1 = 'Summer'
c2 = 'Vacation'
c = c1 + c2
# Display the String like package
d = 'package'
# Repeat the String by *
e = 'hi'
print(a)
print(b)
print(c)
print(d[1] + d[-2])
print(e * 3)

# Unique way to change the words
print('A', 'B', 'C', sep="/", end="--")
print('D')