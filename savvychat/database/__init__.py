from pymongo import MongoClient

import config

Savvydb = MongoClient(config.MONGO_DB_URL)
Savvy = Savvydb["SavvyDb"]["Savvy"]


from .chats import *
from .users import *
