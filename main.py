from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

TOKEN = os.environ['TOKEN']

def start(update: Update,context: CallbackContext):
    update.message.reply_text("Hello World")


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
