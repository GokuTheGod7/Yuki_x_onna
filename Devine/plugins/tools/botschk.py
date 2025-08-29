import asyncio
from datetime import datetime
from pyrogram import filters
from Devine import app as devine
from Devine.core.userbot import Userbot

OWNER_ID = {5268691896}
userbot = Userbot()

BOT_LIST = [
    "",
    "zenitsu_music_xbot",
    "",
    "",
    "",
    ""
]

last_checked_time = None  # Track the last checked time

@devine.on_message(filters.command(["chkalive", "check"]))
async def check_bots_command(client, message):
    global last_checked_time

    if message.from_user.id not in OWNER_ID:
        return await message.reply_text(
            "ᴋɪᴅ ɢʀᴏᴡ ᴜᴘ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴄᴀᴘᴀʙʟᴇ ᴛᴏ ᴅᴏ ᴛʜɪs."
        )

    # Start userbot if not already connected
    if not userbot.one.is_connected:
        await userbot.one.start()

    processing_msg = await message.reply_text(
    text="ᴄʜᴇᴄᴋɪɴɢ ʙᴏᴛs sᴛᴀᴛs... <a href='https://files.catbox.moe/7mtx1x.jpg'></a>"
        )
    start_time = datetime.now()
    response = "ʙᴏᴛs sᴛᴀᴛᴜs ᴅᴇᴀᴅ ᴏʀ ᴀʟɪᴠᴇ ᴄʜᴇᴄᴋᴇʀ\n\n"

    for bot_username in BOT_LIST:
        try:
            bot = await userbot.one.get_users(bot_username)

            await asyncio.sleep(0.5)
            await userbot.one.send_message(bot.id, "/start")

            await asyncio.sleep(0.7)
            async for bot_message in userbot.one.get_chat_history(bot.id, limit=1):
                status = "ᴏɴʟɪɴᴇ" if bot_message.from_user.id == bot.id else "ᴏғғʟɪɴᴇ"
                response += f"• {bot.mention}\n- sᴛᴀᴛᴜs : {status}\n\n"
                break
        except Exception as e:
            response += f"• {bot_username}\n- sᴛᴀᴛᴜs : ᴇʀʀᴏʀ (Reason: {str(e)})\n\n"

    last_checked_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
    await processing_msg.edit_text(
    f"{response} ʟᴀsᴛ ᴄʜᴇᴄᴋ: {last_checked_time}"
    )

    # Stop the userbot connection if it was started in this function
    if userbot.one.is_connected:
        await userbot.one.stop()
