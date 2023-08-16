import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp, bot
import time
import keybords.inline.choice_buttons as key
import keybords.inline.callback_datas as call_datas
#from bd.sql import *
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка старт
@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    text = '''Ооо, поздравляю, ты справился!!!:)'''
    mes_id = await bot.send_message(chat_id=message.chat.id, text='O')
    await one_symbal(text, mes_id['chat']['id'], mes_id['message_id'])
    mes_id = await bot.send_message(chat_id=message.chat.id, text='На самом деле, это была ложь, и я не буду помогать тебе, но я приведу тебя к следующему заданию.')
    time.sleep(5)
    await bot.edit_message_text("Сейчас ты получишь зашифрованную подсказку. Помни, что все, о чем говориться дальше, косвенно связано с числом 22.", mes_id['chat']['id'], mes_id['message_id'], reply_markup=key.menu_keyboard)
    
# Первый пункт    
@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Тебе предстоит найти путь к замку с сокровищем. Мудрец, живущий в нем, показал мне дорогу и подсказал, что нужно сказать охраннику на входе, чтобы войти. Я постараюсь передать тебе слова мудреца, но если у меня не выйдет, то прошу, обратись к моим создателям.', reply_markup=key.one_keyboard)
    await call.answer()

# Первый пункт назад
@dp.callback_query_handler(call_datas.one_p_callback.filter(item_one='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Сейчас ты получишь зашифрованную подсказку. Помни, что все, о чем говориться дальше, косвенно связано с числом 22.', reply_markup=key.menu_keyboard)
    await call.answer()

# Второй пункт 
@dp.callback_query_handler(call_datas.one_p_callback.filter(item_one='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Правда, забыл сказать, что есть одна загвоздка - я не знаю, какая из дверей верная. Чтобы это понять тебе понадобится n-карта. Если она еще не у тебя, то найди ее!!!', reply_markup=key.two_keyboard)
    await call.answer()

# Второй пункт назад
@dp.callback_query_handler(call_datas.two_p_callback.filter(item_two='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Тебе предстоит найти путь к замку с сокровищем. Мудрец, живущий в нем, показал мне дорогу и подсказал, что нужно сказать охраннику на входе, чтобы войти. Я постараюсь передать тебе слова мудреца, но если у меня не выйдет, то прошу, обратись к моим создателям.', reply_markup=key.one_keyboard)
    await call.answer()

# Третий пункт
@dp.callback_query_handler(call_datas.two_p_callback.filter(item_two='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('А теперь соберись. Будет необходим весь твой накопленный опыт и все знания, полученные ранее.', reply_markup=key.three_keyboard)
    await call.answer()

# Третий пункт назад
@dp.callback_query_handler(call_datas.three_p_callback.filter(item_three='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Правда, забыл сказать, что есть одна загвоздка - я не знаю, какая из дверей верная. Чтобы это понять тебе понадобится n-карта. Если она еще не у тебя, то найди ее!!!', reply_markup=key.two_keyboard)
    await call.answer()

# Четвертый пункт
@dp.callback_query_handler(call_datas.three_p_callback.filter(item_three='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('*ХЛОПОК*')
    time.sleep(0.1)
    await call.message.edit_text('У главных ворот ты встречаешь ворона по кличке Цезарь. У него три рта, но произносит от только одно: "gdqlory". Когда ты это слышишь, то понимаешь, что это слово принадлежит тебе, жители замка знают тебя именно под этим именем.', reply_markup=key.four_keyboard)
    await call.answer()

# Четвертый пункт назад
@dp.callback_query_handler(call_datas.four_p_callback.filter(item_four='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('А теперь соберись. Будет необходим весь твой накопленный опыт и все знания, полученные ранее.', reply_markup=key.three_keyboard)
    await call.answer()

# Пятый пункт
@dp.callback_query_handler(call_datas.four_p_callback.filter(item_four='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Ты подходишь к замку и видишь большую дверь, внизу аккуратно располагается ключ. На ключе виднеется надпись "a4a23c4141b4b238a02ec479603fef08". Как только ты ее увидел, в твоей голове сразу же возникло воспоминание о протоколе pptp и кадры из фильма с чарли ЧАПлином. Ты пытаешься вспомнить название этого известного фильма, но вспоминаешь только первые три символа: "md5..."', reply_markup=key.five_keyboard)
    await call.answer()

# Пятый пункт назад
@dp.callback_query_handler(call_datas.five_p_callback.filter(item_five='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('*ХЛОПОК*')
    time.sleep(0.1)
    await call.message.edit_text('У главных ворот ты встречаешь ворона по кличке Цезарь. У него три рта, но произносит от только одно: "gdqlory". Когда ты это слышишь, то понимаешь, что это слово принадлежит тебе, жители замка знают тебя именно под этим именем.', reply_markup=key.four_keyboard)
    await call.answer()

# Шестой пункт
@dp.callback_query_handler(call_datas.five_p_callback.filter(item_five='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('*ХЛОПОК*')
    time.sleep(0.1)
    await call.message.edit_text('Оказалось, что это был всего лишь сон. Проснувшись, ты обнаруживаешь в своих руках карту с замком. На нем написано "ntrbxw-ftzb, sle sykhpeo jfzc, ftjqc-rwz, wbzcnec-pitey". В твоей голове смутно мелькают воспоминания о Вижнере..и ты видишь ключ.', reply_markup=key.sex_keyboard)
    await call.answer()

# Шестой пункт назад
@dp.callback_query_handler(call_datas.sex_p_callback.filter(item_sex='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Ты подходишь к замку и видишь большую дверь, внизу аккуратно располагается ключ. На ключе виднеется надпись "a4a23c4141b4b238a02ec479603fef08". Как только ты ее увидел, в твоей голове сразу же возникло воспоминание о протоколе pptp и кадры из фильма с чарли ЧАПлином. Ты пытаешься вспомнить название этого известного фильма, но вспоминаешь только первые три символа: "md5..."', reply_markup=key.five_keyboard)
    await call.answer()

# седьмой пункт
@dp.callback_query_handler(call_datas.sex_p_callback.filter(item_sex='general_issues'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Я сказал тебе все, что мог. Для поиска подходящей замочной скважины тебе придется пройти их все... Все 65536.', reply_markup=key.seven_keyboard)
    await call.answer()

# седьмой пункт назад
@dp.callback_query_handler(call_datas.seven_p_callback.filter(item_seven='back'))
async def help_key(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('*ХЛОПОК*')
    time.sleep(0.1)
    await call.message.edit_text('Оказалось, что это был всего лишь сон. Проснувшись, ты обнаруживаешь в своих руках карту с замком. На нем написано "ntrbxw-ftzb, sle sykhpeo jfzc, ftjqc-rwz, wbzcnec-pitey". В твоей голове смутно мелькают воспоминания о Вижнере..и ты видишь ключ.', reply_markup=key.sex_keyboard)
    await call.answer()

# Печатать по буквам
async def one_symbal(text, chat_id, mes_id):
    s = ''
    for i in text:
        s += i
        if i == ' ':
            continue
        await bot.edit_message_text(s, chat_id, mes_id)
        time.sleep(0.1)