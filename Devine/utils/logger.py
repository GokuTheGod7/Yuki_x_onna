from pyrogram.enums import ParseMode
from Devine import app
from Devine.utils.database import is_on_off
from config import LOGGER_ID

async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>ᴍᴜsɪᴄ ʀᴇᴄᴏʀᴅs</b>

<b>• ɪɴǫᴜɪʀʏ ⌯ </b> {message.text.split(None, 1)[1]}
<b>• sᴏᴜʀᴄᴇ ⌯ </b> {streamtype}

<b>ᴀʙᴏᴜᴛ ᴄʜᴀᴛ - </b> 

<b>↬ ᴅᴇsɪɢɴᴀᴛɪᴏɴ ⌯ </b> {message.chat.title}
<b>↬ ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b> <code>{message.chat.id}</code>
<b>↬ ᴄʜᴀᴛ ʜᴀɴᴅʟᴇ ⌯ </b> @{message.chat.username}

<b>ᴜsᴇʀ ᴅᴀᴛᴀ - </b>

<b>↬ ɴᴀᴍᴇ ⌯ </b> {message.from_user.mention}
<b>↬ ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b> <code>{message.from_user.id}</code>
<b>↬ ʜᴀɴᴅʟᴇ ⌯ </b> @{message.from_user.username}"""

        # Send log to the primary log channel
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(f"Failed to send log to LOGGER_ID: {e}")

        
