from typing import Final
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

with open('token.txt', 'r') as f:
    TOKEN = f.read()

BOT_USERNAME: Final = "@old_molfar_bot"
