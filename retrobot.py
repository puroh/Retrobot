import credential # archivo con las contraseñas y keys privadas.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import User


def help(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id = chat_id, text = 'Bienvenido a @NOMBRE_BOT, con este bot podras consultar algunas caracteristicas.')
    print('despues mensaje')
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def main():    
    updater = Updater(credential.token['token'], use_context=True)    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help',help))
    dp.add_error_handler(error)
    # Start the bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
