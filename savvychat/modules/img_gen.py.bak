import torch
from transformers import CLIPProcessor, CLIPModel, DALLEProcessor, DALLEModel
from PIL import Image
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from savvychat import savvychat as app

# Load the CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load the DALL-E model and processor
dalle_model = DALLEModel.from_pretrained("openai/dall-e")
dalle_processor = DALLEProcessor.from_pretrained("openai/dall-e")

# Function to generate an image based on a prompt
def generate_image(prompt):
    # Encode the prompt using CLIP
    inputs = clip_processor(text=prompt, return_tensors="pt", padding="max_length", max_length=77, truncation=True)
    with torch.no_grad():
        image_features = clip_model.get_image_features(inputs.pixel_values)

    # Generate the image using DALL-E
    with torch.no_grad():
        image = dalle_model.generate_images(
            text=inputs["input_ids"],
            return_tensors=True,
            output_dir="./output_images",
        )

    # Save the generated image
    image_path = "./output_images/generated_image.png"
    image[0].permute(1, 2, 0).cpu().numpy()
    image[0].save(image_path)
    
    return image_path

# Command handler for the /generate_image command
@app.on_message(filters.command("generate_image"))
async def generate_image_command(_, message):
    # Get the prompt from the command
    prompt = " ".join(message.command[1:])
    
    # Generate the image
    image_path = generate_image(prompt)
    
    # Send the image back to the user
    with open(image_path, "rb") as f:
        await message.reply_photo(photo=f)
