miyweler = ["alma", "armut", "protakal"]
it = iter(miyweler)
print(next(it))

def sanoq (n):
      i = 1
      while i <= n:
            yield i
            i += 1

for son in sanoq(5):
      print(son)