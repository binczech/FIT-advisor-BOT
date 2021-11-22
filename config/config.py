import os
from dotenv import load_dotenv


load_dotenv()


class Config:

    extensions = ['trololo']
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    LOG_CHANNEL = os.getenv('LOG_CHANNEL')
    WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL')
    STORNO_CHANNEL = os.getenv('STORNO_CHANNEL')
