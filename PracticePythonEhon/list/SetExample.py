# Creating set (集合)
a = {'Apple', 'Banana', 'Cucumber'}
li = [1, 2, 3]
b = set(li)
print(len(b))
print('Apple' in a)

# set: operator
c = {'Apple', 'Donuts', 'Egg'}
d = a & c
e = a.intersection(c)
print(d == e)

f = a | c
g = a.union(c)
print(f == g)

h = a - c
i = a.difference(c)
print(h == i)

j = a ^ c
k = a.symmetric_difference(c)
print(j == k)

l = c <= a
m = b.issubset(a)
print(l == m)
