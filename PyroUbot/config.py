import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "7050621072").split()))

API_ID = int(os.getenv("API_ID", "22994596"))

API_HASH = os.getenv("API_HASH", "fe8f997dd2f6fd529aadfbe9181d9dc8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7909404974:AAH_jYBinH-g35VVYR8osUhKoTxWO4_6RbM")

OWNER_ID = int(os.getenv("OWNER_ID", "7050621072"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ml9079716:48gxGsQhTHWumLI15@cluster0.6e1q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002331639417"))
