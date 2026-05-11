fruits = ["apple", "banana", "АК-47"]
it = iter(fruits)
print(next(it))



def a(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for b in a(5):
    print(b)
    
    
