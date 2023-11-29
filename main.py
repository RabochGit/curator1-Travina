import telebot

bot = telebot.TeleBot('6718723182:AAG6cIWP9yFt0bu5TUathP3AmrRJkZp84XU')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, друг')


@bot.message_handler(commands=['reminder'])
def main(message):
    bot.send_message(message.chat.id, 'Всё, над чем ты работаешь, имеет огромное значение')


@bot.message_handler(commands=['relax'])
def main(message):
    bot.send_message(message.chat.id, 'Послушай приятную [музыку](https://www.youtube.com/watch?v=jfKfPfyJRdk)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['trevel'])
def main(message):
    bot.send_message(message.chat.id,
                     'Хибины — это горы на Кольском полуострове. Имеют мягкий рельеф и отличаются потрясающей природой. Там произрастает и обитает почти вся Красная книга. Большую часть года горный массив остаётся заснеженным, благодаря чему привлекает любителей горнолыжного спорта. Основные горнолыжные комплексы – на горах Айкуайвенчорр и Кукисвумчорр. Кататься можно с ноября по июнь. \nНе стоите на лыжах? Отправляйтесь на джип-сафари по полуострову, рыбачьте в изумрудных озёрах или знакомьтесь с бытом кольских оленеводов. Также из программы-минимум в Хибинах — Полярно-альпийский ботанический сад и «Снежная деревня».')


@bot.message_handler(commands=['moretrevel'])
def main(message):
    bot.send_message(message.chat.id,
                     'Посмотри [тревел-шоу] по России и выбери место, которое хочешь посетить.(https://vk.com/video/playlist/-203677279_10)',
                     parse_mode='Markdown')


bot.infinity_polling()