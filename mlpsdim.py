import os
import random
import sys
import time

# Подрубаем поддержку ANSI-цветов в терминале Windows 10
os.system("")

# Проверяем Windows для мгновенного ввода без нажатия Enter
try:
    import msvcrt

    WINDOWS_OS = True
except ImportError:
    WINDOWS_OS = False

# Цветовая палитра зажопинского киберпанка
C_RESET = "\033[0m"
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_PINK = "\033[95m"
C_CYAN = "\033[96m"
C_WHITE = "\033[97m"
C_BOLD = "\033[1m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_key():
    """Считывает нажатие клавиши в реальном времени."""
    if WINDOWS_OS:
        ch = msvcrt.getch()
        try:
            return ch.decode("utf-8").lower()
        except UnicodeDecodeError:
            return ""
    else:
        return sys.stdin.read(1).lower()


def explosion_animation():
    """Легендарная магия взрыва во имя дружбы."""
    frames = [
        f"""
{C_YELLOW}
                  .---.
                 /     \\
                ( () () )  <-- "ДРУЖБА — ЭТО БОМБА!"
                 \\  ^  /
                  '---'
{C_RESET}""",
        f"""
{C_YELLOW}
               .---.  *  .
            * /     \\   *
           ( ()  ()  )   💥
            *\\   ^  /  *
           .  '---'   .
{C_RESET}""",
        f"""
{C_RED}{C_BOLD}
             \\  :  /
          '.  _ _  .'
        -=  (     )  =-   БАБАХ НАХУЙ!
          .'  ~ ~  '.
             /  :  \\
{C_RESET}""",
        f"""
{C_RED}{C_BOLD}
            .-'''''-.
          .'  * * *  '.
         :  BOOOOOOM!  :
          '.  * * *  .'
            '-.....-'
               |||
               |||
{C_RESET}""",
        f"""
{C_WHITE}{C_BOLD}
             _ . - = - . _
         . "  *  *  *  *  " .
       /   САМОУНИЧТОЖЕНИЕ   \\
      |       УСПЕШНО!        |
       \\   ДОЛГ СПИСАН!      /
         ' . _ _ _ _ _ . '
               | | |
               | | |
              /     \\
{C_RESET}""",
    ]

    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.35)


