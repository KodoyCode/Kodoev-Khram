while True:
    k=(input('Введите число (или exit для выхода): '))
    if k == "exit":
        break
    try:
        k=int(k)
    except:
        "Вводите цифры!"
        continue
    if k%2==0 and k%3==0:
        print(f"""Условие (трёхкратное чётное) верное: {k}""")
    else:
        print(f"""Условие (трёхкратное чётное) неверное: {k}""")