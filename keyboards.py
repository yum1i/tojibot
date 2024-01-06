from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData 
from aiogram.utils.keyboard import InlineKeyboardBuilder


kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📚 Учиться"),
                KeyboardButton(text="🚀 Проекты"),
            ],
            [
                KeyboardButton(text="Discord и TikTok 💻")
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите действие из меню"
    )



kb_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python для начинающих", url="tg://resolve?domain=python_interesting")],
        [InlineKeyboardButton(text="Python: задачки и вопросы", url="tg://resolve?domain=quize_python")],
        [InlineKeyboardButton(text="Data Science. SQL", url="tg://resolve?domain=sqlhub")],
        [InlineKeyboardButton(text="Библиотека программиста", url="tg://resolve?domain=devs_storage")],
        [InlineKeyboardButton(text="GitHub программиста", url="tg://resolve?domain=githubdevs")],
        
        
    ]
)


link = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Discord 🌐", url="https://discord.com/invite/DB9nMyGM")],
        [InlineKeyboardButton(text="Tik Tok 🕺", url="https://www.tiktok.com/@zmbkv.xs?_t=8imd6MA4Xa5&_r=1")]
    ]
)