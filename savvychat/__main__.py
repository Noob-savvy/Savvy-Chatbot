import asyncio
import importlib

from pyrogram import idle

from savvychat import LOGGER, savvychat
from savvychat.modules import ALL_MODULES

async def anony_boot():
    try:
        await savvychat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("savvychat.modules." + all_module)

    LOGGER.info(f"Successfully imported all modules.....")
    
    await idle()
    await savvychat.stop()
    LOGGER.info("Stopping savvychat Bot...")
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    
