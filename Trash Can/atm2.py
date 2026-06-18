balance = 5000000
money_list = [1000, 2000, 5000,10000, 20000, 50000, 100000, 200000]
while balance > 0:
    print(f"\nБаланс: {balance}")
    try:
        moneyinput = int(input(f"Сколько вы хотите обналичить? \n{money_list}: "))
        moneymult = int(input(f"Сколько этой купюры вы хотите: {moneyinput} ?: "))
        for i in money_list:
            if
    except TypeError:
        print("Цифры пиши, айтишник недоделанный!")
        money2 = moneyinput * moneymult
        balance -= money2
        print(f"Вы обналичили: {money2}, баланс: {balance}")
    else:
        print("error")