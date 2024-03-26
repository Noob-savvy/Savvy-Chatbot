
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import savvychat
from config import *
from ..modules.helpers.inline import *
#  bard 
x=None
@savvychat.on_message(filters.command(["bard"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bard_chat(bot, message):
    global x
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/bard write shorts notes on human eyes`")
    else:
        a = message.text.split(' ', 1)[1]
    
    try:
        response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
        if response.status_code==200:
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            x=response.json()["results"]
            
            await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{savvychat.username} ",reply_markup=InlineKeyboardMarkup(GPT_BTN),quote=True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass
        
#========================================================bard=======================================#
@savvychat.on_message(filters.command(["bard"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def bard_chat(bot, message):
    if len(message.command) < 2:
        await message.reply_text(
            "Example:**\n\n`/bard tell me about Python programming`")
    else:
        a = message.text.split(' ', 1)[1]

        try:
            response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}')
            if response.status_code == 200:
                await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
                x = response.json()["results"]

                await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{savvychat.username} ", reply_markup=InlineKeyboardMarkup(GPT_BTN), quote=True)
            else:
                pass

        except requests.exceptions.RequestException as e:
            pass
