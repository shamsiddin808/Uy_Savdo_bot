from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Statistika 📊 "),
        ],
        [
            KeyboardButton(text="Yer maydon narxlarni qo'shish 🏘 "),
            KeyboardButton(text="Xona uchun narx qoshish"),
        ],
        [
            KeyboardButton(text="Qavat uchun narx qoshish"),
        ],
    ],
    resize_keyboard=True
)