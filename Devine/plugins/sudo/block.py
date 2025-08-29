from pyrogram import filters
from pyrogram.types import Message

from Devine import app
from Devine.utils.database import add_gban_user, remove_gban_user
from Devine.utils.extraction import extract_user
from config import filter, OWNER_ID

@app.on_message(filters.command(["block"]) & filters.user(OWNER_ID))
async def useradd(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("You need to specify a user to block.")
    user = await extract_user(message)
    if user.id in filter:
        return await message.reply_text(f"{user.mention} is already blocked.")
    await add_gban_user(user.id)
    filter.add(user.id)
    await message.reply_text(f"{user.mention} has been blocked.")


@app.on_message(filters.command(["unblock"]) & filters.user(OWNER_ID))
async def userdel(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("You need to specify a user to unblock.")
    user = await extract_user(message)
    if user.id not in filter:
        return await message.reply_text(f"{user.mention} is not blocked.")
    await remove_gban_user(user.id)
    filter.remove(user.id)
    await message.reply_text(f"{user.mention} has been unblocked.")


@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & filters.user(OWNER_ID))
async def sudoers_list(client, message: Message):
    if not filter:
        return await message.reply_text("No users are currently blocked.")
    mystic = await message.reply_text("Fetching blocked users...")
    msg = "Blocked users list:\n"
    count = 0
    for users in filter:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text("No users are currently blocked.")
    else:
        return await mystic.edit_text(msg)


# New /leave command for the bot to leave a chat
@app.on_message(filters.command("leave") & filters.user(OWNER_ID))
async def leave_chat(client, message: Message):
    if not message.chat:
        return await message.reply_text("This command can only be used in a group or channel.")
    
    try:
        # Make the bot leave the current chat (group or channel)
        await message.chat.leave()
        await message.reply_text("I have left the chat.")
    except Exception as e:
        await message.reply_text(f"An error occurred while leaving the chat: {e}")
