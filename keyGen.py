from telethon import Button

def keyGenerator(status):
    if(status == "menu"):
        return [[Button.inline("Вернуться в меню", b"menu")]]
    elif(status == "confirming_message"):
        return [[Button.inline("Да, я уверен (начать рассылку)", b"start_sending")],[Button.inline("Нет, я ошибся (написать заново)", b"creating_message")]]
    elif(status == "start"):
        return [[Button.inline("Меню", b"menu")]]
    elif(status == "creating_message"):
        return [Button.inline("Создать сообщения для рассылки", b"creating_message")]