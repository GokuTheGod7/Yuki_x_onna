from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from datetime import datetime
from Devine import app 
import requests

@app.on_message(filters.command(["write", "!write", ".write"]))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = message.text.split(None, 1)[1]

    # Send an immediate "writing" response without animation
    m = await message.reply_text("<b>ᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...</b>")

    # Send the text to the writing API and get the resulting image URL
    write_url = f"https://apis.xditya.me/write?text={text}"
    response = requests.get(write_url)

    if response.status_code == 200:
        write_image_url = response.url

        # Prepare a success message
        text = f"""
<b>sᴜᴄᴇssғᴜʟʟʏ ᴛᴇxᴛ ᴡʀɪᴛᴛᴇɴ, 🫧</b>

<b>• ᴡʀɪᴛᴛᴇɴ ʙʏ ⌯ </b>{app.mention}
<b>• ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ⌯ </b>{message.from_user.mention}
"""
        await m.delete()  # Remove the temporary "writing" message
        await message.reply_photo(text=text, photo=write_image_url)
    else:
        await m.edit("<b>ᴇʀʀᴏʀ: ᴄᴏᴜʟᴅɴ'ᴛ ᴡʀɪᴛᴇ ᴛᴇxᴛ.</b>")
