import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6787098484").split()))

API_ID = int(os.getenv("API_ID", "27871075"))

API_HASH = os.getenv("API_HASH", "10227dd3c2fcda863b6f87977fa813be")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7683127121:AAG15ZbUOHlCnrXCdgvYCMscZ8r-DkWrxNM")

OWNER_ID = int(os.getenv("OWNER_ID", "5149934567"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ml9079716:48gxGsQhTHWumLI15@cluster0.6e1q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002331639417"))
