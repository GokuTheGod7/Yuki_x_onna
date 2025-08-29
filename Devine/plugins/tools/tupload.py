import requests
from pyrogram import Client, filters
from Devine import app as Devine
import time
import asyncio
from config import OWNER_ID

# Cloudinary credentials
CLOUDINARY_UPLOAD_URL = "https://api.cloudinary.com/v1_1/your_cloud_name/upload"
CLOUD_NAME = "Untitled"  # Replace with your Cloudinary Cloud Name
API_KEY = "769593722143466"
API_SECRET = "DztGFORQqYfBoxCdawh0g5jBRCg"
MAX_FILE_SIZE_MB = 32  # Cloudinary allows large file uploads depending on your plan
USER_UPLOAD_LIMIT = {}  # Dictionary to track user upload times

async def send_temp_message(message, text):
    reply = await message.reply(text)
    
    for i in range(3):
        await asyncio.sleep(0.3)  
        updated_text = text + '.' * (i + 1)  
        await reply.edit(updated_text)  
        
    return reply  

async def upload_file(client, message, file_path):
    waiting_message = await send_temp_message(message, "ᴡᴀɪᴛ")
    
    start_time = time.time()

    with open(file_path, 'rb') as file:
        # Prepare file upload to Cloudinary
        files = {
            "file": file,
            "api_key": API_KEY,
            "timestamp": int(time.time()),
            "signature": API_SECRET  # You should generate a signature for security purposes
        }

        response = requests.post(CLOUDINARY_UPLOAD_URL, data=files)

    upload_time = round(time.time() - start_time, 2)

    if response.status_code == 200:
        response_data = response.json()
        file_url = response_data["secure_url"]  # Cloudinary URL for the uploaded file

        await waiting_message.edit(f"<b>ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ <a href='{file_url}' target='_blank'>Cloudinary</a> ɪɴ {upload_time} sᴇᴄᴏɴᴅs.</b>\n\n"
                                   f"<b>ᴄᴏᴘʏ ʟɪɴᴋ : <code>{file_url}</code></b> ")
    else:
        await waiting_message.edit("<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ.</b>")

async def handle_upload(client, message, target_message):
    # Check if user is in upload limit
    user_id = message.from_user.id
    current_time = time.time()
    last_upload_time = USER_UPLOAD_LIMIT.get(user_id, 0)

    # Allow only if 10 seconds have passed since the last upload
    if current_time - last_upload_time < 10:
        await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ʙᴇɪɴɢ ʀᴀᴛᴇ-ʟɪᴍɪᴛᴇᴅ. ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 10 sᴇᴄᴏɴᴅs.</b>")
        return

    # Update last upload time
    USER_UPLOAD_LIMIT[user_id] = current_time

    # Upload media
    file_size = (target_message.photo or target_message.video).file_size / (1024 * 1024)  # Convert to MB
    if file_size > MAX_FILE_SIZE_MB:
        await message.reply("<b>ғɪʟᴇ sɪᴢᴇ ᴇxᴄᴇᴇᴅs 32 ᴍʙ ʟɪᴍɪᴛ.</b>")
    else:
        file_path = await target_message.download()
        await upload_file(client, message, file_path)

@Devine.on_message(filters.command("xtgm"))
async def upload_command(client, message):
    if message.from_user.is_bot:
        return  # Ignore messages from bots

    # Check if there's media in the message itself or in a reply
    target_message = message.reply_to_message if message.reply_to_message else message
    media = target_message.photo or target_message.video

    if media:
        await handle_upload(client, message, target_message)
    else:
        await message.reply("<b>sᴇɴᴅ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ғᴏʀ ᴜᴘʟᴏᴀᴅ.</b>")
