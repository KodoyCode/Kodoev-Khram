while True:
    try:
        msg = "Мейсон, цифры, сука, пиши: "
        number = int(input(msg))

        if number == 0:
            print("Мейсон свободен. Допрос окончен.")
            break
        
        print(f"Ты ввел {number}. Резнор недоволен, пиши еще.")
    except ValueError:
        print("ЭТО НЕ ЦИФРЫ, МЕЙСОН! ПОПРОБУЙ ЕЩЕ РАЗ!")