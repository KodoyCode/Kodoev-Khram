
# 
# 
import os
from flask import Flask, render_template, request, redirect, url_for
from google import genai
from PIL import Image

app = Flask(__name__)

# Создаем папку для хранения загруженных картинок, если её ещё нет
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Инициализируем клиента. Ключ подтянется автоматом из переменной окружения, 
# либо вставь его внутрь genai.Client(api_key="твой_ключ")
client = genai.Client(api_key="")

# Создаем ОДНУ сквозную сессию чата с поддержкой памяти
chat_session = client.chats.create(model="gemini-2.5-flash")

# Наш кастомный список для фронтенда, чтобы красиво рендерить и текст, и пути к фоткам
display_history = []

@app.route('/')
def index():
    return render_template('index.html', history=display_history)

@app.route('/send_message', methods=['POST'])
def send_message():
    user_text = request.form.get('user_input')
    image_file = request.files.get('image')
    
    contents = []
    saved_img_url = None

    # Если юзер закинул файл
    if image_file and image_file.filename != '':
        # Формируем путь и сохраняем картинку на жесткий диск
        img_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(img_path)
        
        # Открываем картинку через Pillow для скармливания нейронке
        pil_img = Image.open(img_path)
        contents.append(pil_img)
        
        # Формируем URL для отображения в теге <img> на фронтенде
        saved_img_url = f'/static/uploads/{image_file.filename}'

    # Если есть текст — добавляем его в пачку к Gemini
    if user_text:
        contents.append(user_text)

    # Если ни текста, ни картинки не прислали — просто редиректим обратно
    if not contents:
        return redirect(url_for('index'))

    try:
        # Отправляем всю пачку (картинка + текст) в текущую сессию чата
        response = chat_session.send_message(contents)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Ошибка API: {str(e)}"

    # Закидываем в историю для отображения на странице
    display_history.append({
        'role': 'user',
        'text': user_text,
        'image': saved_img_url
    })
    
    display_history.append({
        'role': 'bot',
        'text': bot_reply,
        'image': None
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)