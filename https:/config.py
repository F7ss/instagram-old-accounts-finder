import os
from dotenv import load_dotenv

load_dotenv()

# إعدادات إنستقرام
INSTA_USERNAME = os.getenv('INSTA_USERNAME')
INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')

# إعدادات تليجرام
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# إعدادات البحث
MIN_USERNAME_LENGTH = 4
YEAR_RANGE = (2010, 2016)
