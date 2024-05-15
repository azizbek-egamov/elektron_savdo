from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💥 Maxsulotlar", callback_data="shop")
        ],
        [
            InlineKeyboardButton(text="🛒 Savat", callback_data="basket"),
            InlineKeyboardButton(text="🛍 Buyurmalarim", callback_data="orders")
        ]
    ]
)

panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Maxsulotlar sozlamalari", callback_data="settings"), 
            InlineKeyboardButton(text="Orqaga", callback_data="back")
        ]
    ]
)

setting = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kategoriyalar", callback_data="ad_categories"),
            InlineKeyboardButton(text="Maxsulotlar", callback_data="ad_maxsulotlar")
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="panel")
        ]
    ]
)

klar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kategoriya qo'shish", callback_data="add_category"),
            InlineKeyboardButton(text="Katagoriya o'chirish", callback_data="del_category")
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="settings")
        ]
    ]
)

mlar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Maxsulot qo'shish", callback_data="add_maxsulot"),
            InlineKeyboardButton(text="Maxsulot o'chirish", callback_data="del_maxsulot")
        ],
        [
            InlineKeyboardButton(text="Orqaga", callback_data="settings")
        ]
    ]
)