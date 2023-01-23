from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

TOKEN = os.environ['TOKEN']


def start(update: Update,context: CallbackContext):
    bot = context.bot
    bot.send_message(chat_id='@image_like',text="Hello World")
    update.message.reply_text("Hello World")

def sendImage(update: Update,context: CallbackContext):
    bot = context.bot
    # Get image id from update
    image_id = update.message.photo[-1].file_id

    
    bot.send_photo(chat_id='@image_like',photo=image_id,caption="Hello World")
    update.message.reply_text("Image has been sent to @image_like")

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo,sendImage))

updater.start_polling()
updater.idle()
