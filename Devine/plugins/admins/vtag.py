from Devine import app 
import asyncio
import random
from Devine.misc import SUDOERS 
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [
    "<b>ʜᴇʏ ᴇᴠᴇʀʏᴏɴᴇ, ᴠᴄ ᴄʜᴀʟᴏ ᴇᴠᴇʀʏᴏɴᴇ, ɪᴛ'ᴠᴇ ʙᴇᴇɴ ᴀ ᴡʜɪʟᴇ 🤩</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ɢᴜʏs, ᴠᴄ ᴄʜᴀʟᴏ ᴛʜᴇʀᴇ'ʀᴇ ɴᴇᴡ ᴄᴏᴍᴇᴅɪᴇs ɪɴ ᴛᴏᴡɴ!</b>",
    "<b>ʏᴏᴏ ᴄᴏᴍᴇ ᴏɴ ɢᴜʏs! ᴠᴄ ᴄʜᴀʟᴏ, ᴡᴇ ɴᴇᴇᴅ ᴛʏᴘɪᴄᴀʟ ᴄʜᴀᴛᴇʀ ɪɴ ᴠᴏɪᴄᴇ!</b>",
    "<b>ʜᴇʏ ᴀʟʟ! ᴠᴄ ᴄʜᴀʟᴏ, ᴅᴏɴ'ᴛ ᴍɪss ᴏᴜᴛ!</b>",
    "<b>ᴡʜᴀᴛ'ᴄʜᴇᴄᴋ ɢᴜʏs! ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ᴄʜᴀʟᴏ ɪᴛ'ᴠᴇ ɢᴏᴏᴅ!</b>",
    "<b>ʜᴇʏ ɴᴏᴏʙs! ᴠᴄ ᴄʜᴀʟᴏ ᴡᴇ'ʀᴇ ᴘʟᴀʏɪɴɢ ɢᴀᴍᴇs</b>",
    "<b>ʜᴇʏ ᴠᴄ ᴅᴇᴇᴘ! ᴄᴏᴍᴇ ᴏɴ, ᴇᴠᴇʀʏᴏɴᴇ ᴍᴀᴋᴇs ᴛʜᴇ ᴄʜᴀᴛ ᴛᴇᴀʀ ᴄᴏᴍᴇ!</b>",
    "<b>ʜᴇʏ ᴘᴀʀᴛʏ ᴘᴇᴏᴘʟᴇ! ᴠᴄ ᴄʜᴀʟᴏ, ᴍᴜᴄʜ ᴏᴜᴛ ᴛᴏ ᴇᴛʀᴇ ᴍᴏᴏʀᴇ ᴠɪᴄᴛᴏʀᴋ 🥳</b>",
    "<b>ᴏʏᴇ! ᴅᴏɴ'ᴛ ᴍɪss ᴛʜɪs ᴇᴠᴇɴᴛ, ᴄᴏᴍᴇ ᴄʜᴀʟᴏ!</b>",
    "<b>ᴍɪᴇᴇ ᴠᴄ ᴛɪᴍᴇ, ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ!</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ! ᴠᴄ ᴡᴇ ɴᴇᴇᴅ ᴇᴀᴄʜ ᴏᴛʜᴇʀ'ꜱ ᴠᴏɪᴄᴇ ᴄᴏᴍᴇ ᴡɪᴛʜ ᴇᴠᴇʀʏ ᴛʜɪɴɢ!</b>",
    "<b>ʜᴇʏ ʙᴀʙʏ ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ? ᴠᴄ ᴄʜᴀʟᴏ</b>",
    "<b>ᴄᴏᴍᴇ ᴛᴏᴇ ᴠᴄ! ᴡᴇ'ʀᴇ ᴄᴏᴏʟ ɪɴ ᴠᴏɪᴄᴇ</b>",
    "<b>ᴅᴏɴ'ᴛ ᴍɪss ᴏᴜᴛ, ᴄᴏᴍᴇ ᴏɴ ᴠᴄ!</b>",
    "<b>ʜᴇʏ ɴᴏᴏʙs, ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ᴄʜᴀʟᴏ 🧑‍💻</b>",
    "<b>ᴠᴄ ᴄʜᴀʟᴏ, ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ!</b>",
    "<b>ᴀᴜʀ ᴛʀʏ ᴠᴄ ᴄʜᴀʟᴏ ɪᴛ'ᴠᴇ ʙᴇᴇɴ ᴀɴ ᴇᴠᴇɴᴛ! 🥳</b>",
    "<b>ᴘʟᴇᴀsᴇ ᴄᴏᴍᴇ ᴠᴄ, ᴡᴇ'ʀᴇ ᴛʀʏɪɴɢ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ ᴍᴏʀᴇ ғᴜɴ!!</b>",
    "<b>ᴠᴄ ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ ᴏɴ! ᴏɴʟɪɴᴇ ᴀʟʟ ᴅᴀʏ!</b>",
    "<b>ᴄᴏᴍᴇ ᴛᴏ ᴠᴄ ᴄʜᴀʟᴏ, ɪᴛ'ᴠᴇ ʙᴇᴇɴ ᴀɴ ᴀᴠᴀɴᴛᴀɢᴇ 🥳</b>",
    "<b>ᴍᴀʏ ʏᴏᴜ ᴄᴏᴍᴇ ᴠᴄ!</b>",
    "<b>ᴠᴄ ᴛᴇᴀᴍ ᴏᴜᴛ ᴄᴏᴍᴇ ᴏɴ!</b>",
    "<b>ʏᴏᴏ ᴠᴄ ᴘᴀʀᴛʏ ᴄᴏᴍᴇ ᴏɴ ᴏᴏ </b>",
    "<b>ᴀʟʟ ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ ᴏɴ!</b>",
    "<b>ᴡʜᴀᴛ' ᴍᴀᴋᴇ ᴄᴏᴍᴇ ᴍᴏʀᴇ ғᴜɴ. ᴠᴄ ᴄʜᴀʟᴏ</b>",
    "<b>ᴄᴏᴍᴇ ᴄʜᴀʟᴏ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ᴠɪᴄᴛᴏʀʏ ᴏᴜᴛ!! 🥳🎉</b>",
    "<b>ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ ᴏɴ ᴠᴄ, ᴡᴇ'ʀᴇ ᴘʟᴀʏɪɴɢ ᴀɴᴏᴛʜᴇʀ ʙᴇᴀᴜᴛɪғᴜʟ ɢᴀᴍᴇ!</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ᴄʜᴀʟᴏ, ᴏᴏ ɪɴᴇʀ ɪɴ ᴠᴏᴛᴇ ᴍᴇɴ ᴀᴇᴠᴇʀʏᴏɴᴇ 🥳</b>",
    "<b>ʜᴇʏ ᴇᴠᴇʀʏᴏɴᴇ! ᴄᴏᴍᴇ ᴠᴄ ᴄʜᴀʟᴏ ᴇᴠᴇʀʏ ᴏɴᴇ!</b>",
    "<b>ᴏʏᴇ! ᴄᴏᴍᴇ ᴠᴄ, ᴏᴜᴛ ᴏғ ᴄᴏᴍᴇᴅɪᴇ ᴠɪᴄᴛᴏʀʏ 🥳</b>",
    "<b>ᴠᴄ ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ ᴇʀᴇ ᴇᴠᴇʀʏ ᴛᴇᴀᴍ ᴄᴏᴍᴇ!</b>",
    "<b>ᴘʟᴇᴀsᴇ ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ ᴠᴄ ᴡɪᴛʜ ᴍᴇ ɪᴛ'ᴠᴇ ʙᴇᴇɴ ᴀɴ ᴇᴠᴇɴᴛ ᴀᴍᴀᴢɪɴɢ!</b>",
    "<b>ᴠᴄ ᴄᴏᴍᴇ ᴏɴ, ᴇᴠᴇʀʏᴏɴᴇ ᴛʜᴇʀᴇ ᴀʀᴇ ᴇᴠᴇʀʏ ɢᴀᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ 🥳</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ! ᴠᴄ ᴛɪᴍᴇ ᴡɪᴛʜ ᴘᴀʀᴛʏ</b>",
    "<b>ᴄᴏᴍᴇ ᴠᴄ ɢᴜʏs, ᴡᴇ ᴘʟᴀʏ ᴇᴠᴇʀʏᴏɴᴇ ᴠᴄ ᴇᴠᴇʀʏᴛʜɪɴɢ</b>",
    "<b>ᴏᴏ ᴄᴏᴍᴇ ᴠᴄ! ᴏᴇᴠᴇʀʏ ᴍᴏᴛᴏᴏ ᴇᴠᴇʀʏᴏɴᴇ 🥳</b>",
    "<b>ʜᴇʏ ᴠᴄ ᴠɪᴏᴋᴇ ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏ ᴏɴᴇ 🥳</b>",
    "<b>ᴠᴄ ᴄʜᴀʟᴏ ᴇᴠᴇʀʏ ᴘᴇʀsᴏɴ! ᴇᴠᴇʀʏᴏɴᴇ ᴄᴏᴍᴇ ᴏɴ!</b>",
    "<b>ᴡᴇ ʜᴀᴠᴇ ᴀ ɪɴᴇᴄᴏᴍᴇ ᴠᴄ ᴄᴏᴍᴇ ᴏɴ, ᴄᴏᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ ᴡᴇᴛ ᴍᴏᴏʀᴇ!</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴠᴄ, ᴇᴠᴇʀʏᴏɴᴇ ᴇᴠᴇʀʏ ᴠᴇʀᴍᴇ ᴄᴏᴍᴇ!</b>",
    "<b>ᴠᴄ ᴄʜᴀʟᴏ ᴇᴠᴇʀʏ ᴏɴᴇ ɴᴏᴡ, ᴇᴠᴇʀʏ ᴇᴠᴇʀ ᴘʟᴇᴀsᴇ!</b>",
    "<b>ᴏᴇᴠᴇʀʏ ᴇᴠᴇʀʏᴏɴᴇ, ᴄᴏᴍᴇ ᴏɴ ᴠᴄ ᴏᴜᴛ!</b>",
    "<b>ʏᴏᴏ ᴠᴄ ᴛɪᴍᴇ ᴇᴠᴇʀʏᴏɴᴇ, ᴠᴄ ᴠɪᴄᴛᴏʀ ᴇᴠᴇʀʏ ᴇᴠᴇʀ ᴡɪᴛʜ ᴄᴏᴍᴇ!</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ! ᴇᴠᴇʀʏ ᴡᴏᴏᴏʟ ᴠᴏʏᴀᴛ ᴄᴏᴍᴇ ᴠᴄ!</b>",
    "<b>ᴠᴇʀᴇ ɢᴏɪɴɢ ᴠᴄ, ᴄᴏᴍᴇ ᴏɴ!</b>",
    "<b>ᴄᴏᴍᴇ ᴄʜᴀʟᴏ, ᴠᴇʀʏ ɴᴏᴏᴇ ᴠᴄ ᴇᴠᴇʀʏᴏɴᴇ!</b>",
    "<b>ᴏᴍᴇᴇᴇ ᴠᴏᴏᴏᴏᴏ ᴄᴏᴍᴇᴇᴇ 🥳</b>",
    "<b>ᴄᴏᴍᴇ ᴏɴ ᴄᴏᴍᴇ ᴠᴄ!</b>",
    "<b>ᴠᴄ ᴛᴇᴀᴍ ᴄᴏᴍᴇ ᴏɴ ᴇᴠᴇʀʏᴏɴᴇ!</b>"
]

