import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
 
app = Flask(__name__)
from main import(
    start,
    query
)


# bot
TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)

@app.route('/api', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return {'status': 200}

    elif request.method == 'POST':
        # get data from request
        data: dict = request.get_json(force=True)

        # convert data to Update obj
        update: Update = Update.de_json(data, bot)

        # Dispatcher
        dp: Dispatcher = Dispatcher(bot, None, workers=0)
        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(CallbackQueryHandler(query))

        # process update
        dp.process_update(update=update)

        return {'status': 200}
if __name__ == '__main__':
    # Run the app in local network
    app.run()
    
print(bot.get_webhook_info())