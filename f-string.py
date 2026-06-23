name = 'Семен'
mid_name = 'Семенович'
balance = 32.56
text = """Дорогой {n} {m}, баланс вашего лицевого счета составляет {b} руб""".format(b=balance,m=mid_name,n=name)
print(text)
text1 = f"""(Type 2) Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб"""
print(text1)
text2 = f"""(Type 3) Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance *2} руб (X2)"""
print(text2)
text3 = f"""(Type 2) Дорогой {name.lower} {mid_name.upper}, баланс вашего лицевого счета составляет {balance} руб"""
print(text3)