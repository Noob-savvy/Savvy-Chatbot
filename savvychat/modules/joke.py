import requests
from savvychat import savvychat as app
from pyrogram import Client, filters

JOKE_API_ENDPOINT = 'https://hindi-jokes-api.onrender.com/jokes?api_key=1a6d440e3f5971eecebceee818c2'

@app.on_message(filters.command("joke"))
async def joke(_, message):
    divy = await message.reply_text("👻")
    response = requests.get(JOKE_API_ENDPOINT)
    r = response.json()
    joke_text = r['jokeContent']
    await divy.edit_text(
        f"✦ {joke_text} \n\n❁ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ [❀᭄ꦿ𝗟 𝗬 𝗞 𝗔 𝗔 [ᴬᶦ]](t.me/{app.username})\n❁ ᴍᴀᴅᴇ ʙʏ ➠ [𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚 𝕽𝖆𝖓𝖆](t.me/about_ranavanshi_divy)"
    )
