import os
from typing import List

API_ID = os.environ.get("API_ID", "23830188")
API_HASH = os.environ.get("API_HASH", "074112305db5152821d9f69b1fcb64eb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7234602291:AAENp88x_Fz8TKp5acrWnYTUIWYg_q2ykhM")
ADMIN = int(os.environ.get("ADMIN", "5528613826"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002128303524"))

DB_URI = os.environ.get("DB_URI", "mongodb+srv://ytuserbot12:30v6lYiMPLdUBM7d@cluster0.9l53pxx.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "ytuserbot12")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002480406032").split()))  # Add Multiple channel id

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyDByuRamhoTaUJ805QONBeqar08DuIMEEg")
