from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_kb():
    kb_list = [[KeyboardButton(text="▶️ Начать *разговор*")]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Чтоб начать диалог с ботом жмите 👇:"
    )


def stop_speak():
    kb_list = [[KeyboardButton(text="❌ Прекратить разговорчики")]]
    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Чтоб завершить диалог с ботом жмите 👇:"
    )