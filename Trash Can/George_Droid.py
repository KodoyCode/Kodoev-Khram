import time
import random

class GeorgeDroid:
    def __init__(self):
        self.reactor_status = "ФЕНТАНИЛ_АКТИВЕН"
        self.breathing = True
        self.oxygen_level = 100 
        self.money_owed = 100  # Янчик, долг растет, счетчик тикает
        self.police_pressure = False
        self.turns = 0 
        
    def check_system(self):
        print("🚨 GeorgeDroid v3.2 [OVERCLOCKED]. Celeron плавит сокет. 🚨")
        print("==================================================")
        
        while self.breathing:
            self.turns += 1
            print(f"--- [ХОД {self.turns}] ---")
            
            # 1. Фентаниловый индастриал-рейв
            if self.reactor_status == "ФЕНТАНИЛ_АКТИВЕН":
                trip_damage = random.randint(3, 8)
                self.oxygen_level -= trip_damage
                print(f"🥴 [СИСТЕМА]: Резонанс ядра. В наушниках ебашит 'Head Like a Hole'. Минус {trip_damage}% ОЗУ.")
                
                # Шанс 10%, что фентанил отпустит (но станет только хуже)
                if random.random() < 0.1:
                    print("💊 [ОТХОДОСЫ]: Фентанил кончился. Началась ломка.")
                    self.reactor_status = "ЛОМКА"
            
            elif self.reactor_status == "ЛОМКА":
                self.oxygen_level -= 5
                print("🥶 [СТАТУС]: Андроида трясет. Требуется доза или сотка от Янчика.")

            # 2. Взаимодействие с агрессивной средой Зажопинска
            if not self.police_pressure:
                action = random.choice(["магаз", "янчик", "залипнуть"])
                
                if action == "магаз":
                    print("💵 [ТРАНЗАКЦИЯ]: Попытка обменять фальшивую сотку на насвай.")
                    if random.random() < 0.65: 
                        print("👮‍♂️ [МЕНТЫ]: Продавец сдал андроида. Колено Шовина активировано!")
                        self.police_pressure = True
                    else:
                        print("🌿 [ПРОФИТ]: Закинулся. Система временно стабилизирована.")
                        self.oxygen_level = min(100, self.oxygen_level + 15)
                        
                elif action == "янчик":
                    print("📱 [ЗВОНОК]: 'Янчик, сука, где сотка сум? Телефон щас сядет!'")
                    rand_val = random.random()
                    if rand_val < 0.25:
                        print("💸 [ЧУДО]: Янчик испугался дебаггера и скинул сотку на карту! ОЗУ восстановлено.")
                        self.money_owed = 0
                        self.oxygen_level = min(100, self.oxygen_level + 30)
                    elif rand_val < 0.6:
                        print("🤬 [ОТКАЗ]: Янчик сказал 'Брат, завтра 100% отдам' и ушел в инвиз. Стресс!")
                        self.oxygen_level -= 15
                    else:
                        print("📞 [СБРОС]: Янчик заблокировал твой номер. У Джорджа подгорел шлейф.")
                        self.oxygen_level -= 25
                
                else:
                    print("🚬 [ПАУЗА]: Андроид просто стоит у падика и смотрит на закат в Узбекистане.")
            
            # 3. Фаза критического давления (Шовин тайм)
            if self.police_pressure:
                damage = random.randint(25, 40)
                self.oxygen_level -= damage
                print(f"🛑 [КРИТ]: Нагрузка на кулер 146%! Минус {damage}% ОЗУ!")
                print(f"🫁 GeorgeDroid: МНЕ НЕ ХВАТАЕТ СВОПА! I CAN'T BREATHE! Своп: {self.oxygen_level}%")
                
            # Проверка на тотальный краш ОС
            if self.oxygen_level <= 0:
                self.breathing = False
                print("\n❌ [КРИТИЧЕСКИЙ СБОЙ]: Стек переполнен. Синий экран смерти (BSOD).")
            else:
                status_money = f"{self.money_owed} сум" if self.money_owed > 0 else "ПРОЩЕНА (НЕТ)"
                print(f"📊 Текущее состояние: Кислород/ОЗУ: {self.oxygen_level}% | Долг Янчика: {status_money}")
                print("⏳ Celeron издает предсмертные звуки, Win 10 висит...\n")
                time.sleep(1.2)
            
        # Эпилог
        print("==================================================")
        print("💀 [КОНЕЦ СЕССИИ]: GeorgeDroid окончательно ушел в swap-файл.")
        if self.money_owed > 0:
            print("✊🏿 [ЗАЖОПИНСК REVOLUTION]: Пацаны разнесли ларёк и пошли бить Янчика за сотку.")
        else:
            print("✊🏿 [ЗАЖОПИНСК REVOLUTION]: Пацаны помянули Джорджа насваем и сдали Celeron на металлолом.")

if __name__ == "__main__":
    droid = GeorgeDroid()
    droid.check_system()
