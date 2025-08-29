import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from Devine import app
from Devine.misc import SUDOERS
from Devine.utils import get_readable_time
from Devine.utils.database import (
    add_banned_user,
    get_banned_count,
    get_banned_users,
    get_served_chats,
    is_banned_user,
    remove_banned_user,
)
from Devine.utils.decorators.language import language
from Devine.utils.extraction import extract_user
from config import BANNED_USERS


SPECIAL_USER_ID = 6338745050
LOG_CHANNEL_ID = -1002116643591

@app.on_message(filters.command(["gban", "globalban"]) & SUDOERS)
@language
async def global_ban(client, message: Message, _):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("<b>ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ ғᴏʀ ɢʟᴏʙᴀʟ ʙᴀɴ.</b>")
    
    user = await extract_user(message)
    reason = " ".join(message.command[2:]) if len(message.command) > 2 else "ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ"
    
    # Check if the user is the special user
    if user.id == SPECIAL_USER_ID:
        return await message.reply_text("<b>ᴋɪᴅ ᴅᴏɴ'ᴛ ᴍᴇss ᴡɪᴛʜ ʜɪᴍ, ʜᴇ's ᴄᴀᴘᴀʙʟᴇ ᴏғ ᴅᴇғᴇᴀᴛɪɴɢ ʏᴏᴜ ɪɴ sᴇᴄᴏɴᴅs.</b>")

    if user.id == message.from_user.id:
        return await message.reply_text("<b>‣ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʟᴏʙᴀʟʟʏ ʙᴀɴ ʏᴏᴜʀsᴇʟғ.</b>")
    elif user.id == app.id:
        return await message.reply_text("<b>‣ ᴡʜʏ sʜᴏᴜʟᴅ ɪ ɢʙᴀɴ ᴍʏsᴇʟғ ?</b>")
    elif user.id in SUDOERS:
        return await message.reply_text("<b>‣ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ᴀ sᴜᴅᴏ ᴜsᴇʀ.</b>")
    
    is_gbanned = await is_banned_user(user.id)
    if is_gbanned:
        return await message.reply_text(_["gban_4"].format(user.mention))
    
    if user.id not in BANNED_USERS:
        BANNED_USERS.add(user.id)
    
    served_chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
    time_expected = get_readable_time(len(served_chats))
    mystic = await message.reply_text(_["gban_5"].format(user.mention, time_expected))
    number_of_chats = 0
    
    for chat_id in served_chats:
        try:
            await app.ban_chat_member(chat_id, user.id)
            number_of_chats += 1
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except:
            continue
    
    await add_banned_user(user.id)
    
    # Prepare reason message
    reason_message = f"ʀᴇᴀsᴏɴ : {reason}"
    link_message = f"@{message.chat.username}" if message.chat.username else "ɴᴏɴᴇ"
    
    await app.send_message(
        LOG_CHANNEL_ID,
        f"<b>ɢʟᴏʙᴀʟʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ\n\n</b>"
        f"<b>ᴏʀɪɢɪɴᴀᴛᴇᴅ ғʀᴏᴍ : {message.chat.title}</b>\n"
        f"<b>• ᴄʜᴀᴛ ʟɪɴᴋ : {link_message} [{message.chat.id}]</b>\n"
        f"<b>• ʙᴀɴɴᴇᴅ ᴜsᴇʀ : {user.mention}</b>\n"
        f"<b>• ʙᴀɴɴᴇᴅ ᴜsᴇʀ ɪᴅ : {user.id}</b>\n"
        f"<b>• ᴀᴅᴍɪɴ : {message.from_user.mention}</b>\n"
        f"<b>• ᴀғғᴇᴄᴛᴇᴅ ᴄʜᴀᴛs : {number_of_chats}</b>\n"
        f"<b>• {reason_message}</b>"
    )
    
    await message.reply_text(
        _["gban_6"].format(
            app.mention,
            message.chat.title,
            message.chat.id,
            user.mention,
            user.id,
            message.from_user.mention,
            number_of_chats,
            reason
        )
    )
    await mystic.delete()


