import random
while True:
    a = [1,2,3,4,5,6,7,8,9]
    b = 1
    c = 2
    d = 3
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
    else:
        print("* bolip turgan sanlardi talin!")