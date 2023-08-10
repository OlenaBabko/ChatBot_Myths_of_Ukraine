from telegram import Update, ReplyKeyboardMarkup

from utils import button
class BaseHandler:
    
    @property
    def message_text(self):
        return """Привіт, мій друже! 
Я - старий Мольфар. 
Тут ти можеш дізнатись свій гороскоп, згідно прадавніх вірувань Українців"""

    @property
    def reply_markup(self):
        return  [["Гороскоп від Мольфара"], ["Вареник з передбаченням 😉"]]

        
    async def __call__(self, update: Update):
        reply_markup = ReplyKeyboardMarkup(self.reply_markup, resize_keyboard=True)
        await update.message.reply_text(self.message_text,
        reply_markup=reply_markup)
        
