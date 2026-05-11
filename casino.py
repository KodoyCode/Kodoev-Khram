import random
import time

def start_casino():
    balance = 100
    print(f"--- ДОБРО ПОЖАЛОВАТЬ В ХРАМ АЗАРТА ---")
    print(f"Твой стартовый капитал: {balance} тугриков. Не профукай.")

    while balance > 0:
        print(f"\nБаланс: {balance}")
        bet = input("Сколько ставишь, смельчак? (или 'exit' чтобы сбежать): ")

        if bet.lower() == 'exit':
            break
        
        try:
            bet = int(bet)
        except:
            print("Цифры вводи, айтишник недоделанный!")
            continue

        if bet > balance:
            print("У тебя столько нет. Янчик в долг не даст.")
            continue

        choice = input("На что ставим? (Красное/Черное/Зеро): ").strip().lower()
        
        # Имитация напряженного ожидания (чтобы игрок успел вспотеть)
        print("Шарик катится...")
        time.sleep(1.5)

        # Тот самый "честный" алгоритм
        # Добавим капельку реальности: Зеро выпадает чуть чаще, если ставка большая? 
        # Ладно, пока оставим честный рандом.
        cells = ['красное'] * 18 + ['черное'] * 18 + ['зеро']
        result = random.choice(cells)

        print(f"ВЫПАЛО: {result.upper()}!")

        if choice == result:
            if result == 'зеро':
                win = bet * 35
                print(f"МАТЕРЬ БОЖЬЯ! ТЫ СОРВАЛ КУШ: {win}!")
            else:
                win = bet
                print(f"Повезло. Забирай свои {win} сверху.")
            balance += win
        else:
            print("Ха! Деньги теперь мои. Приходи еще.")
            balance -= bet

    if balance <= 0:
        print("\nТы банкрот. Иди проси у Янчика, может вернет долг.")
    else:
        print(f"\nУходишь с {balance}? Ну и вали, нам такие осторожные не нужны.")

if __name__ == "__main__":
    start_casino()