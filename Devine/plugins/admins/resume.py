from pyrogram import filters
from pyrogram.types import Message

from Devine import app
from Devine.core.call import devine
from Devine.utils.database import is_music_playing, music_on
from Devine.utils.decorators import AdminRightsCheck
from Devine.utils.inline import close_markup
from config import filter


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~filter)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await devine.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
