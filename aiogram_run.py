import asyncio
from create_bot import bot, dp, admins
from handlers.user_router import user_router
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands():
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    await set_commands()
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, f'Поехали🥳.')
    except:
        pass


async def stop_bot():
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Пора баю😔')
    except:
        pass


async def main():
    dp.include_router(user_router)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
