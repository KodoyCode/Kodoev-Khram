import random
a = [1,2,3,4,5,6,7,8,9]
b = random.choice(a)
c = random.choice(a)
d = random.choice(a)
while True:
    e = int(input("Birinshi san jazin: "))
    f = int(input("Ekinshi san jazin: "))
    g = int(input("Ushinshi san jazin: "))
    if e == b:
        print(b)
    else:
        print("*")
    if f == c:
        print(c)
    else:
        print("*")
    if g == d:
        print(d)
    else:
        print("*")
    if e == b and f == c and g == d:
        print("Siz hamme sanlardi taldiniz!")
        break
    else:
        print("* bolip turgan sanlardi talin!")