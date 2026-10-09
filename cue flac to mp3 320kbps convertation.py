# -*- coding: utf-8 -*-
"""
Автоматический конвертер CUE + FLAC/WAV/APE -> MP3 (320 kbps)
Версия: Pro / Kodoy Hram Edition
"""

import os
import sys
import re
import shutil
import subprocess
from pathlib import Path

def check_ffmpeg():
    """Проверяет наличие ffmpeg в системе."""
    if not shutil.which('ffmpeg'):
        print("❌ ОШИБКА: FFmpeg не найден в PATH!")
        print("Скачай ffmpeg.exe и закинь его в папку со скриптом или добавь в переменные среды Windows.")
        sys.exit(1)

def sanitize_filename(name):
    """Убирает запрещенные символы Windows, зарезервированные имена и точки на конце."""
    # Символы, запрещенные в Windows: \ / * ? : " < > |
    clean = re.sub(r'[\\/*?:"<>|]', "", name)
    # Убираем множественные пробелы и точки/пробелы на концах
    clean = re.sub(r'\s+', ' ', clean).strip(" .")
    
    # Проверка зарезервированных имен Windows
    reserved = {"CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", 
                "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3"}
    if clean.upper() in reserved:
        clean += "_"
        
    return clean or "Track"

def parse_time(time_str):
    """Конвертирует MM:SS:FF в секунды (75 фреймов в секунде для CUE)."""
    parts = time_str.split(':')
    if len(parts) == 3:
        try:
            minutes = int(parts[0])
            seconds = int(parts[1])
            frames = int(parts[2])
            return minutes * 60 + seconds + frames / 75.0
        except ValueError:
            return 0.0
    return 0.0

def read_cue_file(cue_path):
    """Читает CUE файл. utf-8-sig идет ПЕРВЫМ, чтобы срезать BOM-мусор!"""
    encodings = ['utf-8-sig', 'cp1251', 'utf-8', 'cp1252', 'latin1']
    for enc in encodings:
        try:
            with open(cue_path, 'r', encoding=enc) as f:
                return f.readlines()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Не удалось прочитать CUE: {cue_path}")

def clean_cue_value(value_str):
    """Очищает значение тега от внешних кавычек и лишних пробелов."""
    val = value_str.strip()
    if val.startswith('"') and val.endswith('"'):
        val = val[1:-1]
    return val.strip()

def parse_cue(cue_path):
    """Разбирает CUE файл на метаданные и список треков."""
    lines = read_cue_file(cue_path)
    
    album_artist = ""
    album_title = ""
    year = ""
    audio_file = ""
    tracks = []
    current_track = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Метаданные альбома (до первого TRACK)
        if current_track is None:
            if re.match(r'^PERFORMER', line, re.IGNORECASE):
                album_artist = clean_cue_value(line[9:])
            elif re.match(r'^TITLE', line, re.IGNORECASE):
                album_title = clean_cue_value(line[5:])
            elif re.match(r'^REM\s+(DATE|YEAR)', line, re.IGNORECASE):
                parts = line.split(maxsplit=2)
                if len(parts) >= 3:
                    year = clean_cue_value(parts[2])
            elif re.match(r'^FILE', line, re.IGNORECASE):
                m = re.search(r'FILE\s+"?(.*?)"?\s+\w+$', line, re.IGNORECASE)
                if m: 
                    audio_file = m.group(1)
                
        # Парсинг отдельных треков
        if re.match(r'^TRACK', line, re.IGNORECASE):
            m = re.search(r'TRACK\s+(\d+)\s+AUDIO', line, re.IGNORECASE)
            if m:
                track_num = int(m.group(1))
                current_track = {
                    'number': track_num,
                    'title': f"Track {track_num:02d}",
                    'artist': album_artist,
                    'start': 0.0
                }
                tracks.append(current_track)
        elif current_track is not None:
            if re.match(r'^TITLE', line, re.IGNORECASE):
                current_track['title'] = clean_cue_value(line[5:])
            elif re.match(r'^PERFORMER', line, re.IGNORECASE):
                current_track['artist'] = clean_cue_value(line[9:])
            elif re.search(r'INDEX\s+01', line, re.IGNORECASE):
                m = re.search(r'INDEX\s+01\s+(\d+:\d+:\d+)', line, re.IGNORECASE)
                if m: 
                    current_track['start'] = parse_time(m.group(1))
                    
    return {
        'album_artist': album_artist or "Unknown Artist",
        'album_title': album_title or "Unknown Album",
        'year': year,
        'audio_file': audio_file,
        'tracks': tracks
    }

def find_audio_file(cue_dir, referenced_file):
    """Ищет FLAC/WAV/APE/WV файл по наводке из CUE или просто в папке."""
    if referenced_file:
        ref_path = cue_dir / referenced_file
        if ref_path.exists():
            return ref_path
        
        # Проверяем тот же файл, но с другими популярными расширениями
        stem = Path(referenced_file).stem
        for ext in ['.flac', '.wav', '.ape', '.wv', '.m4a']:
            candidate = cue_dir / (stem + ext)
            if candidate.exists():
                return candidate
                
    # Если в CUE написана дичь или файл переименовали — ищем самый большой аудиофайл
    audio_extensions = ['*.flac', '*.wav', '*.ape', '*.wv']
    audio_files = []
    for ext in audio_extensions:
        audio_files.extend(cue_dir.glob(ext))
        
    if len(audio_files) == 1:
        return audio_files[0]
    elif len(audio_files) > 1:
        # Берём самый весомый файл (скорее всего это полный альбом)
        return max(audio_files, key=lambda f: f.stat().st_size)
        
    return None

