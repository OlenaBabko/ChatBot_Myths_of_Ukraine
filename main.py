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



# IF USER CONTACT A BOT
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('birthday', birthday_command))

    # MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERRORS
    app.add_error_handler(error)

    # POLLS THE BOT
    print('polling...')
    app.run_polling(poll_interval=3)