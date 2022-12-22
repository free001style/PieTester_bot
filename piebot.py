from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio
import aioschedule
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

bot = AsyncTeleBot(os.getenv('TOKEN'))
flag = [-1, -1, -1]
answer = ""
# all answers
answer000 = "Поздравляю! Ты ароматный пирог с вишней!\n\n" \
            "Хрустящая и рассыпчатая основа из рубленого теста," \
            " заполнена сочной рубиново-красной вишневой начинкой.\n" \
            "Ты готовишься пирог достаточно просто и получаешься очень вкусным, " \
            "ароматным, с небольшой кислинкой, которую придает тебе свежая вишня.\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer001 = "Поздравляю! Ты кисленький пирог с яблоком!\n\n" \
            "Твой потрясающий вкус - настоящий яблочный!\n" \
            "Текстура сочная, нежная и ароматная. Рецепт совершенно простой," \
            " из доступных ингредиентов. Зато аромат и хруст " \
            "теста не оставят равнодушным ни одного попробовавшего тебя человека!\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer010 = "Поздравляю! Ты сливовый пирог!\n\n" \
            "Легендарный сливовый пирог по рецепту из американской газеты «Нью-Йорк таймс». Твой рецепт  много лет " \
            "печатали на страницах газеты по просьбам читательниц, настолько ты был хорош. Песочное тесто на " \
            "сливочном масле - мягкое и рассыпчатое, сливы придают тебе сочность и необыкновенный вкус и аромат.\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer100 = "Поздравляю! Ты клубничный пирог со сметанной заливкой.\n\n" \
            "Вкуснейший пирог с ягодой к чаю на песочном тесте. " \
            "Ты хорош для на завтрака в выходной день или на любой " \
            "семейный праздник, где все оценят вкуснейшую нежную выпечку с клубникой.\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer011 = "Поздравляю! Ты курник!\n\n Очень ароматный и сочный  пирог с курицей и картошкой. Простой в " \
            "приготовлении, из теста на кефире. Всё в тебе хорошо: куриное филе, нежный картофель и сладкий лук. Ты " \
            "нежный и сытный. Прекрасно подходишь к праздничному столу и понравишься родным и гостям!\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer101 = "Поздравляю! Ты киш с ветчиной и сыром!\n\nДовольно популярный вид выпечки. Ты готовишься из рубленного " \
            "теста, которое по своей текстуре напоминает песочную основу. Твоей особенностью является то, " \
            "тебя выпекают открытым, а начинку покрывают специальной заливкой из яиц, сливок и сыра. Есть тебя можно " \
            "холодным и горячим - хорошо будет по всякому.\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer110 = "Поздравляю! Ты пирог с мясом!\n\nТы - универсальное блюдо, которое можно готовить в качестве второго на " \
            "обед, ужин, подавать к завтраку, брать с собой на пикник или предлагать гостям на праздничном столе. Ты " \
            "сытный и сочный. Пропечённый и мягкий. Есть тебя - одно удовольствие!\n" \
            "Чтобы пройти опрос заново, тыкни reset"
answer111 = "Поздравляю! Ты пирог с шампиньонами!\n\nКак и другие пироги с грибной начинкой, ты - распространенное " \
            "блюдо, для которого нужны самые простые продукты. Готовят тебя из слоеного или дрожжевого теста. Твоей " \
            "начинке не нужна дополнительная тепловая обработка, поэтому процесс приготовления сильно ускоряется.\n" \
            "Чтобы пройти опрос заново, тыкни reset"


@bot.message_handler(commands=['start'])
async def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Quest1")
    item2 = types.KeyboardButton("Quest2")
    item3 = types.KeyboardButton("Quest3")
    item4 = types.KeyboardButton("reset")
    item5 = types.KeyboardButton("result")
    markup.add(item1, item2, item3, item4, item5)

    await bot.send_message(message.chat.id,
                           'Приветствую, {0.first_name}!\n''Я — <b>PieTester</b>\n''И именно я и мой отец поможем тебе понять, кто ты из пирогов и из какого теста ты сделан)))\n''Тыкай на кнопки, чтобы пройти тест.'.format(
                               message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
async def questions(message):
    if message.text == "Quest1":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Сладкий", callback_data='Сладкий')
        item2 = types.InlineKeyboardButton("Солёный", callback_data='Солёный')
        markup.add(item1, item2)
        await bot.send_message(message.chat.id, "Ты сладкий или солёный пирог?", reply_markup=markup)
    elif message.text == "Quest2":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Дрожжевое", callback_data='Дрожжевое')
        item2 = types.InlineKeyboardButton("Песочное", callback_data='Песочное')
        markup.add(item1, item2)
        await bot.send_message(message.chat.id, "Ты пирог из дрожжевого "
                                                "теста или из песочного?", reply_markup=markup)
    elif message.text == "Quest3":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Крошкой из теста", callback_data='Крошкой из теста')
        item2 = types.InlineKeyboardButton('Вы что, какие украшения!?', callback_data='Вы что, какие украшения!?')
        markup.add(item1, item2)
        await bot.send_message(message.chat.id, "Чем ты украшен?", reply_markup=markup)

    elif message.text == "result":
        global answer
        global flag
        answer = ""
        if -1 in flag:
            await bot.send_message(message.chat.id, "Пройди тест")
        for i in flag:
            answer += str(i)
        if answer == "000":
            await bot.send_message(message.chat.id, answer000)
        if answer == "001":
            await bot.send_message(message.chat.id, answer001)
        if answer == "010":
            await bot.send_message(message.chat.id, answer010)
        if answer == "100":
            await bot.send_message(message.chat.id, answer100)
        if answer == "011":
            await bot.send_message(message.chat.id, answer011)
        if answer == "101":
            await bot.send_message(message.chat.id, answer101)
        if answer == "110":
            await bot.send_message(message.chat.id, answer110)
        if answer == "111":
            await bot.send_message(message.chat.id, answer111)

    elif message.text == "reset":
        flag = [-1, -1, -1]
        answer = ""
        await bot.send_message(message.chat.id, "Можете теперь пройти опросник заново)")

    else:
        await bot.send_message(message.chat.id, "Неверная команда")


@bot.callback_query_handler(func=lambda call: True)
async def callback_inline(call):
    global flag
    if call.message:
        cmci = call.message.chat.id
        if call.data == 'Солёный':
            flag[0] = 1
        if call.data == "Сладкий":
            flag[0] = 0
        if call.data == 'Песочное':
            flag[1] = 1
        if call.data == 'Дрожжевое':
            flag[1] = 0
        if call.data == 'Вы что, какие украшения!?':
            flag[2] = 1
        if call.data == 'Крошкой из теста':
            flag[2] = 0
        await bot.edit_message_text(chat_id=cmci, message_id=call.message.message_id,
                                    text='Переходи к следующему вопросу или, если это был последний вопрос, то тыкай на result',
                                    reply_markup=None)


async def scheduler():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(bot.infinity_polling(), scheduler())


if __name__ == "__main__":
    asyncio.run(main())
