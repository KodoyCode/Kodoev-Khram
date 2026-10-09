# Универсальная функция перевода из 10-ричной в любую систему от 2 до 36
def dec_to_base(num: int, base: int) -> str:
    if num == 0:
        return "0"
    
    # Алфавит из 36 символов (0-9 + A-Z)
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
        
    return result

# Список систем, которые зашьём в шпаргалку для печати
# (2, 3, 4, 8, 10, 12, 16, 18, 36 — самые частые на олимпиадах и в айти)
selected_bases = [2, 3, 8, 10, 12, 16, 18, 36]

filename = "all_bases_table.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("=" * 80 + "\n")
    f.write("       УНИВЕРСАЛЬНАЯ ШПАРАЛКА ПО СИСТЕМАМ СЧИСЛЕНИЯ (BASE 2 - 36)\n")
    f.write("=" * 80 + "\n\n")
    
    # Шапка таблицы
    header = f"{'DEC (10)':<8} | " + " | ".join([f"BASE-{b:<2}" for b in selected_bases if b != 10])
    f.write(header + "\n")
    f.write("-" * len(header) + "\n")
    
    # Генерим числа от 0 до 35 (чтобы захватить весь алфавит до буквы Z)
    for i in range(36):
        row = f"{i:<8} | "
        cols = []
        for b in selected_bases:
            if b == 10:
                continue
            val = dec_to_base(i, b)
            cols.append(f"{val:<7}")
        row += " | ".join(cols)
        f.write(row + "\n")
        
        # Визуальный разделитель каждые 8 чисел для удобства глаз
        if (i + 1) % 8 == 0:
            f.write("-" * len(header) + "\n")

print(f"Готово! Скрипт сгенерил шпаргалку в файл '{filename}'. Забирай и печатай!")