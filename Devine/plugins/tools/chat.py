import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from Devine import app as devine 
from pyrogram.errors import RPCError
from pyrogram.enums import ParseMode

LOG_GROUP = -1001997798206

@devine.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = None
    try:
        link = await devine.export_chat_invite_link(chat.id)
    except RPCError as e:
        link = f"Failed to fetch"  # Handle the error gracefully

    for member in message.new_chat_members:
        if member.id == devine.id:
            count = await devine.get_chat_members_count(chat.id)
            adder = message.from_user
            adder_username = f"@{adder.username}" if adder.username else "No username"
            adder_id = adder.id
            msg = (
                f"#NEW_GROUP\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ : <code>{chat.title}</code>\n"
                f"ᴄʜᴀᴛ ɪᴅ : <code>{chat.id}</code>\n"
                f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : @{chat.username}\n"
                f"ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs : {count}\n\n"
                f"ᴀᴅᴅᴇᴅ ʙʏ : {adder.mention}\n"
                f"ᴀᴅᴅᴇʀ ᴜsᴇʀɴᴀᴍᴇ : {adder_username}\n"
                f"ᴀᴅᴅᴇʀ ɪᴅ : <code>{adder_id}</code>\n\n"
                f"ᴄʜᴀᴛ ʟɪɴᴋ : <pre>{link}</pre>\n"
            )
            await devine.send_message(LOG_GROUP, text=msg, parse_mode=ParseMode.HTML)
