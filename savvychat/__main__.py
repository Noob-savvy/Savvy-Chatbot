import asyncio
import importlib

from pyrogram import idle

from savvychat import LOGGER, savvychat, LOGGER_ID
from savvychat.modules import ALL_MODULES


async def anony_boot():
    try:
        await savvychat.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("savvychat.modules." + all_module)

    LOGGER.info(f"@{savvychat.username} Started.")
    await self.send_message(
                chat_id=LOGGER_ID,
                text=f"<u><b>» {savvychat.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{savvychat.id}</code>\nɴᴀᴍᴇ : {savvychat.name}\nᴜsᴇʀɴᴀᴍᴇ : @{savvychat.username}",
            )
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping savvychat Bot...")
