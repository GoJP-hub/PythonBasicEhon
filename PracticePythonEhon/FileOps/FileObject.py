# basics of file object ops
print("basics of FileObject Ops")
print("common ops for file are:")
print("1) open the file")
print("2) read and write the file")
print("3) close the file")
print('*********************')

# basics of opening the file
print('basics of opening the file')
print('options for file usage: r = read only, w = write new, a = write/add to existing, r+ = read and write')
print('*********************')

# example of reading a file
print('example of reading a file: for loop and Strip')
fileEx = open('HelloGo.txt', 'r',encoding="utf-8_sig")

for readEx in fileEx:
    print(readEx.strip())

fileEx.close()
print('*********************')

# example of reading a file
print('example of reading a file: readline()')
fileEx2 = open('HelloGo.txt', 'r',encoding="utf-8_sig")
line1 = fileEx2.readline()
line2 = fileEx2.readline()
line3 = fileEx2.readline()
print(line1.strip())
print(line2.strip())
print(line3.strip())
fileEx2.close()
print('*********************')

# example of reading a file
print('example of reading a file: read()')
fileEx3 = open('HelloGo.txt', 'r',encoding="utf-8_sig")
print(fileEx3.read())
fileEx3.close()
print('example of reading a file: read(3)')
fileEx3 = open('HelloGo.txt', 'r',encoding="utf-8_sig")
print(fileEx3.read(3))
print(fileEx3.read(3))
fileEx3.close()
print('*********************')

# example of reading a file
print('example of reading a file: readlines()')
fileEx4 = open('HelloGo.txt', 'r',encoding="utf-8_sig")
listFile = fileEx4.readlines()
print(listFile[0].strip())
print(listFile[1].strip())
print(listFile[2].strip())
fileEx4.close()
print('*********************')

# example of reading a file
print('example of reading a file: list()')
fileEx5 = open('HelloGo.txt', 'r',encoding="utf-8_sig")
listFile2 = list(fileEx5)
print(listFile2[0].strip())
print(listFile2[1].strip())
print(listFile2[2].strip())
fileEx5.close()
print('*********************')