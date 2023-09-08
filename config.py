from dotenv import load_dotenv
from os import getenv


load_dotenv()
APP_ID: int = getenv("APP_ID")
API_HASH: str = getenv("API_HASH")
BOT_TOKEN:str = getenv("BOT_TOKEN")
SPAM_BOT_USERNAME:str = getenv("SPAM_BOT_USERNAME")