# krolik_pro.py

action = "eat"

if action == "eat":
    # Кортеж: (имя_файла, номер_строки, смещение_символа, текст_строки)
    error_info = ("krolik_pro.py", 15, 12, "shashlik.cook(victim=rabbit)")
    raise SyntaxError("Rabbit is too cute to be eaten", error_info)