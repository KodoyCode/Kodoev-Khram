text=input(": ")

shifrlaw=lambda harip:chr(ord(harip)+3) if harip.isalpha() else harip

jasirin_soz=''.join(list(map(shifrlaw,text)))

print(f"Shifrlangan cod: {jasirin_soz}")