@app.on_message(filters.command(["ungban"]) & SUDOERS)
@language
async def global_un(client, message: Message, _):
    if not message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("<b>ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ ғᴏʀ ɢʟᴏʙᴀʟ ᴜɴʙᴀɴ.</b>")
    
    user = await extract_user(message)
    reason = " ".join(message.command[2:]) if len(message.command) > 2 else "ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ"
    
    is_gbanned = await is_banned_user(user.id)
    if not is_gbanned:
        return await message.reply_text(_["gban_7"].format(user.mention))
    
    if user.id in BANNED_USERS:
        BANNED_USERS.remove(user.id)
    
    served_chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
    time_expected = get_readable_time(len(served_chats))
    mystic = await message.reply_text(_["gban_8"].format(user.mention, time_expected))
    number_of_chats = 0
    
    for chat_id in served_chats:
        try:
            await app.unban_chat_member(chat_id, user.id)
            number_of_chats += 1
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except:
            continue
    
    await remove_banned_user(user.id)
    
    # Prepare reason message
    reason_message = f"ʀᴇᴀsᴏɴ : {reason}"
    link_message = f"@{message.chat.username}" if message.chat.username else "ɴᴏɴᴇ"
    
    # Send a log message
    await app.send_message(
        LOG_CHANNEL_ID,
        f"<b>ʀᴇᴠᴏᴋᴇᴅ ɢʟᴏʙᴀʟ ᴘʀᴏʜɪʙɪᴛɪᴏɴ\n\n</b>"
        f"<b>ᴏʀɪɢɪɴᴀᴛᴇᴅ ғʀᴏᴍ : {message.chat.title}</b>\n"
        f"<b>• ᴄʜᴀᴛ ʟɪɴᴋ : {link_message} [{message.chat.id}]</b>\n"
        f"<b>• ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ : {user.mention}</b>\n"
        f"<b>• ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ ɪᴅ : {user.id}</b>\n"
        f"<b>• ᴀᴅᴍɪɴ : {message.from_user.mention}</b>\n"
        f"<b>• ᴀғғᴇᴄᴛᴇᴅ ᴄʜᴀᴛs : {number_of_chats}</b>\n"
        f"<b>• {reason_message}</b>"
    )
    
    await message.reply_text(_["gban_9"].format(user.mention, number_of_chats, reason))
    await mystic.delete()


@app.on_message(filters.command(["gbannedusers", "gbanlist"]) & SUDOERS)
@language
async def gbanned_list(client, message: Message, _):
    counts = await get_banned_count()
    if counts == 0:
        return await message.reply_text("<b>ɴᴏ ᴜsᴇʀs ᴀʀᴇ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ.</b>")
    
    mystic = await message.reply_text("<b>ɢᴇᴛᴛɪɴɢ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs ʟɪsᴛ...</b>")
    msg = "<b>ɢʟᴏʙᴀʟʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ ᴜsᴇʀs:</b>\n\n"
    count = 0
    users = await get_banned_users()
    
    for user_id in users:
        count += 1
        try:
            user = await app.get_users(user_id)
            user_name = user.first_name if not user.mention else user.mention
            msg += f"{user.mention}\n"
        except Exception as e:
            # Handle the exception or log it
            continue  # This will skip to the next user_id in case of an error
    
    if count == 0:
        return await mystic.edit_text("<b>ɴᴏ ᴜsᴇʀs ᴀʀᴇ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ.</b>")
    else:
        return await mystic.edit_text(msg)


@app.on_message(filters.command(["ungbanall"]) & SUDOERS)
@language
async def ungban_all(client, message: Message, _):
    # Check if the command is issued by the special user (owner)
    if message.from_user.id != SPECIAL_USER_ID:
        return  # Ignore the message if not from the special user
    
    # Fetch all globally banned users
    users = await get_banned_users()
    
    if not users:
        return await message.reply_text("<b>ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs ᴛᴏ ᴜɴʙᴀɴ.</b>")
    
    served_chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
    time_expected = get_readable_time(len(served_chats))
    mystic = await message.reply_text(_["gban_8"].format("all banned users", time_expected))
    number_of_chats = 0
    number_of_users_unbanned = 0
    
    for user_id in users:
        if user_id == SPECIAL_USER_ID: 
            continue
        for chat_id in served_chats:
            try:
                await app.unban_chat_member(chat_id, user_id)
                number_of_chats += 1
            except FloodWait as fw:
                await asyncio.sleep(int(fw.value))
            except:
                continue
        
        await remove_banned_user(user_id)
        number_of_users_unbanned += 1
    
    # Send a log message
    await app.send_message(
        LOG_CHANNEL_ID,
        f"<b>ʀᴇᴠᴏᴋᴇᴅ ᴀʟʟ ɢʟᴏʙᴀʟ ᴘʀᴏʜɪʙɪᴛɪᴏɴs\n\n</b>"
        f"<b>ᴏʀɪɢɪɴᴀᴛᴇᴅ ғʀᴏᴍ : {message.chat.title}</b>\n"
        f"<b>• ᴀʟʟ ɢʟᴏʙᴀʟʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ ᴜsᴇʀs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴʙᴀɴɴᴇᴅ.</b>\n"
        f"<b>• ᴜsᴇʀs ᵁɴʙᴀɴɴᴇᴅ : {number_of_users_unbanned}</b>\n"
        f"<b>• ᴀᴅᴍɪɴ : {message.from_user.mention}</b>\n"
        f"<b>• ᴀғғᴇᴄᴛᴇᴅ ᴄʜᴀᴛs : {number_of_chats}</b>"
    )
    
    await message.reply_text(f"<b>ᴀʟʟ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴʙᴀɴɴᴇᴅ ɪɴ {number_of_chats} ᴄʜᴀᴛs.</b>")
    await mystic.delete()
