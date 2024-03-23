
# ---------------------------------------------

from os import getenv

from dotenv import load_dotenv

load_dotenv()
# -----------------------------------------------
API_ID = "20419271"
# -------------------------------------------------------------
API_HASH = "acdae9b36fd2fa77967598829d7e73a6"
# ---------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN",None)
# --------------------------------------------
OWNER_USERNAME = "cute_divuu"
# -------------------------------------------
OWNER_ID = getenv("OWNER_ID","6810304102")
# -----------------------------------------------
MONGO_URL = getenv("MONGO_URL", None)
# ------------------------------------------------
LOGGER_ID = getenv("LOGGER_ID","-1002055978397")
# ------------------------------------------------

SUPPORT_GRP = "savvy_robot_support"
UPDATE_CHNL = "Savvy_robot_update"