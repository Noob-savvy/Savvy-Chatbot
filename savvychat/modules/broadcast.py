import asyncio

from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from pyrogram.types import Message
from pyrogram import Client, filters
from savvychat import savvychat, OWNER
from savvychat.database.chats import get_served_chats
from savvychat.database.users import get_served_users, del_user

#==========================================================================================================================
REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""
#==========================================================================================================================


@savvychat.on_message(filters.private & filters.command('broadcast') & filters.user(OWNER))
async def send_text(client: savvychat, message: Message):
    if message.reply_to_message:
        chats = await get_served_chats()
        users = await get_served_users()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in chats:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1

        group_chats = len(chats) - len(users)
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{len(users)}</code>
Total Groups: <code>{group_chats}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""

        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
