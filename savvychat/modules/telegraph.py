from pyrogram import filters
from savvychat import savvychat
from telegraph import upload_file

@savvychat.on_message(filters.command(["tgm", "telegraph"]))
async def telegram_upload(_, message):
  reply = message.reply_to_message

  if not reply:
    await message.reply_text("Reply to a media file")
    return

  try:
    pending_message = await message.reply("Uploading to Telegraph...")
    file_path = await reply.download()

    try:
      telegraph_urls = upload_file(file_path)
    except Exception as e:
      await pending_message.edit_text(f"Upload failed: {e}")
      return

    telegraph_url = "https://telegra.ph" + telegraph_urls[0]
    await pending_message.edit_text(f"Uploaded successfully!\n\n{telegraph_url}")

  except Exception as e:
    print(e)
    await message.reply_text("An error occurred while uploading!")

@savvychat.on_message(filters.command(["graph", "grf"]))  
async def graph_upload(_, message):

  # Same logic as above using https://graph.org
  
  reply = message.reply_to_message

  if not reply:
    await message.reply_text("Reply to a media file")
    return
   
  try:
    pending_message = await message.reply("Uploading to graph...")
    file_path = await reply.download()

    try:
         graph_urls = upload_file(file_path)
    except Exception as e:
      await pending_message.edit_text(f"Upload failed: {e}")
      return

    graph_url = "https://graph.org" + graph_urls[0]
    await pending_message.edit_text(f"Uploaded successfully!\n\n{graph_url}")

  except Exception as e:
    print(e)
    await message.reply_text("An error occurred while uploading!")
