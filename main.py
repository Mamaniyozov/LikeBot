from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

TOKEN = os.environ['TOKEN']


def start(update: Update,context: CallbackContext):
    bot = context.bot
    # group_id = 1898707587
    bot.send_message(chat_id='5575549228',text="Hello World")
    bot.send_message(chat_id='@image_like',text="Hello World")
   
    # update.message.reply_text("Hello World")


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
