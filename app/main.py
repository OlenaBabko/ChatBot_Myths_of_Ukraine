import logging
import os
import sys

# Get the current directory
#current_directory = os.path.dirname(os.path.abspath(__file__))
# Add the current directory to the Python path
#sys.path.append(current_directory)

from config.env import get_settings

#from telegram import __version__ as TG_VER
#try:
#    from telegram import __version_info__
#except ImportError:
#    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
#if __version_info__ < (20, 0, 0, "alpha", 1):
#    raise RuntimeError(
#        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#        f"{TG_VER} version of this example, "
#        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#    )

from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext

from handlers.handler import BaseHandler
from handlers.generate_constellation import GenerateConstellationHandler
from handlers.generate_constellation_varenyk import GenerateConstellationHandlerVarenyk

env = get_settings()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)





def main() -> None:
    handler = BaseHandler()
    application = Application.builder().token(env.BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", handler))
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice))
    application.add_handler( MessageHandler(filters.Regex(r'[0-3][0-9]\.[0-1][0-9]\.[12][09][0-9][0-9]'), handle_varenyk_choice))
    application.add_handler( MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex(r'[0-3][0-9]\.[0-1][0-9]\.[12][09][0-9][0-9]'), handle_menu_choice))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

async def handle_menu_choice(update: Update, context: CallbackContext,) -> None:
    handler = BaseHandler()
    selected_option = update.message.text
    # Define functions for each menu option
    if selected_option == "Гороскоп від Мольфара":
        handler = GenerateConstellationHandler()
    elif selected_option == "Вареник з передбаченням 😉":
        handler = GenerateConstellationHandlerVarenyk()
    await handler(update)

async def handle_varenyk_choice(update: Update, context: CallbackContext, ) -> None:
    handler = GenerateConstellationHandler()
    await handler(update)

if __name__ == "__main__":
    main()
    