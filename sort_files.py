import os
import shutil

# Укажи путь к папке, где вечный срач (например, твои Загрузки)
# В Windows пути пишутся либо через /, либо с буквой r перед кавычками
source_dir = r'C:\Users\user\Desktop\SaiytovAydos-Files'

# Словарь: ключ - имя папки, значение - список расширений
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.jfif'],
    'HTML': ['.html'],
    'CSS': ['.css'],
    'PYTHON': ['.py'],
    'JAVA': ['.js', '.json'],
    'XML': ['.xml'],
    'Video': ['.mp4', '.mkv', '.mov'],
    'Audio': ['.mp3', '.flac', '.wav'],
}

def sort_files():
    # Проверяем, существует ли вообще такая папка
    if not os.path.exists(source_dir):
        print("Чел, путь кривой. Проверь папку! 🤡")
        return

    # Проходимся по всем файлам в папке
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Пропускаем, если это папка, а не файл
        if os.path.isdir(file_path):
            continue

        # Узнаем расширение файла
        extension = os.path.splitext(filename)[1].lower()

        # Ищем, в какую папку отправить этот файл
        moved = False
        for folder_name, extensions in folders.items():
            if extension in extensions:
                target_folder = os.path.join(source_dir, folder_name)
                
                # Если папки еще нет — создаем её
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Перемещаем файл
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"По факту: {filename} улетел в {folder_name}")
                moved = True
                break
        
        if not moved:
            print(f"Хз куда деть {filename}, оставил как есть.")

if __name__ == "__main__":
    print("Запускаю генеральную уборку... 😭")
    sort_files()
    print("Готово! Теперь в папке хотя бы можно что-то найти.")