my_os = "windows_10"
ram_gb = int(input("How much RAM you got? "))
if ram_gb == 8:
     print("(мне лень придумать ещё одну фразу, так что просто держи этот текст)")
elif ram_gb <= 8:
    print("Your PC is a shithole, but for python OK")
elif ram_gb <= 4:
    print("Windows XP")
elif ram_gb >= 8:
    print("He has a RAM! Catch him!")
else:
    print("ayoo man wtf")