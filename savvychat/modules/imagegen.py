import os
import json
import io
from dotenv import load_dotenv
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from savvychat.modules.helpers.inline import SETTINGS
from savvychat.modules.callbacks import (
    help_callback,
    settings_callback,
    choose_model_callback,
    selected_model_callback,
    change_steps_callback,
    step_incre_callback,
    step_decre_callback,
    change_image_count_callback,
    image_incre_callback,
    image_decre_callback,
    back2settings_callback,
    
)
from savvychat.modules.helpers.models import MODELS
from diffusers import StableDiffusionPipeline
import torch
from savvychat import savvychat as app



DEFAULT_SETTINGS = {
    "model": "digiplay/Juggernaut_final",  # change default model in env
    "steps": 100,
    "seed": -1,
    "image_count": 1,
}


pipe = None


@app.on_callback_query()
async def cb_data(bot, update):
    chat_id = update.message.chat.id
    settings_file_path = f"{chat_id}-settings.json"

    if not os.path.exists(settings_file_path):
        with open(settings_file_path, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)

    with open(settings_file_path, "r") as f:
        settings = json.load(f)

    if update.data == "cbhelp":
        await help_callback(update)
    elif update.data == "cbabout":
        await about_callback(update)
    elif update.data == "cbsettings":
        await settings_callback(update, settings)
    elif update.data == "choose_model":
        await choose_model_callback(update, settings)
    elif update.data.startswith("select_model_"):
        index = int(update.data.split("_")[2])
        selected_model = MODELS[index]
        await selected_model_callback(
            update, selected_model, settings, settings_file_path
        )
    elif update.data == "change_steps":
        await change_steps_callback(update, settings)
    elif update.data.startswith("+steps"):
        await step_incre_callback(
            update,
            settings,
            settings_file_path,
        )
    elif update.data == "change_image_count":
        await change_image_count_callback(update, settings)
    elif update.data.startswith("+image"):
        await image_incre_callback(update, settings, settings_file_path)
    elif update.data.startswith("-image"):
        await image_decre_callback(update, settings, settings_file_path)
    elif update.data.startswith("-steps"):
        await step_decre_callback(update, settings, settings_file_path)
    elif update.data.startswith("cb_back_settings"):
        await back2settings_callback(update, settings)
    else:
        await start_callback(update)




@app.on_message(filters.command(["generate"]) & filters.private)
async def generate(bot, update: Message):
    if update.reply_to_message:
        chat_id = update.chat.id
        settings_file_path = f"{chat_id}-settings.json"
        if not os.path.exists(settings_file_path):
            with open(settings_file_path, "w") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4)
        text = await update.reply_text("Loading settings...", quote=True)
        prompt = update.reply_to_message.text
        with open(f"{chat_id}-settings.json") as f:
            settings = json.load(f)
            await text.edit("Settings Loaded...")
            await text.edit(f'Downloading...\n{settings.get("model")}')
            model_loaded = await load_model(settings.get("model"), update)
            if not model_loaded:
                await update.reply_text("Failed to load the model.")
                return
            else:
                await text.edit("Generating Image...")
            try:
                images = await generate_image(
                    update,
                    prompt,
                    settings.get("steps"),
                    settings.get("seed"),
                    settings.get("image_count"),
                )
                await text.edit(f'Uploading {settings.get("image_count")} Image ....')
                for image in images:
                    await update.reply_photo(image, reply_markup=GITHUB_BUTTON)
                await text.delete()
            except Exception as e:
                await text.delete()
                text = f"Failed to generate Image \nCreate an issue here"
                error = f"ERROR: {(str(e))}"
                
                
                await update.reply_text(
                    text,
                    disable_web_page_preview=True,
                    quote=True,
                    
                )
    else:
        await update.reply_text(
            text="Reply /generate to a prompt",
            disable_web_page_preview=True,
            quote=True,
        )


async def load_model(model, update):
    global pipe
    try:
        pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float16)
        pipe = pipe.to("cuda")
        return True
    except Exception as e:
        text = f"Failed to download Model \nCreate an issue here"
        error = f"ERROR: {(str(e))}"
        
        await update.reply_text(
            text, disable_web_page_preview=True, quote=True, 
        )
        return False


async def generate_image(update, prompt, steps, seed, count):
    global pipe
    steps = steps
    if seed == -1:
        torch.manual_seed(torch.seed())
    else:
        torch.manual_seed(seed)
    pipe = pipe.to("cuda")

    # def custom_callback(step, timestep, latents):
    #     text = f'Step: {step}, Timestep: {timestep}, Latents: {latents}'
    #     print("🤖",  text)
    #     # await update.reply_text(text, disable_web_page_preview=True, quote=True,)

    images = pipe(prompt, num_inference_steps=steps, num_images_per_prompt=count).images
    image_streams = []
    for image in images:
        image_stream = io.BytesIO()
        image.save(image_stream, format="PNG")
        image_stream.seek(0)
        image_streams.append(image_stream)
    return image_streams


@app.on_message(filters.command(["settings"]) & filters.private)
async def settings(bot, update: Message):
    chat_id = update.chat.id
    settings_file_path = f"{chat_id}-settings.json"
    if not os.path.exists(settings_file_path):
        with open(settings_file_path, "w") as f:
            json.dump(DEFAULT_SETTINGS, f, indent=4)
            text = "Settings file created. Please use the command again to access the settings."
    else:
        with open(settings_file_path, "r") as f:
            settings = json.load(f)
            model = settings.get("model")
            steps = settings.get("steps")
            text = f"Current Settings:\n🤖 Model: {model}\n🔄 Steps: {steps}"
            await update.reply_text(text=text, reply_markup=SETTINGS, quote=True)


