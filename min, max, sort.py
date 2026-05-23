import random
a = [random.randint(1,100) for i in range(10)]
print(a)
print(max(a))
print(min(a))
a.sort()
print(a) 