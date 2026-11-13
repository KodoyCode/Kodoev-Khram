
total_debt = 3000000
try:
    inp = int(input("Сколько Янчик соизволил вернуть сегодня: "))
    if inp == 0:
        print("Продолжаем ждать червей...")
    elif inp > 0:
        awefk = total_debt - inp
        print(f"Остаток долга: {awefk}. Неси остальное, пёс!")
    elif inp < 0:
        print("Янчик, открой, у меня подарок для тебя!")
    else:
        print("ЧО ОН НЕСЁТ СУКА")
except :
    print("ЧО ОН НЕСЁТ СУКА") 