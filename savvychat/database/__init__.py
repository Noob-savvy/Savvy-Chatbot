from pymongo import MongoClient

import config

Savvydb = MongoClient(config.MONGO_URL)
Savvy = Savvydb["SavvyDb"]["Savvy"]

Divudb = MongoClient(config.MONGO_DB_URL)
Divu = Divudb["DivuDb"]["Divu"]

from .chats import *
from .users import *
