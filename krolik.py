# krolik.py

print("=== ДОБРО ПОЖАЛОВАТЬ В КОДОЕВ ХРАМ ===")
action = input("Что ты хочешь сделать с кроликом? (beat / eat / hug): ")

if action == "beat":
    # Вот тут срабатывает детонатор:
    raise SyntaxError("Rabbit is too cute to be beaten")

elif action == "eat":
    # И тут тоже детонатор:
    raise SyntaxError("Rabbit is too cute to be eaten")

elif action == "hug":
    print("Красавчик, кролик урчит, Celeron G1620 даже не нагрелся.")

else:
    print("Ты чё ввел, дядя? Янчик, перелогинься.")