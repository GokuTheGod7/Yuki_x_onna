import requests
from pyrogram import Client, filters
from Devine import app as Devine
import time
import asyncio
from config import OWNER_ID

IMGBB_API_KEY = "51b914d093ef0a465446f4e071b5f119"
IMGBB_UPLOAD_URL = "https://api.imgbb.com/1/upload"
MAX_FILE_SIZE_MB = 32  
USER_UPLOAD_LIMIT = {}  

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

    try:
        with open(file_path, 'rb') as file:
            response = requests.post(
                IMGBB_UPLOAD_URL,
                data={"key": IMGBB_API_KEY},
                files={"image": file}
            )
    except Exception as e:
        await waiting_message.edit("ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ: " + str(e))
        return

    upload_time = round(time.time() - start_time, 2)

    if response.status_code == 200:
        response_data = response.json()
        file_url = response_data["data"]["url"]

        await waiting_message.edit(f"<b>ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ <a href='{file_url}' target='_blank'>ɪᴍɢʙʙ</a> ɪɴ {upload_time} sᴇᴄᴏɴᴅs.</b>\n\n"
                                   f"<b>ᴄᴏᴘʏ ʟɪɴᴋ : <code>{file_url}</code></b>")
    else:
        await waiting_message.edit("ғᴀɪʟᴇᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ. sᴛᴀᴛᴜs ᴄᴏᴅᴇ: " + str(response.status_code))

async def handle_upload(client, message, target_message):
    user_id = message.from_user.id
    current_time = time.time()
    last_upload_time = USER_UPLOAD_LIMIT.get(user_id, 0)

    if current_time - last_upload_time < 10:
        await message.reply("ʏᴏᴜ ᴀʀᴇ ʙᴇɪɴɢ ʀᴀᴛᴇ-ʟɪᴍɪᴛᴇᴅ. ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 10 sᴇᴄᴏɴᴅs.")
        return

    USER_UPLOAD_LIMIT[user_id] = current_time

    media = target_message.photo or target_message.video
    if not media:
        await message.reply("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ғᴏʀ ᴜᴘʟᴏᴀᴅ.")
        return

    file_size = media.file_size / (1024 * 1024)  # Convert to MB
    if file_size > MAX_FILE_SIZE_MB:
        await message.reply("ғɪʟᴇ sɪᴢᴇ ᴇxᴄᴇᴇᴅs 32 ᴍʙ ʟɪᴍɪᴛ.")
        return

    try:
        file_path = await target_message.download()
        if file_path:
            await upload_file(client, message, file_path)
        else:
            await message.reply("ғᴀɪʟᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ғɪʟᴇ.")
    except Exception as e:
        await message.reply("ᴇʀʀᴏʀ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ғɪʟᴇ: " + str(e))

@Devine.on_message(filters.command(["tgm", "telegraph", "tm"]))
async def upload_command(client, message):
    if message.from_user.is_bot:
        return  

    target_message = message.reply_to_message if message.reply_to_message else message
    media = target_message.photo or target_message.video

    if media:
        await handle_upload(client, message, target_message)
    else:
        await message.reply("sᴇɴᴅ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ғᴏʀ ᴜᴘʟᴏᴀᴅ.")
