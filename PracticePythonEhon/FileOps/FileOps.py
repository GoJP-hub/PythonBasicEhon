# example of write a file
print('example of create/write a file: write()')
fileExW = open('GreetingGo.txt', 'w',encoding="utf-8_sig")
writeEx = fileExW.write('Good evening.\nGo.\n')
fileExW.close()
print('show created file: read()')
fileExR = open('GreetingGo.txt', 'r',encoding="utf-8_sig")
print(fileExR.read())
fileExR.close()
print('*********************')

# example of write a file: with
print('example of create/write a file using With: write()')
with open('GreetingGo2.txt', 'w', encoding='utf-8_sig') as fileExW2:
    fileExW2.write('Good morning.\nGo.\n')

print('example of read a file using With: strip()')
with open('GreetingGo2.txt', 'r', encoding='utf-8_sig') as fileExR2:
    for readEx in fileExR2:
        print(readEx.strip())