from pyrogram import filters
from pyrogram.types import Message

from Devine import app
from Devine.utils.database import get_loop, set_loop
from Devine.utils.decorators import AdminRightsCheck
from Devine.utils.inline import close_markup
from config import filter as BANNED_USERS 

prefixes = ["/", "!", "."]
command_filters = filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS

@app.on_message(filters.group & ~BANNED_USERS & (filters.command(["loop", "cloop"]) | filters.regex(f"^[{'|'.join(prefixes)}]loop$|^[{'|'.join(prefixes)}]cloop$")))
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    usage = "ᴜsᴀɢᴇ : /loop ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ."

    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip()
    if state.isnumeric():
        state = int(state)
        if 1 <= state <= 10:
            got = await get_loop(chat_id)
            if got != 0:
                state = got + state
            if state > 10:
                state = 10
            await set_loop(chat_id, state)
            return await message.reply_text(
                text=f"ʟᴏᴏᴘ ᴄᴏᴜɴᴛ sᴇᴛ ᴛᴏ {state} ʙʏ {message.from_user.mention}."
            )
        else:
            return await message.reply_text(usage)

    elif state.lower() in ["enable", "en"]:
        await set_loop(chat_id, 1000000)
        return await message.reply_text(
            text=f"ʟᴏᴏᴘ ᴇɴᴀʙʟᴇᴅ ʙʏ {message.from_user.mention}."
        )

    elif state.lower() in ["disable", "dis"]:
        got = await get_loop(chat_id)
        if got > 0:  # Only disable if looping is enabled
            await set_loop(chat_id, 0)
            return await message.reply_text(
                f"ʟᴏᴏᴘ ʜᴀs ʙᴇᴇɴ ᴅɪsᴀʙʟᴇᴅ ʙʏ {message.from_user.mention}."
            )
        else:
            return await message.reply_text("ʟᴏᴏᴘ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")

    else:
        return await message.reply_text(usage)
