import credential # archivo con las contraseñas y keys privadas.

#librerias de telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import User

#Librerias de chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer

# Entreanmiento del bot

bot = ChatBot(
    'Mr. Sypher',
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    #logic_adapters=[
     #   'chatterbot.logic.MathematicalEvaluation',
      #  'chatterbot.logic.TimeLogicAdapter',
       # 'chatterbot.logic.BestMatch'
    #],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(bot)
#trainer = UbuntuCorpusTrainer(bot)

trainer.train(
    'chatterbot.corpus.english',
    #'./dataset_1MM/'
    )  



def convert_uppercase(update, context):
    print("user: ", update.message.text)
    bot_response = bot.get_response(update.message.text)
    print(f'bot: {bot_response}')
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id = chat_id, text=str(bot_response ))

def help(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id = chat_id, text = 'Bienvenido a @rtrsofkabot, habla con este bot.')
    print('despues mensaje')
    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def main():    
    updater = Updater(credential.token['token'], use_context=True)    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help',help))
    dp.add_error_handler(error)
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), convert_uppercase))
    escrito = MessageHandler(Filters.text & (~Filters.command), convert_uppercase)
    # Start the bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
