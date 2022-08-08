
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    text = 'вызван /start'
    print(text)
    update.message.reply_text('здравствуй, пользователь. введи команду /planet, чтобы узнать в каком созвездии сегодня находится планета')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet (update,context):
    print('вызван /planet')
    message = update.message.text.split()[1]
    print(message)

    if message =='Venus':
        update.message.reply_text(ephem.constellation(ephem.Venus('2022/08/08')))
    elif message == 'Mars':
        update.message.reply_text(ephem.constellation(ephem.Mars('2022/08/08')))
    elif message == 'Mercury':
         update.message.reply_text(ephem.constellation(ephem.Mercury('2022/08/08')))
    elif message == 'Jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter('2022/08/08')))
    elif message == 'Saturn':
         update.message.reply_text(ephem.constellation(ephem.Saturn('2022/08/08')))
    elif message == 'Uranus':
         update.message.reply_text(ephem.constellation(ephem.Uranus('2022/08/08')))
    elif message == 'Neptune':
         update.message.reply_text(ephem.constellation(ephem.Neptune('2022/08/08')))
    elif message == 'Pluto':
         update.message.reply_text(ephem.constellation(ephem.Pluto('2022/08/08')))
    else:
        update.message.reply_text('используй только планеты солнечной системы')
def main():
    mybot = Updater("5453490042:AAGJgGvrSTT7RYw7uEuOMxnrtHTro-zV-hs", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
