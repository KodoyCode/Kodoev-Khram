import random
password = random.randint(1000,9999)
attempts = 0

while True:
    try:
        int1 = int(input(f"Paroldi jazin ({password}): "))
        if int1 == password:
            print(f"Siz paroldi taptiniz!: {password}")
            break
        else:
            attempts += 1
            if attempts >= 4:
                print("Error.")
                print(f"Password: {password}")
                break
            else:
                print(f"Paroldi duris jazin! (attempts: {4 - attempts})")
    except ValueError:
        print("I said, write a number!")
    except Exception as e:
        print(f"Something went wrong, check this out: {e}")