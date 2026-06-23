import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TALB, TPE1, TPE2, TPOS, TRCK

def main():
    print("==================================================")
    print("   КОНВЕЙЕР АВТОМАТИЗАЦИИ ПРОЕКТА 'КОДОЕВ ХРАМ'   ")
    print("==================================================")
    
    # Скрипт вежливо спросит, где лежит папка с дисками
    album_path = input("Закинь сюда полный путь к папке альбома (где disc1 и disc2): ").strip().strip('"')
    
    # Карта соответствия папок и номеров дисков
    discs = {
        "disc1": "1",
        "disc2": "2"
    }
    
    for folder_name, disc_num in discs.items():
        full_path = os.path.join(album_path, folder_name)
        
        if not os.path.exists(full_path):
            print(f"\n⚠️ Папка {folder_name} не найдена по пути: {full_path}. Пропускаем...")
            continue
            
        print(f"\n Начинаем зачистку папки: {folder_name} (Диск {disc_num})")
        
        for filename in os.listdir(full_path):
            if filename.lower().endswith('.mp3'):
                file_path = os.path.join(full_path, filename)
                
                # Наглый костыль: выдираем первые две цифры из имени файла типа "01. Mr. Self Destruct.mp3"
                track_num = "".join([c for c in filename[:2] if c.isdigit()])
                if not track_num:
                    track_num = "1"  # Если файл назван через задницу, ставим заглушку
                
                try:
                    # Проверяем, есть ли уже ID3 теги, если нет — создаем с нуля
                    try:
                        audio = MP3(file_path, ID3=ID3)
                    except Exception:
                        audio = MP3(file_path)
                        audio.add_tags()
                    
                    # Силой кода заталкиваем православные теги в файл
                    # TALB — Альбом, TPE1 — Исполнитель, TPE2 — Альбом-Артист, TPOS — Номер диска, TRCK — Номер трека
                    audio.tags.add(TALB(encoding=3, text="The Downward Spiral (Deluxe Edition)"))
                    audio.tags.add(TPE1(encoding=3, text="Nine Inch Nails"))
                    audio.tags.add(TPE2(encoding=3, text="Nine Inch Nails"))
                    audio.tags.add(TPOS(encoding=3, text=disc_num))
                    audio.tags.add(TRCK(encoding=3, text=track_num))
                    
                    audio.save()
                    print(f"   [OK] {filename} -> Диск {disc_num}, Трек {track_num}")
                except Exception as e:
                    print(f"   [ERROR] Скрипт споткнулся о файл {filename}: {e}")
                    
    print("\n==================================================")
    print(" СПЕЦОПЕРАЦИЯ ЗАВЕРШЕНА. ПЧЕЛА ДОЛЖНА ПОВИНОВАТЬСЯ! ")
    print("==================================================")

if __name__ == "__main__":
    main()