from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import keybords.inline.callback_datas as key

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.menu_callback.new(item_menu='general_issues')),
        ],
    ]
)

one_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.one_p_callback.new(item_one='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.one_p_callback.new(item_one='back')),
        ],
    ]
)

two_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.two_p_callback.new(item_two='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.two_p_callback.new(item_two='back')),
        ],
    ]
)

three_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.three_p_callback.new(item_three='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.three_p_callback.new(item_three='back')),
        ],
    ]
)

four_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.four_p_callback.new(item_four='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.four_p_callback.new(item_four='back')),
        ],
    ]
)

five_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.five_p_callback.new(item_five='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.five_p_callback.new(item_five='back')),
        ],
    ]
)

sex_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Далее', callback_data=key.sex_p_callback.new(item_sex='general_issues')),
            InlineKeyboardButton(text='Назад', callback_data=key.sex_p_callback.new(item_sex='back')),
        ],
    ]
)

seven_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Назад', callback_data=key.seven_p_callback.new(item_seven='back')),
        ],
    ]
)