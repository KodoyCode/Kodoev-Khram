class MyLittlePenys:
    def __init__(self, color: str = "розовый в яблоках", is_magic: bool = True):
        # Реально используем то, что передали, а не забиваем болт!
        self.color = color
        self.is_magic = is_magic
        self.can_gallop = True
        self.is_hungry = True

    def feed(self, hay_count: int) -> str:
        """Метод кормления чудовища сеном"""
        if hay_count <= 0:
            self.is_hungry = True
            return "Пенис голоден, зол, сморщился и отказывается скакать!"
        
        self.is_hungry = False
        magic_status = "магически " if self.is_magic else ""
        return f"Пенис цвета «{self.color}» сожрал {hay_count} мешков сена, сыт и {magic_status}радостно ржёт на весь Зажопинск!"

    def kick_yanchik(self):
        """Спец-способность для выбивания бабок"""
        return "Пенис с разворота прописывает Янчику копытом в челюсть. Долг всё ещё не возвращён, но на душе потеплело."