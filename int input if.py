a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=a
if b>a:
    c=b
print(a)
print(b)
print(c)

if b>a:
    a,b=b,a
print(a,b)