import time
import random
b=[1,2,3,4,5]
a = 0
while a < 500:
    a += random.choice(b)
    print(f"Now the flowers will grow: {a}")
    time.sleep(0.1)
print("That's the ticket.")