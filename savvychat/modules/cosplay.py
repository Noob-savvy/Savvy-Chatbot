import requests
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import ChatType  # Import ChatType from pyrogram.types
from savvychat import savvychat as app
from savvychat.modules.helpers.inline import GPT_BTN

@app.on_message(filters.command("cosplay"))
async def cosplay(_, msg):
    img = requests.get("https://waifu-api.vercel.app").json()
    await msg.reply_photo(img, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ [❀᭄ꦿ𝗟 𝗬 𝗞 𝗔 𝗔 [ᴬᶦ]](t.me/{app.username})", reply_markup=InlineKeyboardMarkup(GPT_BTN))

@app.on_message(filters.command("ncosplay"))
async def ncosplay(_, msg):
    if msg.chat.type != ChatType.PRIVATE:
        await msg.reply_text("❍ sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ ᴡɪᴛʜ ʙᴏᴛ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ɢᴏ ᴘᴍ",url=f"https://t.me/{app.username}?start=True")]
                ]
            ))
    else:
        ncosplay = requests.get("https://waifu-api.vercel.app/items/1").json()
        await msg.reply_photo(ncosplay, caption=f"❅ ᴄᴏsᴘʟᴀʏ ʙʏ ➠ [❀᭄ꦿ𝗟 𝗬 𝗞 𝗔 𝗔 [ᴬᶦ]](t.me/{app.username})", reply_markup=InlineKeyboardMarkup(GPT_BTN))