class PiggyGame:

    def __init__(self, width=30, height=12):
        self.width = width
        self.height = height
        self.px = width // 2
        self.py = height // 2
        self.magic = 0
        self.max_magic = 100
        self.score = 0
        self.debt_collected = 0
        self.game_over = False

        # Генерируем лут и врагов
        self.tnt = []
        self.debts = []
        self.enemies = []

        self.spawn_stuff()

    def spawn_stuff(self):
        # Спавним тротил дружбы (*)
        for _ in range(5):
            self.tnt.append(
                [
                    random.randint(1, self.width - 2),
                    random.randint(1, self.height - 2),
                ]
            )

        # Спавним заначки Янчика ($)
        for _ in range(3):
            self.debts.append(
                [
                    random.randint(1, self.width - 2),
                    random.randint(1, self.height - 2),
                ]
            )

        # Спавним дедлайны и преподов курсов (!)
        for _ in range(3):
            self.enemies.append(
                [
                    random.randint(1, self.width - 2),
                    random.randint(1, self.height - 2),
                ]
            )

    def draw(self):
        clear_screen()
        print(
            f"{C_PINK}{C_BOLD}=== MY LITTLE PIGGY: SELF DESTRUCT IS MAGIC! ==={C_RESET}"
        )
        print(
            f"{C_CYAN}Железо: Celeron G1620 | Проект: 'Кодоев Храм' | Версия: 1.0 Alpha{C_RESET}\n"
        )

        # Рендерим карту
        print(f"{C_WHITE}+" + "-" * self.width + f"+{C_RESET}")
        for y in range(self.height):
            line = f"{C_WHITE}|{C_RESET}"
            for x in range(self.width):
                if x == self.px and y == self.py:
                    line += f"{C_PINK}{C_BOLD}@(oo){C_RESET}"[
                        :1
                    ]  # Свинка-терминатор
                elif [x, y] in self.tnt:
                    line += f"{C_YELLOW}*{C_RESET}"  # Тротил
                elif [x, y] in self.debts:
                    line += f"{C_GREEN}${C_RESET}"  # Долг Янчика
                elif [x, y] in self.enemies:
                    line += f"{C_RED}!{C_RESET}"  # Дедлайн
                else:
                    line += " "
            line += f"{C_WHITE}|{C_RESET}"
            print(line)
        print(f"{C_WHITE}+" + "-" * self.width + f"+{C_RESET}")

        # Полоска ульты магии
        bar_len = 20
        filled = int((self.magic / self.max_magic) * bar_len)
        bar = (
            f"{C_RED}█{C_RESET}" * filled + f"{C_WHITE}░{C_RESET}" * (bar_len - filled)
        )

        print(
            f"\n{C_BOLD}Шкала Магии Дружбы:{C_RESET} [{bar}] {C_YELLOW}{self.magic}%{C_RESET}"
        )
        print(
            f"Очки: {C_CYAN}{self.score}{C_RESET} | Отжато у Янчика: {C_GREEN}{self.debt_collected} сум{C_RESET}"
        )
        print(
            f"\n{C_BOLD}Управление:{C_RESET} [W,A,S,D] — Бегать | [X] — {C_RED}{C_BOLD}САМОУНИЧТОЖЕНИЕ{C_RESET} | [Q] — Свалить"
        )

    def move(self, dx, dy):
        nx, ny = self.px + dx, self.py + dy
        if 0 <= nx < self.width and 0 <= ny < self.height:
            self.px, self.py = nx, ny

        # Подбираем тротил
        for t in self.tnt[:]:
            if t == [self.px, self.py]:
                self.tnt.remove(t)
                self.magic = min(self.max_magic, self.magic + 25)
                self.score += 50
                # Спавним новый тротил где-то на карте
                self.tnt.append(
                    [
                        random.randint(0, self.width - 1),
                        random.randint(0, self.height - 1),
                    ]
                )

        # Отжимаем долг
        for d in self.debts[:]:
            if d == [self.px, self.py]:
                self.debts.remove(d)
                self.debt_collected += 5000
                self.score += 100
                self.magic = min(self.max_magic, self.magic + 10)
                self.debts.append(
                    [
                        random.randint(0, self.width - 1),
                        random.randint(0, self.height - 1),
                    ]
                )

        # Двигаем врагов (тупой рандомный ИИ)
        for e in self.enemies:
            e[0] = max(0, min(self.width - 1, e[0] + random.choice([-1, 0, 1])))
            e[1] = max(
                0, min(self.height - 1, e[1] + random.choice([-1, 0, 1]))
            )
            if e == [self.px, self.py]:
                self.magic = max(0, self.magic - 15)
                print(f"\a")  # Звуковой писк

    def self_destruct(self):
        if self.magic >= 100:
            explosion_animation()
            print(
                f"\n{C_GREEN}{C_BOLD}>>> ПОБЕДА! МАГИЯ ДРУЖБЫ ИСПАРИЛА ЗАЖОПИНСК! <<<{C_RESET}"
            )
            print(
                f"Итоговый счёт: {self.score + 500} | Долг Янчика возвращён взрывной волной!"
            )
            print(
                f"{C_PINK}Свинка отправилась в рай для шашлыка. Кодоев Храм защищён.{C_RESET}\n"
            )
            self.game_over = True
        else:
            print(
                f"\n{C_RED}Магия не готова! Нужно 100% тротила! Жри больше звёздочек (*)!{C_RESET}"
            )
            time.sleep(1)


def main():
    game = PiggyGame()

    while not game.game_over:
        game.draw()
        cmd = get_key()

        if cmd == "w":
            game.move(0, -1)
        elif cmd == "s":
            game.move(0, 1)
        elif cmd == "a":
            game.move(-1, 0)
        elif cmd == "d":
            game.move(1, 0)
        elif cmd == "x":
            game.self_destruct()
        elif cmd == "q":
            print(
                f"\n{C_YELLOW}Ты с позором ливнул в меню Windows 10... Янчик ликует.{C_RESET}"
            )
            break


if __name__ == "__main__":
    main()