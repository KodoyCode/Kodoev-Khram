import time

hungry = True
debtor_status = "morozitsya"  # стандартное состояние Янчика

while hungry:
    try:
        print("[INFO] Чекаем холодильник...")
        fridge_content = check_fridge()
        
        if not fridge_content:
            raise EmptyFridgeException("Мышь повесилась, остался только майонез 2021 года")
            
        eat(fridge_content)
        hungry = False
        print("[SUCCESS] Живот заправлен, можно верстать дивы дальше.")

    except EmptyFridgeException as e:
        print(f"[WARNING] Ошибка: {e}")
        print("[ACTION] Инициируем операцию 'Выбей долг'...")
        
        # Зачем орать в пустоту, когда есть конкретный виновник твоей диеты?
        scream(target="Янчик", reason="ВЕРНИ ДОЛГ НА СОМСУ, ПЕС")
        
        # Пытаемся набрать его с лагающего Samsung A10
        call_yanchik(device="Samsung A10", delay=5)  # 5 сек задержки чисто на лаги интерфейса
        
        if debtor_status == "morozitsya":
            print("[CRITICAL] Янчик скинул трубку. Переходим к пассивному выживанию.")
            drink_kipyatok_with_bread()
            
    finally:
        # Проверка, не сгорел ли проц от таких сложных вычислений
        if cpu_temp > 85:
            print("[PANIC] Селерон закипел, открывай форточку!")
            time.sleep(10)