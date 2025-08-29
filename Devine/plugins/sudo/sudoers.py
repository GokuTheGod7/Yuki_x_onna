from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus
from Devine import app
from Devine.misc import SUDOERS
from Devine.utils.database import add_sudo, remove_sudo
from Devine.utils.extraction import extract_user
from config import filter as BANNED_USERS, OWNER_ID, SPECIAL_USER as SPECIAL_USER_ID, DISASTER_LOG as LOG_CHANNEL_ID  

SPECIAL_USERS = {SPECIAL_USER_ID}

async def log_new_sudo_user(user, adder, chat):
    log_message = (
        f"<b>{user.mention} ʜᴀs ʙᴇᴇɴ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀs ᴀ sᴜᴅᴏᴇʀ.\n\n</b>"
        f"<b>ᴜsᴇʀ ᴅᴀᴛᴀ -\n</b>"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ <code>{user.id}</code></b>\n"
        f"<b>ʜᴀɴᴅʟᴇ ⌯ @{user.username if user.username else 'none'}</b>\n\n"
        f"<b>ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʙʏ {adder.mention}</b>\n"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ <code>{adder.id}</code>\n\n"
        f"<b>ᴀʙᴏᴜᴛ ᴄʜᴀᴛ -\n</b>"
        f"<b>ᴅᴇsɪɢɴᴀᴛɪᴏɴ ⌯ {chat.title}\n</b>"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ <code>{chat.id}</b>\n"
        f"<b>ᴄʜᴀᴛ ʜᴀɴᴅʟᴇ ⌯ @{chat.username if chat.username else 'none'}</b>"
    )
    await app.send_message(LOG_CHANNEL_ID, log_message)  

async def log_removed_sudo_user(user, remover, chat):
    log_message = (
        f"<b>ᴀᴄᴄᴇss {user.mention} ʜᴀs ʙᴇᴇɴ ʀᴇᴠᴏᴋᴇᴅ.</b>\n\n"
        f"<b>ᴜsᴇʀ ᴅᴀᴛᴀ -\n</b>"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ <code>{user.id}</code></b>\n"
        f"<b>ʜᴀɴᴅʟᴇ ⌯ @{user.username if user.username else 'none'}</b>\n\n"
        f"<b>ᴀᴄᴄᴇss ʀᴇᴠᴏᴋᴇᴅ ʙʏ {remover.mention}</b>\n"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b><code>{remover.id}</code>\n\n"
        f"<b>ᴀʙᴏᴜᴛ ᴄʜᴀᴛ -\n"
        f"<b>ᴅᴇsɪɢɴᴀᴛɪᴏɴ ⌯ {chat.title}</b>\n"
        f"<b>ɪᴅᴇɴᴛɪғɪᴇʀ ⌯ </b><code>{chat.id}</b>\n"
        f"<b>ᴄʜᴀᴛ ʜᴀɴᴅʟᴇ ⌯ @{chat.username if chat.username else 'none'}</b>"
        )
    await app.send_message(LOG_CHANNEL_ID, log_message)



