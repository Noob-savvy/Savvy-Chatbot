import asyncio
import importlib


from pyrogram import idle, errors

from savvychat import LOGGER, savvychat
from savvychat.modules import ALL_MODULES


async def Savvy_boot():
    try:
        await savvychat.start()
    except errors.exceptions.flood_420 as e:
        wait_time = int(str(e).split("_")[2])
        LOGGER.warning(f"Got FloodWait error, waiting for {wait_time} seconds...")
        await asyncio.sleep(wait_time)
        await Savvy_boot()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("savvychat.modules." + all_module)
       
    LOGGER.info("Imported all modules successfully.......")
    LOGGER.info(f"@{savvychat.username} is alive now..")
    
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Savvy_boot())
    LOGGER.info("Stopping savvychat Bot...")
