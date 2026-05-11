#=====================================



a = [1,2,3]
i = iter(a)

print(next(i))
print(next(i))
print(next(i))



#======================================


g = (i for i in range(1, 4))

print(next(g))
print(next(g))
print(next(g))