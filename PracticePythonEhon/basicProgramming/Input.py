import sys
from builtins import input

name = input('Insert direction text--What is your name?: ')
print('Hi. Mr. ' + name)

# Error messages
sys.stdout.write('Standard output \n')
sys.stderr.write('Output error \n')

s1 = sys.stdin.readline()
