balance = 5000000
money_list = ["1000", "2000", "5000", "10000", "20000", "50000", ]
money_multiplier
while True:
    
    bankinput = input(f"Сколько сумов вы хотите обналичить? ({money_list})")
    multiplierinput = input(f"Сколько купюр хотите? ({bankinput})")
    money_list = int(money_list)
    if bankinput == money_list:
        