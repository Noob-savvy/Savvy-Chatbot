
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import savvychat
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.helpers.inline import *



x=None
#blackbox
@savvychat.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Example:**\n\n`/blackbox write simple flask app code`")
    else:
        a = message.text.split(' ', 1)[1]

        try:
            response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
            if response.status_code == 200:
                await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
                x = response.json()["results"]
            
                await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{savvychat.username} ", reply_markup=InlineKeyboardMarkup(GPT_BTN), quote=True, disable_web_page_preview=True)  
            else:
                pass

        except requests.exceptions.RequestException as e:
            pass
