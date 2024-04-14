from pyrogram import Client, filters
from pyrogram.types import Message
from savvychat import savvychat

@savvychat.on_message(filters.command(["math","solve"], prefixes="/"))
async def calculate_math(client, message):
    divy = await message.reply_text(".......SOLVING....... ") 
    await asyncio.sleep(1.3)
    await divy.edit("➗")
    await asyncio.sleep(0.2)
    await divy.edit("✖️")
    await asyncio.sleep(0.2)
    await divy.edit("➕")
    await asyncio.sleep(1.3)
    await divy.edit("➖")
    await asyncio.sleep(0.2)
    await divy.edit("🟰")
    await asyncio.sleep(0.2)
    await divy.delete()
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)
