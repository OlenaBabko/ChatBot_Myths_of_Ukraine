from .handler import BaseHandler
from telegram import Update, ReplyKeyboardMarkup
from utils import button
from utils.load_json import load_json_file, choose_random_element_by_date
import re
from datetime import datetime

def whoareyou (date: str) -> str:

    user_birthdate = datetime.strptime(date, "%d.%m.%Y")
    day = user_birthdate.day
    month = user_birthdate.month

    if ((day >= 20 and month == 1) or (day <= 19 and month == 2)):
        return "Водяник"
    elif ((day >= 20 and  month == 2) or ( day <= 20 and  month == 3))  :
         return "Русалка"
    elif ((day >= 21 and  month == 3) or (day <= 19 and  month == 4))  :
         return "Баран"
    elif ((day >= 20 and  month == 4) or ( day <= 20 and  month == 5))  :
         return "Тур"
    elif ((day >= 21 and  month == 5) or (day <= 21 and  month == 6))  :
         return "Ворота"
    elif ((day >= 22 and  month == 6) or (day <= 22 and  month == 7))  :
         return "Дід"
    elif ((day >= 23 and  month == 7) or (day <= 22 and  month == 8))  :
         return "Ворон"
    elif ((day >= 23 and  month == 8) or (day <= 22 and  month == 9))  :
         return "Панна"
    elif (( day >= 23 and  month == 9) or (day <= 22 and  month == 10))  :
         return "Доля"
    elif (( day >= 23 and  month == 10) or (day <= 21 and  month == 11))  :
         return "Громовик"
    elif (( day >= 23 and  month == 11) or (day <= 21 and  month == 12))  :
         return "Господар"
    elif (( day >= 22 and  month == 12) or (day <= 19 and  month == 1))  :
         return "Коза"


class GenerateConstellationHandler(BaseHandler):
    #@property
    def message_text(self,update):
        text = update.message.text
        if re.fullmatch(r'[0-3][0-9]\.[0-1][0-9]\.[12][09][0-9][0-9]', text):
            name = whoareyou (text)
            data = load_json_file("handlers/constellation.json")
            dic = data[name]
            constellation = dic['constellation']
            horoscope = dic['horoscope']

            return f"""
Вітаю, ти {name}  
Твоє місце - {constellation}
Знай, шо {horoscope}                          
"""
        else:
            return """
Дізнайся свій гороскоп, створений на основі українських міфів та архетипів. 
Цей гороскоп допоможе знайти гармонію з навколишнім світом.
Введи дату  народження 😉 (формат: дд.мм.ггг)
"""

    @property
    @button.back_button
    def reply_markup(self):
        return [["Гороскоп від Мольфара"]]

    async def __call__(self, update: Update):
        reply_markup = ReplyKeyboardMarkup(self.reply_markup, resize_keyboard=True)
        await update.message.reply_text(self.message_text(update),
        reply_markup=reply_markup)
