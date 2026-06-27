#TAPSIRMA:
'''
kompyuter random 9 xanali san harip ham belgilerden quralgan
1 martelik paroldi jaratadi ham oni paydalaniwshiga beredi
ham paydalaniwshidan 1 martelik paroldi teriwin soraydi
paydalaniwshi 1 martlik paroldi tergenneson duris bolsa durisdesin,
eger qate bolsa parol ozgersin ham ol paydalaniwshiga korsetilsin
eger 1 martelik paroldi duris terse parol jane ozgersin ham ol paydalanwishiga berilsin.

PAYDALANATUGUN FUNKCYALAR:
shart operatorlari
random funkcyalari
list ham onin funkcyalari
input,append,extend,sort while...

'''
import random

# Буквы (arip)
a = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


b = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']


c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


vse = []
vse.extend(a)
vse.extend(b)
vse.extend(c)


vse.sort()

print("--- OTP Generator Baslandi ---")

while True:
    spisok = []
    

    while len(spisok) < 9:
        znak = random.choice(vse)
        spisok.append(znak)
    

    parol = "".join(spisok)
    
    print(f"\nSizdin bir martelik paroliniz: {parol}")
    
    vvod = input("Paroldi kiritin: ")
    
    if vvod == parol:
        print("Duris!")
        print("Parol ozgeredi, jana parol kutin...")
    else:
        print("Qate!")
        print("Parol qate bolgani ushin ozgerdi!")