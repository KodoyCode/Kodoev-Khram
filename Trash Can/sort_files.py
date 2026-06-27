import os
import shutil

# Путь к твоей обители хаоса
source_dir = r'C:/Users/Kodoy/Downloads'

folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.jfif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Code': ['.html', '.css', '.py', '.xml', '.js', '.json'],
    'Soft': ['.exe', '.msi', '.iso'],
    'Archives': ['.zip', '.rar', '.7z', '.gz', '.bz2'],
    'Video': ['.mp4', '.mkv', '.mov'],
    'Audio': ['.mp3', '.flac', '.wav'],
}

def get_unique_path(target_folder, filename):
    """Функция, которая не даст скрипту упасть, если файл уже существует"""
    base, extension = os.path.splitext(filename)
    counter = 1
    target_path = os.path.join(target_folder, filename)
    
    # Если файл с таким именем уже сидит в целевой папке, добавляем циферку
    while os.path.exists(target_path):
        filename = f"{base}_{counter}{extension}"
        target_path = os.path.join(target_folder, filename)
        counter += 1
        
    return target_path

def sort_files():
    if not os.path.exists(source_dir):
        print("Чел, путь кривой. Проверь папку! 🤡")
        return

    print("🧹 Начинаю жёсткую зачистку...")
    files_moved = 0

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        moved = False

        # Ищем категорию
        for folder_name, extensions in folders.items():
            if extension in extensions:
                target_folder = os.path.join(source_dir, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Получаем безопасный путь с учётом возможных дубликатов
                final_target_path = get_unique_path(target_folder, filename)
                shutil.move(file_path, final_target_path)
                print(f"📦 {filename} -> {folder_name}")
                moved = True
                files_moved += 1
                break
        
        # Если это какой-то неведомый хлам, кидаем в 'Other'
        if not moved:
            other_folder = os.path.join(source_dir, 'Other')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
                
            final_target_path = get_unique_path(other_folder, filename)
            shutil.move(file_path, final_target_path)
            print(f"🗑️ Неопознанный объект {filename} отправлен в Other")
            files_moved += 1

    print(f"🏁 Готово! Раскидано файлов: {files_moved}. Теперь чисто, как в аптеке.")

if __name__ == "__main__":
    sort_files()