@app.on_message(filters.command(["vctag", "vctags"], prefixes=["/", "."]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("<b>ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ᴛʜᴏsᴇ sᴍᴀʀᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴜsᴇ ɪᴛ. Iғ ʏᴏᴜ ᴄᴀɴ’ᴛ ʜᴀɴᴅʟᴇ ɪᴛ, ᴍᴀʏʙᴇ ʏᴏᴜ sʜᴏᴜʟᴅ ʀᴇᴛʜɪɴᴋ ʏᴏᴜʀ sᴛᴀᴛᴜs.</b>")

    if message.from_user.id in SUDOERS:
        is_admin = True  
    else:
        is_admin = False
        try:
            participant = await client.get_chat_member(chat_id, message.from_user.id)
            is_admin = participant.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
        except UserNotParticipant:
            is_admin = False

    if not is_admin:
        return await message.reply("<b>ʏᴏᴜ’ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴀʀʟɪɴɢ. ᴏɴʟʏ ᴛʜᴏsᴇ ᴡɪᴛʜ ᴀᴄᴛᴜᴀʟ ᴀᴜᴛʜᴏʀɪᴛʏ ᴄᴀɴ ᴅᴏ ᴛʜɪs.</b>")

    if message.reply_to_message and message.text:
        return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ, sᴡᴇᴇᴛʜᴇᴀʀᴛ. ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ɴᴇxᴛ ᴛɪᴍᴇ, sᴡᴇᴇᴛʜᴇᴀʀᴛ. ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")
    else:
        return await message.reply("<b>/sᴘᴀᴍ ᴊᴜsᴛ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ.</b>")

    if chat_id in spam_chats:
        return await message.reply("<b>ᴏʜʜ, ᴘʟᴇᴀsᴇ ! ᴀᴛ ʟᴇᴀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴛʜᴇ ᴘʀᴏᴄᴇss ғᴏʀ ᴀ ᴍᴏᴍᴇɴᴛ.</b>")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""  # Initialize usrtxt as an empty string

    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"{usr.user.mention} "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}]({usr.mention})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except ValueError:
        pass 


