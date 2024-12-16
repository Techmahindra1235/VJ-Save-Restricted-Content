import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22555631"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fa01340f331aa1bfa112d863ade8a142")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7131325321"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vermaaditi708:WMGYHyX1bk2Yx8TW@cluster0.rj8ln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