def find_cover_image(cue_dir):
    """Ищет обложку альбома в папке."""
    cover_names = ['folder.jpg', 'cover.jpg', 'front.jpg', 'folder.png', 'cover.png', 'front.png']
    for name in cover_names:
        img_path = cue_dir / name
        if img_path.exists():
            return img_path
            
    images = list(cue_dir.glob('*.jpg')) + list(cue_dir.glob('*.png')) + list(cue_dir.glob('*.jpeg'))
    return images[0] if images else None

def process_cue(cue_path):
    print(f"\n📂 Разбор CUE: {cue_path.name}")
    cue_dir = cue_path.parent
    
    try:
        data = parse_cue(cue_path)
    except Exception as e:
        print(f"  ❌ Ошибка чтения CUE файла: {e}")
        return

    tracks = data['tracks']
    if not tracks:
        print("  ⚠️ Нет треков в CUE.")
        return
        
    audio_path = find_audio_file(cue_dir, data['audio_file'])
    if not audio_path:
        print(f"  ❌ Не найден аудиофайл-исходник для {cue_path.name}")
        return

    cover_path = find_cover_image(cue_dir)
    if cover_path:
        print(f"  🖼️ Найдена обложка: {cover_path.name}")
        
    print(f"  🎵 Альбом: {data['album_artist']} — {data['album_title']} [{data['year'] or 'N/A'}] ({len(tracks)} тр.)")
    
    total_tracks = len(tracks)
    for i, track in enumerate(tracks):
        start_sec = track['start']
        duration_sec = (tracks[i+1]['start'] - start_sec) if (i < total_tracks - 1) else None
            
        clean_title = sanitize_filename(track['title'])
        track_artist = track['artist'] or data['album_artist']
        out_filename = f"{track['number']:02d} - {clean_title}.mp3"
        out_path = cue_dir / out_filename
        
        if out_path.exists():
            print(f"  ⏩ Пропуск (уже нарезан): {out_filename}")
            continue
            
        print(f"  ⏳ Нарезка [{i+1}/{total_tracks}]: {out_filename}")
        
        # Базовая команда FFmpeg (без лишнего спама в консоль)
        cmd = ['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error']
        
        # Быстрое позиционирование ДО `-i`
        cmd.extend(['-ss', f"{start_sec:.3f}", '-i', str(audio_path)])
        
        # Если есть обложка — цепляем её вторым входом
        if cover_path:
            cmd.extend(['-i', str(cover_path)])
            
        if duration_sec is not None:
            cmd.extend(['-t', f"{duration_sec:.3f}"])
            
        # Выбираем аудиопоток
        cmd.extend(['-map', '0:a'])
        
        # Если есть обложка — мапим её как видеопоток в MP3 (Album Art)
        if cover_path:
            cmd.extend(['-map', '1:v', '-c:v', 'copy', '-metadata:s:v', 'title="Album cover"', '-metadata:s:v', 'comment="Cover (front)"'])
            
        # Параметры кодирования LAME MP3 + теги ID3v2.3 (чтобы корректно читалось везде)
        cmd.extend([
            '-c:a', 'libmp3lame', '-b:a', '320k',
            '-id3v2_version', '3',
            '-metadata', f"title={track['title']}",
            '-metadata', f"artist={track_artist}",
            '-metadata', f"album={data['album_title']}",
            '-metadata', f"album_artist={data['album_artist']}",
            '-metadata', f"track={track['number']}/{total_tracks}"
        ])
        
        if data['year']:
            cmd.extend(['-metadata', f"date={data['year']}"])
            
        cmd.append(str(out_path))
        
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            print(f"  ❌ Ошибка FFmpeg на треке {out_filename}: {res.stderr.strip()}")
        else:
            print(f"  ✅ Записан: {out_filename}")

def main():
    # Сначала проверяем бинарь FFmpeg
    check_ffmpeg()
    
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1].strip('"\''))
    else:
        target_dir_str = input("Введи путь к папке с музыкой: ").strip('"\'')
        target_dir = Path(target_dir_str)
        
    if not target_dir.exists():
        print(f"❌ Путь не существует: {target_dir}")
        return

    print(f"🔍 Сканируем {target_dir} на наличие .cue файлов...")
    cue_files = list(target_dir.rglob('*.cue'))
    
    if not cue_files:
        print("❌ .cue файлы не найдены.")
        return

    print(f"🎯 Найдено CUE альбомов: {len(cue_files)}")
    for cue in cue_files:
        process_cue(cue)
        
    print("\n🎉 Готово, шеф! Вся музыка порезана в 320 kbps и снабжена тегами.")

if __name__ == '__main__':
    main()