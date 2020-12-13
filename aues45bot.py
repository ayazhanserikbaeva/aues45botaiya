#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyTelegramBotAPI


# In[2]:


import telebot
from telebot import types
bot = telebot.TeleBot('1417046970:AAEdSOprR2FZvPSI_t1qUiCuifjN2sW1_fQ')


# In[ ]:


RK1=0
RK2=0
SR=0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Введи баллы РК1:')
    bot.register_next_step_handler(message, get_RK1) 
    
@bot.message_handler(commands=['help'])    
def helpcom(message):
    bot.send_message(message.from_user.id, 'По всем вопросам: @MeAiya') 

def get_RK1(message): 
    global RK1
    try:
        RK1 = int(message.text)
        if RK1<=100 and RK1>=0:
            bot.send_message(message.from_user.id, 'Введи баллы РК2:')
            bot.register_next_step_handler(message, get_RK2) 
        else:
            bot.send_message(message.from_user.id, 'Введи баллы корректно.')
            bot.register_next_step_handler(message, get_RK1)
    except Exception:
        bot.send_message(message.from_user.id, 'Введи баллы корректно.')
        bot.register_next_step_handler(message, get_RK1)
            
    
def get_RK2(message): 
    global RK2 
    try:
        RK2 = int(message.text)
        if RK2<=100 and RK2>=0:
            bot.send_message(message.from_user.id, 'Введи баллы cредний текущий:')
            bot.register_next_step_handler(message, get_SR) 
        else:
            bot.send_message(message.from_user.id, 'Введи баллы корректно.')
            bot.register_next_step_handler(message, get_RK2)
    except Exception:
        bot.send_message(message.from_user.id, 'Введи баллы корректно.')
        bot.register_next_step_handler(message, get_RK2)
    
    
        
def get_SR(message): 
    global SR
    try:
        SR = int(message.text)
        if SR<=100 and SR>=0:
            bot.send_message(message.from_user.id, 'Напишите /level')
            bot.register_next_step_handler(message, get_text_messages)
        else:
            bot.send_message(message.from_user.id, 'Введи баллы корректно.')
            bot.register_next_step_handler(message, get_SR)
    except Exception:
        bot.send_message(message.from_user.id, 'Введи баллы корректно.')
        bot.register_next_step_handler(message, get_SR)

    
    
@bot.message_handler(commands=['text'])
def get_text_messages(message):
    if message.text == '/level':
        keyboard = types.InlineKeyboardMarkup()

        key_stip = types.InlineKeyboardButton(text='Стипендия', callback_data='stip')
        keyboard.add(key_stip)

        key_povich = types.InlineKeyboardButton(text='Повышка', callback_data='povich')
        keyboard.add(key_povich)
        bot.send_message(message.from_user.id, text='Выберите что хотите расчитать:', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напишите /level')
        bot.register_next_step_handler(message, get_text_messages)
        
    

@bot.callback_query_handler(func=lambda call: True)
def send_text(call):
    if call.data=='stip':
        stip=((((((((int(RK1)+int(RK2))/int(2))*float(0.2)) + (int(SR)*float(0.8))) *float(0.6)) - int(70.0))/float(0.4))*(-1));
        if stip > 100:
            bot.send_message(call.message.chat.id, 'К сожаленю, для стипендии вам надо на экзамене набрать больше 100. ')
        else:
            bot.send_message(call.message.chat.id, 'Для стипендии вам надо на экзамене набрать ' + str(stip))
        
        
    elif call.data=='povich':  
        povich=((((((((int(RK1)+int(RK2))/int(2))*float(0.2)) + (int(SR)*float(0.8))) *float(0.6)) - int(90.0))/float(0.4))*(-1));
        if povich > 100:
            bot.send_message(call.message.chat.id, 'К сожаленю, для повышки вам надо на экзамене набрать больше 100. ')
        else:
            bot.send_message(call.message.chat.id, 'Для повышки вам надо на экзамене набрать ' + str(povich))
        

        
        
bot.polling(none_stop=True, interval=0)

