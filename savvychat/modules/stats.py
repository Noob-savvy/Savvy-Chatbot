from pyrogram import filters, Client
from pyrogram.types import Message

from savvychat import OWNER, savvychat
from savvychat.database.chats import get_served_chats
from savvychat.database.users import get_served_users
from config import OWNER_ID

@savvychat.on_message(filters.command("stats") & filters.private & filters.user(OWNER_ID))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""{(await cli.get_me()).mention} ᴄʜᴀᴛʙᴏᴛ sᴛᴀᴛs:

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )
