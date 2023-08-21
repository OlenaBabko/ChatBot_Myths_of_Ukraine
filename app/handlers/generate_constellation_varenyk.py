from .handler import BaseHandler
#from handlers.handler import BaseHandler
from utils import button
from utils.load_json import load_json_file, choose_random_element_by_date
import random

class GenerateConstellationHandlerVarenyk(BaseHandler):
    @property
    def message_text(self):

        data = load_json_file("handlers/constellation_varenyk.json")
        text = random.choice(data)
        return f"""
Твоя доля:
{text}        
        """

    @property
    @button.back_button
    def reply_markup(self):
        return [["Вареник з передбаченням 😉"]]
