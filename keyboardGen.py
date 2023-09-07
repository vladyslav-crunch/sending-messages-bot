from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def gen_markup(status):
    if(status == "start"):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Создать сообщение", callback_data="creating_message"),
                               InlineKeyboardButton("something else...", callback_data="something"))
        return markup
    elif(status == "creating_message"):
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Отмена", callback_data="cancel"))
        return markup