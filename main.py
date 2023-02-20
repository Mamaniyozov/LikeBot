from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
from likedb  import LikeDB


TOKEN = os.environ['TOKEN']
# like_db = LikeDB['likes.json']

def start(update: Update,context: CallbackContext):
    chat_id=update.message.chat.id
    mark=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="like👍",callback_data='like👍')],
        [InlineKeyboardButton(text="dislike👎",callback_data='dislike👎')]
    ])
    bot = context.bot
    bot.sendPhoto(chat_id,"https://pics.freeicons.io/uploads/icons/png/18727039041580202142-512.png",reply_markup=mark)
    update.message.reply_text("Hello World")
def query(update: Update, context: CallbackContext):
    
    
    quer=update.callback_query
    quer.answer("Loading")
    chat_id=quer.message.chat_id
    bot = context.bot
    n=0
    m=0
    if quer.data=='dislike👎':
        m=LikeDB.add_dislike()
        b=LikeDB.pop_like()
        print(m,b)
        
        update.message.reply_text("Rate the picture")
    if quer.data=='like👍':
        n=LikeDB.add_like()
        c=LikeDB.pop_dislike()
        print(n,c)
        


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
updater.idle()
