import os
import subprocess

# --- НАСТРОЙКИ ---
WORKSHOP_DIR = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\4000"
GMAD_PATH = r"C:\Program Files (x86)\Steam\steamapps\common\GarrysMod\bin\gmad.exe"
OUTPUT_DIR = r"C:\GMod_Unpacked_Addons"

# Минимальный вес в МБ (все еще фильтруем жир)
MIN_SIZE_MB = 100  
# ------------------

def unpack_gma_fixed():
    inp = bool(input("Вы хотите продолжить? (напишите y или 1 или да): "))
    if inp == "y" or "1" or "да":
        if not os.path.exists(GMAD_PATH):
            print(f"[!] Ошибка: gmad.exe не найден! Проверь путь: {GMAD_PATH}")
            return

        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

        min_size_bytes = MIN_SIZE_MB * 1024 * 1024
        print(f"[*] Запуск исправления. Ищем аддоны от {MIN_SIZE_MB} МБ...")
        
        unpacked_count = 0
        skipped_count = 0

        for root, dirs, files in os.walk(WORKSHOP_DIR):
            for file in files:
                if file.endswith('.gma'):
                    gma_file_path = os.path.join(root, file)
                    
                    # Фильтр по размеру
                    file_size_bytes = os.path.getsize(gma_file_path)
                    if file_size_bytes < min_size_bytes:
                        skipped_count += 1
                        continue
                    
                    file_size_mb = file_size_bytes / (1024 * 1024)
                    
                    # --- ВОТ ТУТ МАГИЯ ИСПРАВЛЕНИЯ ---
                    # os.path.basename(root) достает имя папки, то есть ID воркшопа (например, "213456789")
                    workshop_id = os.path.basename(root)
                    pure_filename = os.path.splitext(file)[0]
                    
                    # Соединяем ID воркшопа и имя файла. Получится типа "213456789_gmpublisher"
                    addon_unique_name = f"{workshop_id}_{pure_filename}"
                    addon_output_path = os.path.join(OUTPUT_DIR, addon_unique_name)
                    # ----------------------------------

                    print(f"\n[+] Нашел аддон: {file} (ID: {workshop_id}) ~{file_size_mb:.2f} МБ")
                    print(f"    Распаковка в уникальную папку: {addon_output_path}")

                    command = [
                        GMAD_PATH,
                        "extract",
                        "-file", gma_file_path,
                        "-out", addon_output_path
                    ]

                    try:
                        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        if result.returncode == 0:
                            print("    [Успешно распаковано]")
                            unpacked_count += 1
                        else:
                            print(f"    [Ошибка gmad]: {result.stderr.strip()}")
                    except Exception as e:
                        print(f"    [Ошибка скрипта]: {e}")

        print("\n" + "="*40)
        print("[+] Фикс отработал!")
        print(f"[+] Успешно распотрошено: {unpacked_count}")
        print(f"[+] Пропущено мелкотни: {skipped_count}")
        print("="*40)
    else:
        print("Cancel")

if __name__ == "__main__":
    unpack_gma_fixed()