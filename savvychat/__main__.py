import asyncio
import importlib

from pyrogram import idle

from savvychat import LOGGER, savvychat
from savvychat.modules import ALL_MODULES


async def Savvy_boot():
    try:
        await savvychat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("savvychat.modules." + all_module)
       
    LOGGER.info(f"@{savvychat.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Savvy_boot())
    LOGGER.info("Stopping savvychat Bot...")
