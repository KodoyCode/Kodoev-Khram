#Random ham onin funkcyalari
import random


#randint
'''
san = random.randint(1,10)

print(san)

'''


#randrange
'''
print(random.randrange(1,10))

'''

#Choice
'''
miyweler =['alma','anar','juzim','banan']

print(random.choice(miyweler))

'''


#shuffle
'''
miyweler =['alma','anar','juzim','banan']

random.shuffle(miyweler)

print(miyweler)

'''

#sample
'''
sanlar= [1,2,3,4,5,6,7,8,9]

print(random.sample(sanlar,3))

'''

#random
'''
print(random.random())
'''



#uniform
'''
print(random.uniform(1,10))

'''


#choice
'''
miyweler =['alma','anar','juzim','banan']

print(random.choices(miyweler,k=5))

'''


#seed
'''
random.seed(2)

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

'''

#randrange
'''
san = random.randrange(10,101,5)

print(san)

'''

#choice
'''
print(random.choice([30,50,70]))

'''