try:
    with open('tryReading.txt', 'r', encoding='utf-8_sig') as fileEx:
        for readEx in fileEx:
            print(readEx.strip())
except FileNotFoundError:
    print('File not present')
except Exception as e:
    print(e.args)
