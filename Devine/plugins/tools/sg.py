import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory
from Devine import userbot as us, app
from Devine.core.userbot import assistants

@app.on_message(filters.command(["sg", "sang", "sangmeta"], prefixes=["/", "!", ".", "-"]))
async def sg(client: Client, message: Message):
    if not message:
        return  

    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply("ᴘʀᴏᴠɪᴅᴇ ᴀ ᴜsᴇʀɴᴀᴍᴇ, ᴜsᴇʀ ɪᴅ, ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ.")

    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[0.1]

    lol = await message.reply("<b>ᴘʀᴏᴄᴇssɪɴɢ.</b>")
    await asyncio.sleep(0.1)
    await lol.edit("<b>ᴘʀᴏᴄᴇssɪɴɢ..</b>")
    await asyncio.sleep(0.1)
    await lol.edit("<b>ᴘʀᴏᴄᴇssɪɴɢ...</b>")
    
    try:
        user = await client.get_users(f"{args}")
    except Exception:
        return await lol.edit("sᴘᴇᴄɪғʏ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ</b>")

    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)

    if 1 in assistants:
        ubot = us.one

    try:
        a = await ubot.send_message(sg, f"{user.id}")
        await a.delete()
    except Exception as e:
        return await lol.edit(f"Error: {e}")

    await asyncio.sleep(1)

    async for stalk in ubot.search_messages(a.chat.id):
        if stalk.text:
            await message.reply(f"{stalk.text}")
            break  
    else:
        await message.reply("ᴛʜᴇ ʙᴏᴛ ɪs ᴜɴʀᴇsᴘᴏɴsɪᴠᴇ.")

    try:
        user_info = await ubot.resolve_peer(sg)
        await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    await lol.delete()
