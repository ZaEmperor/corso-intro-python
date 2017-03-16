from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = '332228678:AAGCZF4wP1DqRPoKmeJcMf7KKpeYGgS4JiY'


def start(bot, update):
    update.message.reply_text("Ciao!")

def controller(bot, update):
    msg = update.message.text
    import pdb; pdb.set_trace()

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, controller))
    updater.start_polling()


    updater.idle()

if __name__ == '__main__':
    main()


