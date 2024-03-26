
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from .. import savvychat
from config import *
from ..modules.helpers.inline import *
from pyrogram.enums import ChatAction


@savvychat.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chatgpt_chat(bot, message):
    
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt write simple website code using html css ,js?`")
    else:
        a = message.text.split(' ', 1)[1]

    try:
        response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={a}') 
        if response.status_code==200:
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            x=response.json()["results"]
            
            await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{savvychat.username} ",reply_markup=InlineKeyboardMarkup(GPT_BTN),quote=True)  
        else:
            pass

            
    except requests.exceptions.RequestException as e:
        pass

#============================================================= CHAT GPT ==============================================================#

@savvychat.on_message(filters.command(["chatgpt","ai","ask"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def chatgpt_chat(bot, message):
    
    if len(message.command) < 2:
        await message.reply_text(
            "Example:**\n\n`/chatgpt write simple website code using html css ,js?`")
    else:
        a = message.text.split(' ', 1)[1]

        try:
            response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={a}') 
            if response.status_code == 200:
                await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
                x = response.json()["results"]
            
                await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{savvychat.username} ", reply_markup=InlineKeyboardMarkup(GPT_BTN), quote=True)  
            else:
                pass

            
        except requests.exceptions.RequestException as e:
            pass
