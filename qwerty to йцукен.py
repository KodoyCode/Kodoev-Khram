def flip_layout(text):
    layout_map = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
    }
    # Добавляем обратные значения в один присест, чтобы не плодить мусор
    layout_map.update({v: k for k, v in layout_map.items()})
    
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in layout_map:
            flipped = layout_map[lower_char]
            result.append(flipped.upper() if char.isupper() else flipped)
        else:
            result.append(char)
    return "".join(result)

while True:
    text = input("\nВводи текст (или 'exit' для выхода): ")
    if text.lower() == "exit":
        print("Ну и иди нахуй.")
        break
    print("Исправил (нет):", flip_layout(text))