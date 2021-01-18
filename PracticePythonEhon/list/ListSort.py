num = [50, 1, 3, 100]
# Ops for sorting
print('num[0] is: ', end=' ')
print(num[0])
num.sort()
print('after sort, num[0] is: ', end=' ')
print(num[0])
num.sort(reverse=True)
print('after sort in reverse, num[0] is: ', end=' ')
print(num[0])
# creating new list using sorted
num2 = sorted(num)
print('recreate list bia sortED(), num2[0] is: ', end=' ')
print(num2[0])