import asyncio
import aioschedule
import config
from loader import bot, AuthMiddleware
import requests

FLUG = True

async def on_shutdown(dp):
    await bot.close()

async def on_startup(_):
    asyncio.create_task(scheduler())

    r = requests.get('http://95.105.52.77:3287/epicsound.mp3')

    with open('подсказка.mp3', 'wb') as f: 
        f.write(r.content)

async def check():
    global FLUG
    if requests.get('http://95.105.52.77:3287/').status_code == 200 and FLUG:
        await bot.send_audio(config.FOR_WHERE, audio=open('подсказка.mp3', 'rb'))
        FLUG = False

async def scheduler():
    aioschedule.every(5).seconds.do(check)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
    
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    dp.middleware.setup(AuthMiddleware())
    executor.start_polling(dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True)