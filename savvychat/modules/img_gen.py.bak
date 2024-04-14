import random
import json
import requests
from pyrogram import Client, filters
from savvychat import savvychat as app
from config import segmind_api_key

@app.on_message(filters.command(["gen"], prefixes="/"))
async def generate_image(client, message):
    try:
        if len(message.text.split()) > 1:
            await client.send_chat_action(message.chat.id, 'upload_photo')
            random_seed = random.randint(1, 10000000000000000)
            user_prompt = ' '.join(message.text.split()[1:])
            payload = {
                "prompt": user_prompt,
                "negative_prompt": "(worst quality, low quality, normal quality, lowres, low details, oversaturated, undersaturated, overexposed, underexposed, grayscale, bw, bad photo, bad photography, bad art)++++, (watermark, signature, text font, username, error, logo, words, letters, digits, autograph, trademark, name)+, (blur, blurry, grainy), morbid, ugly, asymmetrical, mutated malformed, mutilated, poorly lit, bad shadow, draft, cropped, out of frame, cut off, censored, jpeg artifacts, out of focus, glitch, duplicate, (airbrushed, cartoon, anime, semi-realistic, cgi, render, blender, digital art, manga, amateur)++, (3D ,3D Game, 3D Game Scene, 3D Character), (bad hands, bad anatomy, bad body, bad face, bad teeth, bad arms, bad legs, deformities)++",
                "scheduler": "dpmpp_2m",
                "num_inference_steps": 25,
                "guidance_scale": 5,
                "samples": 1,
                "seed": random_seed,
                "img_width": 512,
                "img_height": 768,
                "base64": False
            }
            api_url = "https://api.segmind.com/v1/sd1.5-juggernaut"
            headers = {
                "x-api-key": segmind_api_key,  # Assuming segmind_api_key is defined somewhere in your code
                "Content-Type": "application/json"
            }
            response = requests.post(api_url, headers=headers, data=json.dumps(payload))
            model_info = response.headers.get('X-Model')
            caption = (
                f"Model: {model_info}\n"
                f"LoRa's: {response.headers.get('X-LoRas')}\n"
                f"Size: {payload['img_width']}x{payload['img_height']}\n"
                f"Steps: {payload['num_inference_steps']}\n"
                f"Sampler: {payload['scheduler']}\n"
                f"CFG: {payload['guidance_scale']}\n"
                f"Seed: {payload['seed']}"
            )
            await client.send_photo(message.chat.id, response.content, caption=caption, reply_to_message_id=message.message_id)
        else:
            await message.reply("Please provide a prompt after the /gen command. For example, /gen YourPromptHere")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await message.reply(error_message)


