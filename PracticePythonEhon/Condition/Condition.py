a = 3
print("what is a: ")

if a % 2 == 0:
    print(a, " is even.")
else:
    print(a,  " is odd.")

if 0 <= a & a <= 9:
    print(a, " is 1 digit.")
elif 10 <= a & a <= 99:
    print(a, " is 2 digits.")
else:
    print(a, ' is more than 2 digit')