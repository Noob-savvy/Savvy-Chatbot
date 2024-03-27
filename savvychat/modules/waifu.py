from pyrogram import Client, filters
import requests
from savvychat import savvychat

waifu_api_url = 'https://api.waifu.im/search'

async def get_waifu_data(tags):
  params = {
    'included_tags': tags, 
    'height': '>=2000'
  }

  try:
    response = requests.get(waifu_api_url, params=params)
    if response.status_code == 200:
      return response.json()
    else:
      return None
  except Exception as e:
    print("API Error:", e)
    return None
    #====≠=================================================================#

async def get_husbando_data(tags):
  params = {
    'included_tags': tags, 
    'height': '>=2000'
  }

  try:
    response = requests.get(waifu_api_url, params=params)
    if response.status_code == 200:
      return response.json()
    else:
      return None
  except Exception as e:
    print("API Error:", e)
    return None
#============================== waifu =====================================:

@savvychat.on_message(filters.command("waifu"))
async def waifu_command(client, message):

  try:  
    tags = ['maid','waifu']
    waifu_data = await get_waifu_data(tags)

    if waifu_data and 'images' in waifu_data:
      first_image = waifu_data['images'][0]
      image_url = first_image['url']
      await message.reply_photo(image_url, caption=f"❀ ʜᴇʏ{message.from_user.mention}, ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴡᴀɪғᴜ \n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ") 
    else:
      await message.reply_text("No waifu found with the specified tags.")
  
  except Exception as e:
    print(e)
    await message.reply_text("An internal error occurred!")


#========================= husbando ====================================#

@savvychat.on_message(filters.command("husbando"))
async def husbando_command(client, message):

  try:  
    tags = ['servant']
    husbando_data = await get_husbando_data(tags)

    if husbando_data and 'images' in husbando_data:
      first_image = husbando_data['images'][0]
      image_url = first_image['url']
      await message.reply_photo(image_url, caption="Here is your husbando baby!") 
    else:
      await message.reply_text("No husbando found with the specified tags.")
  
  except Exception as e:
    print(e)
    await message.reply_text("An internal error occurred!")