@app.on_message(filters.command(["stopvc"]))
async def cancel_spam(client, message):
    if message.chat.id not in spam_chats:
        return await message.reply("<b>ᴄᴜʀʀᴇɴᴛʟʏ, ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ, ᴅᴀʀʟɪɴɢ...</b>")
    
    if message.from_user.id in SUDOERS:
        spam_chats.remove(message.chat.id)  
        return await message.reply("<b>ᴀʜʜ, ғᴏʀ ʜᴇᴀᴠᴇɴ's sᴀᴋᴇ, ɪᴛ's sᴛᴏᴘᴘᴇᴅ.</b>")
    
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
        is_admin = participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        )
    except UserNotParticipant:
        is_admin = False

    if not is_admin:
        return await message.reply("<b>ʏᴏᴜ’ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴀʀʟɪɴɢ. ᴏɴʟʏ ᴛʜᴏsᴇ ᴡɪᴛʜ ᴀᴄᴛᴜᴀʟ ᴀᴜᴛʜᴏʀɪᴛʏ ᴄᴀɴ ᴅᴏ ᴛʜɪs.</b>")
    
    try:
        spam_chats.remove(message.chat.id)
    except ValueError:
        pass  
    return await message.reply("<b>ᴀʜʜ, ғᴏʀ ʜᴇᴀᴠᴇɴ's sᴀᴋᴇ, ɪᴛ's sᴛᴏᴘᴘᴇᴅ.</b>")
