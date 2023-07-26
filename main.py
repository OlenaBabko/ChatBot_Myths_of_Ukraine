from typing import Final
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

with open('token.txt', 'r') as f:
    TOKEN = f.read()

BOT_USERNAME: Final = "@old_molfar_bot"



# COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Good evening my friend. I am Old Molfar. I will tell your horoscope according to the ancient beliefs of Ukrainians")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Old Molfar. Type me to start conversation")

async def birthday_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("put your birth date")


# RESPONSES
async def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'hi there!'
    if 'how are you' in processed:
        return 'I am good'
    
    return "Type the date correctly"

# Define functions for each menu option
async def send_constellation_details(update: Update):
    await update.message.reply_text("Дізнайтеся свій унікальний гороскоп, створений на основі українських міфів та архетипів. Цей гороскоп допоможе вам розкрити свій потенціал, зосередитися на головному та знайти гармонію з навколишнім світом.")



