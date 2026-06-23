a={
    "Ati":"Timur",
    "Familiya":"Nurlanov"
}

print(a.keys())
print(a.values())
print(a.items)

print(type(a))

jana_magliwmat={"jasi":30,"rayoni":"Nokis"}
a.update(jana_magliwmat)

print(a)

list=a.pop("jasi")

print(f"Oshirilgen magliwmat: {list}")

company={
    "dasturshi":{"ati":"Asxat","tili":"Python","tajriybesi":3},
    "dasturshi":{"ati":"Begis","tili":"Java","tajriybesi":1}
}

for dev,magliwmat in company.items:
    print(f"ID:{dev}-> Ati: {magliwmat["ati"]},Dasturlew tili: {magliwmat}")