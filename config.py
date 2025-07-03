from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "26467271"
# -------------------------------------------------------------
API_HASH = "cdb49c92e3d8f2e51152c813dcfe15be"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7860277015"))
SUPPORT_GRP = "MusicOnMasti"
UPDATE_CHNL = "About_Zain"
OWNER_USERNAME = "Uff_Zainu"
