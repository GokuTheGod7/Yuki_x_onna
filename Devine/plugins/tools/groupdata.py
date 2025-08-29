import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from config import OWNER_ID, SPECIAL_USER as SPECIAL_USER_ID
from Devine import app as devine

@devine.on_message(~filters.private & filters.command(["groupdata"], prefixes=["/", ".", "!", "#"]), group=2)
async def instatus(devine, message):
    start_time = time.perf_counter()
    user = await devine.get_chat_member(message.chat.id, message.from_user.id)
    count = await devine.get_chat_members_count(message.chat.id)
    
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ) or message.from_user.id in {OWNER_ID, SPECIAL_USER_ID}:
        sent_message = await message.reply_text("ɢᴇᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ")
        await sleep(0.1)
        await sent_message.edit("ɢᴇᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.")
        await sleep(0.1)
        await sent_message.edit("ɢᴇᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ..")
        await sleep(0.1)
        await sent_message.edit("ɢᴇᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ...")
        await sleep(0.1)
        await sent_message.edit("ɢᴏᴛ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ")
        
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        
        async for ban in devine.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        
        async for member in devine.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await sent_message.edit(f"""
<b>• ɴᴀᴍᴇ : {message.chat.title}</b>
<b>• ᴍᴇᴍʙᴇʀs : {count}</b>
<b>• ʙᴏᴛs : {bot}</b>
<b>• ᴢᴏᴍʙɪᴇs : {deleted_acc}</b>
<b>• ʙᴀɴɴᴇᴅ ᴜsᴇʀs : {banned}</b>
<b>• ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀs : {premium_acc}</b>\n
<b>↬ ᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {timelog}s</b>""")
    else:
        sent_message = await message.reply_text("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴇxᴇᴄᴜᴛᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ !")
        await sleep(5)
        await sent_message.delete()
