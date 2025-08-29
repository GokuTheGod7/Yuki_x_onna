from Devine import app
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.errors import UsernameNotOccupied

@app.on_message(filters.command(["id", "identifier"], prefixes=["/", "!", ".", "+", "?"]))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    reply = message.reply_to_message
    text = ""

    if not reply and len(message.command) == 1:
        text = f"ᴛʜɪs ᴄʜᴀᴛ's ɪᴅ ɪs : `<code>{chat.id}</code>`\n"

    elif reply and not reply.forward_from_chat and not reply.sender_chat:
        user_id = reply.from_user.id
        first_name = reply.from_user.first_name
        text = f"ᴜsᴇʀ {first_name}'s ɪᴅ ɪs `<code>{user_id}</code>`.\n"

    elif reply and reply.forward_from_chat:
        user_id = reply.from_user.id
        first_name = reply.from_user.first_name
        channel_id = reply.forward_from_chat.id
        channel_title = reply.forward_from_chat.title
        text = (
            f"ᴜsᴇʀ {first_name}'s ɪᴅ ɪs `<code>{user_id}</code>`.\n"
            f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {channel_title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `<code>{channel_id}</code>`.\n\n"
        )

    elif reply and reply.sender_chat:
        chat_id = reply.sender_chat.id
        chat_title = reply.sender_chat.title
        text = f"ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, {chat_title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `<code>{chat_id}</code>`."

    # Check if a username is provided
    elif len(message.command) == 2 and message.command[1].startswith('@'):
        username = message.command[1][1:]  # Remove the '@' symbol
        try:
            user = await client.get_users(username)
            text = f"ᴜsᴇʀ {user.first_name}'s ɪᴅ ɪs `<code>{user.id}</code>`."
        except UsernameNotOccupied:
            text = "ᴛʜᴇ ᴜsᴇʀɴᴀᴍᴇ ɪs ɴᴏᴛ ᴏᴄᴄᴜᴘɪᴇᴅ."

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )
