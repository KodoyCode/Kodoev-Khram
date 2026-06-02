try:
    number = int(input("Write a number: "))
    if number == 666:
        raise Exception ("GG, THE SCRIPT IS MINED!!!")
    print(f"You wrote a number: {number}")
except ValueError:
    print("THAT'S NOT A NUMBER")
except Exception as e:
    print(f"Something went wrong, check this out: {e}")