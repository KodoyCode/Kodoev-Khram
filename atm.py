import random
pul = int(input("Sheshipalajaq sammanizdi jazin: "))
kupyuralar = [1000 , 2000 , 5000 , 10000 , 20000 , 50000 , 100000 , 200000]
for i in kupyuralar:
    if pul >= i:
        sani = random.randint(0 , pul // i)
        pul -= sani * i
        print(i , "somliq kupyuradan" , sani , "dana shiqti")
if pul > 0:
    print("Qalgan summani sheshiwdin ilaji joq" , pul)