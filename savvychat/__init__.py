
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
import config
from savvychat.logger import LOGGER
from savvychat.bot import savvychat

boot = time.time()
mongo = MongoCli(config.MONGO_DB_URL)
db = mongo.Anonymous
Mongo = MongoCli(config.MONGO_URL)
Db = Mongo.divu
OWNER = config.OWNER_ID
LOGGER_ID = config.LOGGER_ID

#bot client
savvychat = savvychat()
