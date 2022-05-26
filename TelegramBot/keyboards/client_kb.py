from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Keyboards:

    @property
    def menu_num(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('1')
        btn2 = KeyboardButton('2')
        btn3 = KeyboardButton('3')
        btn4 = KeyboardButton('4')
        btn5 = KeyboardButton('5')
        btn6 = KeyboardButton('🔙 Вернуться')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        return markup

    @property
    def start_menu(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('👱🏽 Выбрать героя')
        btn2 = KeyboardButton('💪 Метовые герои')
        markup.add(btn1, btn2)
        return markup

    @property
    def menu_meta(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('🗡️ Carry')
        btn2 = KeyboardButton('🏹 Mid lane')
        btn3 = KeyboardButton('🛡️ Off lane')
        btn4 = KeyboardButton('🤝 Soft support (Pos 4)')
        btn5 = KeyboardButton('🆘 Hard support (Pos 5)')
        btn6 = KeyboardButton('🔙 Back')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        return markup

    @property
    def hero_menu(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('🏹 Предметы')
        btn2 = KeyboardButton('😊 Кого контрит')
        btn3 = KeyboardButton('😰 Контрпики')
        btn4 = KeyboardButton('🏟 Последние игры')
        btn5 = KeyboardButton('🔄 Выбрать другого героя')
        btn6 = KeyboardButton('🔙 Back')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        return markup


    @property
    def menu_items(self):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('🛒 Предметы для покупки')
        btn2 = KeyboardButton('🏁 Стартовый закуп')
        btn3 = KeyboardButton('⚔ Доп. предметы')
        btn4 = KeyboardButton('🔙 Назад')
        markup.add(btn1, btn2, btn3, btn4)
        return markup
