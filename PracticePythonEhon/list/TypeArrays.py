# 種類：タプル
from builtins import print

a = ('dog', 'cat', 'bird')
print('cannot edit the values in タプル unlike List')
print('cannot call the value in タプル')
# print(a(1))

# 種類：dictionary
b = {1:'リンゴ', 2:'みかん', 3:'イチゴ'}
print('棚の２つ目には、' + b[2])
print('棚の２つ目には、モノが入っているか:', end='')
print(2 in b)
print('棚の４つ目には、モノが入っていないか:', end='')
print(not 4 in b)
print('棚の３つ目には、モノが入っているか:', end='')
print(b.get(3))
# 辞書：代入
b[2] = 'マンダリン'
print('棚の2つ目には、モノは何に変わったか:', end='')
print(b.get(2))
# 辞書：Function→dict()とzip()
d = dict(チョコ = 1, アイス = 2, 仙豆 = 3)
print(d.get('チョコ'))
e1 = ['チョコ', 'アイス', '仙豆']
e2 = [1, 2, 3]
e = dict(zip(e1, e2))
print(e.get('アイス'))

# 辞書: 追加・削除
f = dict(チョコ = 1, アイス = 2, 仙豆 = 3)
f['コーヒー豆'] = 4 # 追加
print(f.get('コーヒー豆'))

del f['チョコ']
f.pop('アイス')
print(f.get('仙豆'))
f.clear() # 中身のみ全部を削除

# 辞書: キーのみ抽出
g = dict(チョコ = 1, アイス = 2, 仙豆 = 3)
keyForG = list(g.keys())
print(keyForG[1])
valueForG = list(g.values())
print(valueForG[2])