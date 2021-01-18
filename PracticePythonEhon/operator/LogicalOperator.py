# 複雑な条件式
from builtins import print
a = 10
# More than X and Less than Y
print('Equation a: (5 <= a) and (a <= 20)_____', (5 <= a) and (a <= 20))
# Neither X and Y
print('Equation b1: not (a == 0) or not a == 1)_____', not (a == 0) or  (a == 1))
print('Equation b2: not (a == 0) or not a == 1)_____', not (a == 0) and not (a == 1))

# 条件付きの実行
b = 4
(b < 10 ) and (print('b is less than 4. It is condition with --and--, so it will run when it is true'))
(b < 10 ) or (print('b is more than 4. It is condition with --or--, so it will run when it is false'))

# 三項演算子
score = 70
c = 'PASS' if score > 75 else 'FAIL'
print(c)