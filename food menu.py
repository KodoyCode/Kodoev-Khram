menu={
    "Palaw": 25000,
    "Shashlik": 30000,
    "Somsa": 8000
}

buyirtqa=input('ne zakaz beresiz?: ')

sena = menu.get(buyirtqa,"Bunday awqat menyuda joq")

print(f"siz tanlagan awqat: {buyirtqa}, senasi: {sena}")
