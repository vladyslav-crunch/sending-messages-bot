from dotenv import load_dotenv
from os import getenv


load_dotenv()
MANAGER_APP_ID: int = getenv("MANAGER_APP_ID")
MANAGER_API_HASH: str = getenv("MANAGER_API_HASH")
MANAGER_BOT_TOKEN:str = getenv("MANAGER_BOT_TOKEN")
SPAM_BOT_USERNAME:str = getenv("SPAM_BOT_USERNAME")