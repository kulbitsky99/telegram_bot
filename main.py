import telebot
import config
import random
import time
from telebot import types
import json

bot = telebot.TeleBot(config.TOKEN)


#main_bot
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Каталог 🗂")
    item2 = types.KeyboardButton("Ссылка на наш сайт 🔗")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - бот <b>{1.first_name}</b>, помогающий Вам выбрать лучший электронный девайс! Если вы хотите увидеть содержательные отзывы на технику, а также краткое описание ее характеристик - кликните на кнопку <b>Каталог 🗂</b> под полем ввода сообщения! Если же вам нужны фотографии и полное описание продукта, переходите на наш сайт, нажав на поле <b>Ссылка на наш сайт 🔗</b>. Приятных покупок!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Каталог 🗂':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Фотоаппараты", callback_data='photos')
            item2 = types.InlineKeyboardButton("Телефоны", callback_data='phones')
            item3 = types.InlineKeyboardButton("Наушники", callback_data='headphones')
            item4 = types.InlineKeyboardButton("Часы", callback_data='clocks')
            item5 = types.InlineKeyboardButton("Ноутбуки", callback_data='notebooks')
            item6 = types.InlineKeyboardButton("Планшеты", callback_data='tablets')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Каталог товаров для Вас!', reply_markup=markup)
            #bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Ссылка на наш сайт 🔗':
            bot.send_message(message.chat.id, 'Наш сайт: http://mich.belarus.tilda.ws')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            #json_parser
            with open("words_main.json") as f:
                data = json.load(f)

                model = [None]*len(data)
                prise = [None]*len(data)
                country = [None]*len(data)
                mark = [None]*len(data)
                description = [None]*len(data)
                link = [None]*len(data)
                review = [None]*len(data) 

                for elem in data:
                    model[elem['_id']] = elem["model"]
                    prise[elem['_id']] = elem["prise"]
                    country[elem['_id']] = elem["country"]
                    mark[elem['_id']] = elem["mark"]
                    description[elem['_id']] = elem["descripton"]
                    link[elem['_id']] = elem["link"]
                    review[elem['_id']] = elem["review"]
            
            #photos handler       
            if call.data == 'photos':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Зеркальный фотоаппарат Canon EOS 6D Body", callback_data='p1')
                item2 = types.InlineKeyboardButton("Зеркальный фотоаппарат Canon EOS 5D Mark III Body", callback_data='p2')
                item3 = types.InlineKeyboardButton("Canon EOS 6D Mark II Body", callback_data='p3')
                item4 = types.InlineKeyboardButton("Nikon D610 Body", callback_data='p4')
                item5 = types.InlineKeyboardButton("Nikon D780 Body", callback_data='p5')
                item6 = types.InlineKeyboardButton("Беззеркальный фотоаппарат Sony Alpha a7 II Body (ILCE-7M2B)", callback_data='p6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какой фотоаппарат вам по душе?', reply_markup=markup)
                #bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'p1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[0], prise[0], country[0], mark[0], description[0], link[0], review[0], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'p2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[1], prise[1], country[1], mark[1], description[1], link[1], review[1], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'p3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[2], prise[2], country[2], mark[2], description[2], link[2], review[2], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'p4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[3], prise[3], country[3], mark[3], description[3], link[3], review[3], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'p5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[4], prise[4], country[4], mark[4], description[4], link[4], review[4], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'p6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[5], prise[5], country[5], mark[5], description[5], link[5], review[5], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
                     
                     
            #phones handler                                                   
            elif call.data == 'phones':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Apple iPhone 13 128GB (темная ночь)", callback_data='ph1')
                item2 = types.InlineKeyboardButton("Apple iPhone 12 64GB (черный)", callback_data='ph2')
                item3 = types.InlineKeyboardButton("Apple iPhone 11 64GB (черный)", callback_data='ph3')
                item4 = types.InlineKeyboardButton("Apple iPhone X 64GB (серый космос)", callback_data='ph4')
                item5 = types.InlineKeyboardButton("Apple iPhone SE 64GB (черный)", callback_data='ph5')
                item6 = types.InlineKeyboardButton("Samsung Galaxy S21 5G 8GB/128GB (серый фантом)", callback_data='ph6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какой телефон вам по душе?', reply_markup=markup)
                #bot.send_message(call.message.chat.id, 'Бывает 😢')
                
            elif call.data == 'ph1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[6], prise[6], country[6], mark[6], description[6], link[6], review[6], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'ph2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[7], prise[7], country[7], mark[7], description[7], link[7], review[7], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'ph3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[8], prise[8], country[8], mark[8], description[8], link[8], review[8], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'ph4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[9], prise[9], country[9], mark[9], description[9], link[9], review[9], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'ph5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[10], prise[10], country[10], mark[10], description[10], link[10], review[10], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'ph6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[11], prise[11], country[11], mark[11], description[11], link[11], review[11], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            
            #headphones handler    
            elif call.data == 'headphones':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Наушники Samsung Galaxy Buds 2 (черный)", callback_data='h1')
                item2 = types.InlineKeyboardButton("Наушники Samsung Galaxy Buds Live (черный)", callback_data='h2')
                item3 = types.InlineKeyboardButton("Наушники Samsung Galaxy Buds Pro (черный)", callback_data='h3')
                item4 = types.InlineKeyboardButton("Наушники Apple AirPods Pro (без поддержки MagSafe)", callback_data='h4')
                item5 = types.InlineKeyboardButton("Наушники Apple AirPods 3", callback_data='h5')
                item6 = types.InlineKeyboardButton("Наушники Apple AirPods Max (серый космос)", callback_data='h6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какие наушники вам по душе?', reply_markup=markup)
            elif call.data == 'h1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[18], prise[18], country[18], mark[18], description[18], link[18], review[18], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'h2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[19], prise[19], country[19], mark[19], description[19], link[19], review[19], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'h3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[20], prise[20], country[20], mark[20], description[20], link[20], review[20], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'h4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[21], prise[21], country[21], mark[21], description[21], link[21], review[21], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'h5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[22], prise[22], country[22], mark[22], description[22], link[22], review[22], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'h6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[23], prise[23], country[23], mark[23], description[23], link[23], review[23], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html')    
                
                
            #clocks handler    
            elif call.data == 'clocks':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Умные часы Apple Watch Series 7 45 мм (темная ночь/темная ночь спортивный)", callback_data='c1')
                item2 = types.InlineKeyboardButton("Умные часы Apple Watch SE 44 мм (алюминий серый космос/черный спортивный)", callback_data='c2')
                item3 = types.InlineKeyboardButton("Умные часы Apple Watch Series 6 44 мм (алюминий синий/темный ультрамарин)", callback_data='c3')
                item4 = types.InlineKeyboardButton("Умные часы Samsung Galaxy Watch3 45мм (черный)", callback_data='c4')
                item5 = types.InlineKeyboardButton("Умные часы Samsung Galaxy Watch Active2 40мм (ваниль)", callback_data='c5')
                item6 = types.InlineKeyboardButton("Умные часы Samsung Galaxy Watch 46мм (серебристая сталь)", callback_data='c6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какие часы вам по душе?', reply_markup=markup)
            elif call.data == 'c1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[12], prise[12], country[12], mark[12], description[12], link[12], review[12], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'c2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[13], prise[13], country[13], mark[13], description[13], link[13], review[13], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'c3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[14], prise[14], country[14], mark[14], description[14], link[14], review[14], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'c4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[15], prise[15], country[15], mark[15], description[15], link[15], review[15], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'c5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[16], prise[16], country[16], mark[16], description[16], link[16], review[16], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'c6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[17], prise[17], country[17], mark[17], description[17], link[17], review[17], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html')    
                
            #notebooks handler    
            elif call.data == 'notebooks':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Ноутбук Apple Macbook Pro 14 M1 Pro 2021 MKGR3", callback_data='n1')
                item2 = types.InlineKeyboardButton("Ноутбук Apple Macbook Air 13 M1 2020 MGN63", callback_data='n2')
                item3 = types.InlineKeyboardButton("Ноутбук Apple MacBook Pro 16 2019 MVVJ2", callback_data='n3')
                item4 = types.InlineKeyboardButton("Ноутбук Xiaomi Mi Notebook Pro 15.6 2019 JYU4118CN", callback_data='n4')
                item5 = types.InlineKeyboardButton("Ноутбук Xiaomi Mi Notebook Pro 15.6 GTX JYU4199CN", callback_data='n5')
                item6 = types.InlineKeyboardButton("Ноутбук Xiaomi RedmiBook 16 JYU4275CN", callback_data='n6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какой ноутбук вам по душе?', reply_markup=markup)
            elif call.data == 'n1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[24], prise[24], country[24], mark[24], description[24], link[24], review[24], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'n2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[25], prise[25], country[25], mark[25], description[25], link[25], review[25], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'n3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[26], prise[26], country[26], mark[26], description[26], link[26], review[26], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'n4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[27], prise[27], country[27], mark[27], description[27], link[27], review[27], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'n5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[28], prise[28], country[28], mark[28], description[28], link[28], review[28], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 'n6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[29], prise[29], country[29], mark[29], description[29], link[29], review[29], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html')
                     
                         
            #tablets handler    
            elif call.data == 'tablets':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton("Планшет Apple iPad 10.2 2021 64GB MK2K3 (серый космос)", callback_data='t1')
                item2 = types.InlineKeyboardButton("Планшет Apple iPad Pro 11 2020 128GB MY232 (серый космос)", callback_data='t2')
                item3 = types.InlineKeyboardButton("Планшет Apple iPad Air 2020 64GB (небесно-голубой)", callback_data='t3')
                item4 = types.InlineKeyboardButton("Планшет Huawei MatePad 10.4 BAH3-L09 64GB LTE (полночный серый)", callback_data='t4')
                item5 = types.InlineKeyboardButton("Планшет Samsung Galaxy Tab A7 Wi-Fi 64GB (темно-серый)", callback_data='t5')
                item6 = types.InlineKeyboardButton("Планшет Samsung Galaxy Tab S7 Wi-Fi (черный)", callback_data='t6')
                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(call.message.chat.id, 'Какой планшет вам по душе?', reply_markup=markup)
            elif call.data == 't1':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[30], prise[30], country[30], mark[30], description[30], link[30], review[30], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 't2':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[31], prise[31], country[31], mark[31], description[31], link[31], review[31], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 't3':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[32], prise[32], country[32], mark[32], description[32], link[32], review[32], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 't4':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[33], prise[33], country[33], mark[33], description[33], link[33], review[33], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 't5':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[34], prise[34], country[34], mark[34], description[34], link[34], review[34], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html') 
            elif call.data == 't6':
                bot.send_message(call.message.chat.id,
                     "Модель 📸 : {}\n\nЦена 💸 : {}\n\nПроизводитель 🌍 : {}\n\nОценка с Onliner.by ✅ : {}\n\nОписание модели ⚙️ : {}\n\nСсылка на товар, где вы можете увидеть фото товара и его более подробные характеристики : {}\n\nСодержательный отзыв на товар 🤔 : {}".format(model[35], prise[35], country[35], mark[35], description[35], link[35], review[35], 
                         call.message.from_user, bot.get_me()),
                     parse_mode='html')    

            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
            #                       reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #                         text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))

# RUN
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)
