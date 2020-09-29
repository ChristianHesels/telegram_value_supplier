from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

class ValueSupplier:
    __instance = None
    token = ''

    def __init__(self):
        if ValueSupplier.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            print("Start ValueSupplier Bot..")	
            print("Initial value is '0'")
            self.value = 0
            ValueSupplier.__instance = self
            self.updater = Updater(token=self.token, use_context=True)
            dispatcher = self.updater.dispatcher
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.INFO)
            get_value_handler = CommandHandler('get_value', self.get_value)
            dispatcher.add_handler(get_value_handler)
            
            self.updater.start_polling()

    @staticmethod
    def get_instance():
        if ValueSupplier.__instance == None:
            ValueSupplier()
        return ValueSupplier.__instance

    def get_value(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(self.value))

    def set_value(self, value):
        print("Value set to '" + value + "'.")
        self.value = value



    def shutdown(self):
        print("Shutdown Telegram Bot..")
        self.updater.stop()
        print("Done.")









