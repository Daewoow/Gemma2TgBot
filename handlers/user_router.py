from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from create_bot import bot, local_client
# from db_handler.db_funk import (get_user_data, insert_user, clear_dialog,
#                                 add_message_to_dialog_history, get_dialog_status)
from keyboards.kbs import start_kb, stop_speak
from aiogram.utils.chat_action import ChatActionSender

user_router = Router()


@user_router.message(Command(commands=['start', 'restart']))
async def cmd_start(message: Message):
    await message.answer(text='Привет! Давай начнем общаться. Для этого просто нажми на кнопку "Начать диалог"',
                            reply_markup=start_kb())


@user_router.message(F.text.lower().contains('начать диалог'))
async def start_speak(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        await message.answer(text='Диалог начат. Введите ваше сообщение:', reply_markup=stop_speak())


@user_router.message(F.text.lower().contains('завершить диалог'))
async def start_speak(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        await message.answer(text='Диалог очищен! Начнем общаться?', reply_markup=start_kb())


@user_router.message(F.text)
async def handle_message(message: Message):
    async with ChatActionSender.typing(bot=bot, chat_id=message.from_user.id):
        user_msg_dict = {"role": "user", "content": message.text}

        dialog_history = [{
            "role": "user",
            "content": message.text,
        }]

        # сохраняем сообщение в базу данных и получаем историю диалога
        # dialog_history = await add_message_to_dialog_history(user_id=message.from_user.id,
        #                                                      message=user_msg_dict,
        #                                                      return_history=True)

        chat_completion = local_client.chat.completions.create(model="gemma2", messages=dialog_history)
        message_llama = await message.answer(text=chat_completion.choices[0].message.content, reply_markup=stop_speak())
        dialog_history.append({
            "role": "assistant",
            "content": chat_completion.choices[0].message.content,
        })
