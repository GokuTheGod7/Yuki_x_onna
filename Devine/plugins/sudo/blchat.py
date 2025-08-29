from pyrogram import filters
from pyrogram.types import Message

from Devine import app
from Devine.utils.database import blacklist_chat, blacklisted_chats, whitelist_chat
from config import OWNER_ID  # Import OWNER_ID from vars


@app.on_message(filters.command(["blchat", "blacklistchat"]) & filters.user(OWNER_ID))
async def blacklist_chat_func(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /blchat [chat_id]")
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text("This chat is already blacklisted.")
    blacklisted = await blacklist_chat(chat_id)
    if blacklisted:
        await message.reply_text("Chat successfully blacklisted.")
    else:
        await message.reply_text("Failed to blacklist the chat.")
    try:
        await app.leave_chat(chat_id)
    except:
        pass


@app.on_message(filters.command(["whitelistchat", "unblacklistchat", "unblchat"]) & filters.user(OWNER_ID))
async def white_funciton(client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage: /whitelistchat [chat_id]")
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("This chat is not blacklisted.")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text("Chat successfully whitelisted.")
    await message.reply_text("Failed to whitelist the chat.")


@app.on_message(filters.command(["blchats", "blacklistedchats"]) & filters.user(OWNER_ID))
async def all_chats(client, message: Message):
    text = "List of blacklisted chats:\n"
    j = 0
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except:
            title = "Private chat"
        j = 1
        text += f"{count}. {title}[<code>{chat_id}</code>]\n"
    if j == 0:
        await message.reply_text("No blacklisted chats.")
    else:
        await message.reply_text(text)
