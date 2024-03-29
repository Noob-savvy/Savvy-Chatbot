import sys

from pyrogram import Client
from savvychat.logger import LOGGER
import config


class savvychat(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="savvychat",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            lang_code="en",
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        LOGGER(__name__).info(f"Bot Started as {self.name}")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {self.name} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :**\n\n✨ ɪᴅ : `{self.id}`\n❄ ɴᴀᴍᴇ : {self.name}\n💫 ᴜsᴇʀɴᴀᴍᴇ : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
