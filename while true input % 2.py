while True:
    k=(input('Введите число (или exit для выхода): '))
    if k == "exit":
        break
    try:
        k=int(k)
    except:
        "Вводите цифры!"
        continue
    if k%2==0:
        print(f"""Чётное число: {k}""")
    else:
        print(f"""Нечётное число: {k}""")