@app.on_message(filters.command(["addsudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
async def useradd(client, message: Message):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.")

    if user.id == OWNER_ID:
        return await message.reply_text("ᴀʀᴇ ᴜ ᴋɪᴅᴅɪɴɢ ɴᴏᴏʙ ? ʜᴇ ɪs ᴍʏ ᴄʀᴇᴀᴛᴏʀ !")

    if user.id in SUDOERS:
        return await message.reply_text(f"{user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀs ᴀ sᴜᴅᴏ ᴜsᴇʀ.")

    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(f"{user.mention} ʜᴀs ʙᴇᴇɴ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀs ᴀ sᴜᴅᴏᴇʀ.")
        
        await log_new_sudo_user(user, message.from_user, message.chat)
        
    else:
        await message.reply_text("ᴛʜᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴛᴏ ᴀᴅᴅ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ᴡᴀs ᴜɴsᴜᴄᴄᴇssғᴜʟ. ᴘʟᴇᴀsᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴀɢᴀɪɴ.")




@app.on_message(filters.command(["delsudo", "rmsudo", "removerand", "removesudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
async def userdel(client, message: Message):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.")

    if user.id == OWNER_ID:
        return await message.reply_text("ᴀʀᴇ ᴜ ᴋɪᴅᴅɪɴɢ ɴᴏᴏʙ ? ʜᴇ ɪs ᴍʏ ᴄʀᴇᴀᴛᴏʀ !")

    if user.id not in SUDOERS:
        return await message.reply_text(f"{user.mention} ɪs ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ sᴜᴅᴏ.")

    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(f"sᴜᴅᴏ ᴀᴄᴄᴇss ғᴏʀ {user.mention} ʜᴀs ʙᴇᴇɴ ʀᴇᴠᴏᴋᴇᴅ.")
        
        await log_removed_sudo_user(user, message.from_user, message.chat)
        
    else:
        await message.reply_text("ᴛʜᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ᴡᴀs ᴜɴsᴜᴄᴄᴇssғᴜʟ. ᴘʟᴇᴀsᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴀɢᴀɪɴ.")



@app.on_message(filters.command(["sudolist", "sudoers", "specialusers"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    if message.from_user.id != OWNER_ID and message.from_user.id not in SUDOERS:
        return await message.reply_text("ʙʀᴜʜ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ .\nᴠɪsɪᴛ @zenitsu_bot_support")

    text = "<b>👑 ᴅɪsᴀsᴛᴇʀs ᴏғ ᴀɴᴏᴛʜᴇʀ ʟᴇᴠᴇʟ.</b>\n\n"
    text += "<b>๏ ᴍʏ ʟᴏʀᴅ</b>\n"
    user = await client.get_users(OWNER_ID)
    user = user.first_name if not hasattr(user, "mention") else user.mention
    text += f"{user}\n\n"

    text += "<b>🔱 sᴘᴇᴄɪᴀʟ ᴅɪsᴀsᴛᴇʀs</b>\n"
    if isinstance(SPECIAL_USER_ID, list):
        for special_id in SPECIAL_USER_ID:
            try:
                user = await client.get_users(special_id)
                user_name = user.first_name if not hasattr(user, "mention") else user.mention
                text += f"‣ {user_name}\n"
            except Exception:
                text += f"‣ ᴜɴᴀʙʟᴇ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғᴏʀ {special_id}.\n"
    else:
        try:
            user = await client.get_users(SPECIAL_USER_ID)
            user_name = user.first_name if not hasattr(user, "mention") else user.mention
            text += f"‣ {user_name}\n"
        except Exception:
            text += f"‣ ᴜɴᴀʙʟᴇ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғᴏʀ {SPECIAL_USER_ID}.\n"

    text += "\n"

    text += "<b>❄️ sᴜᴅᴏᴇʀs</b>\n"
    if not SUDOERS:
        text += "ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ sᴜᴅᴏᴇʀs ᴄᴜʀʀᴇɴᴛʟʏ."
    else:
        for sudo_id in SUDOERS:
            if sudo_id == OWNER_ID:
                continue
            try:
                user = await client.get_users(sudo_id)
                user_name = user.first_name if not hasattr(user, "mention") else user.mention
                text += f"» {user_name}\n"
            except Exception:
                text += f"» ᴜɴᴀʙʟᴇ ᴛᴏ ғᴇᴛᴄʜ ᴅᴀᴛᴀ ғᴏʀ {sudo_id}.\n"

    await message.reply_text(text)



@app.on_chat_member_updated()
async def welcome_special_users(client, update: ChatMemberUpdated):
    new_chat_member = update.new_chat_member

    if new_chat_member is None:
        return

    if not hasattr(new_chat_member, 'user') or not hasattr(new_chat_member, 'status'):
        return

    if new_chat_member.status == ChatMemberStatus.MEMBER:
        user_id = new_chat_member.user.id
        chat = update.chat

        # Only send a welcome message for specific users
        if user_id == OWNER_ID:
            message = f"🔱 ᴍʏ ʟᴏʀᴅ ɪs ɴᴏᴡ ᴘᴀʀᴛ ᴏғ ᴛʜᴇ ᴄʜᴀᴛ."
        elif user_id in SPECIAL_USERS:
            message = f"🔱 ᴍʏ ʟᴏʀᴅ ɪs ɴᴏᴡ ᴘᴀʀᴛ ᴏғ ᴛʜᴇ ᴄʜᴀᴛ."
        elif user_id in SUDOERS:
            message = f"❄️ ɢʟᴏʙᴀʟ ᴀᴅᴍɪɴ ɪs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ ɴᴏᴡ."
        else:
            return  # Do nothing for other users

        # Send the welcome message
        await client.send_message(chat.id, message)
