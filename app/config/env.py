import os

from dotenv import load_dotenv

if os.getenv("ENVIRONMENT") == "development":
    dev_dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env.dev")
    if not os.path.isfile(os.path.join(dev_dotenv_path)):
        raise FileNotFoundError(
            "The .env.dev file is missing. Please make sure to create the .env.dev file with the required environment variables."
        )
    load_dotenv(dev_dotenv_path)
else:
    load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN") or None
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or None
    QUOTES_PATH = "../static/quotes/ukrquotes.json"
    CONSTELLATION_PATH = "../static/constellation/constellation.json"


def get_settings() -> Settings:
    return Settings()
