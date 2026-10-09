my_os = "windows_10"
ram_gb = int(input("How much RAM you got? "))
if ram_gb == 8:
     print("(i'm too lazy to add more phrases, so take this text)")
elif ram_gb <= 8:
    print("Your PC is a shithole, but for python OK")
elif ram_gb <= 4:
    print("Windows XP")
elif ram_gb >= 8:
    print("He has a RAM! Catch him!")
else:
    print("ayoo man wtf")