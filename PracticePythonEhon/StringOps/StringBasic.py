# Sprit the String
stEx = "Apple,Orange,Fish,Meat"
stExList = stEx.split(',')

print('print the result for stExList')
for x in stExList:
    print(x)
print('******************')

# Join the String
stExJoin = ','.join(stExList)
print('print the result for stExJoin')
print(stExJoin)
print('******************')

# Change the term in String
stEx2 = 'Apple'
stExReplace = stEx2.replace('A', '1: a')
print('print the result for stExReplace')
print(stExReplace)
print('******************')

# Skip learning below items
print('Skip learning below items')
print('find(), index(), count(), st in StringVariable')
print('strip(), upper/lower/title(), str(), len(), ....')