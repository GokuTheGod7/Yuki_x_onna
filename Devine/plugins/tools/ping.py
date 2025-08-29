from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Devine import app
from Devine.core.call import devine as Devine
from Devine.utils import bot_sys_stats
from Devine.utils.decorators.language import language
from config import BANNED_USERS, SUPPORT_CHANNEL, SUPPORT_CHAT


@app.on_message(filters.command(["ping", "status"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_text(
        text=_["ping_1"].format(app.mention),
    )  # Fixed missing parenthesis here

    pytgping = await Devine.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            ],
            [
                InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=true"),
            ],
        ])
    )






import asyncio
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import OWNER_ID
from Devine import app
import config 

@app.on_message(filters.command("alive"))
async def awake(_, message: Message):
    loading_1 = await message.reply_text("💖")
    await asyncio.sleep(0.5)

    loading_texts = [
        "<b>ʟᴏᴀᴅɪɴɢ</b>",
        "<b>ʟᴏᴀᴅɪɴɢ.</b>",
        "<b>ʟᴏᴀᴅɪɴɢ..</b>",
        "<b>ʟᴏᴀᴅɪɴɢ...</b>"
    ]

    for text in loading_texts:
        await loading_1.edit_text(text)
        await asyncio.sleep(1)  
    
    await loading_1.delete()

    owner = await app.get_users(OWNER_ID)
    
    if message.from_user.id == OWNER_ID:
        TEXT = "ɪ'ᴍ ᴀʟɪᴠᴇ ᴍʏ ʟᴏʀᴅ <a href='https://files.catbox.moe/qnq089.jpg' target='_blank'>⚡</a> !\n\n"
    else:
        TEXT = f"ʏᴏᴏ {message.from_user.mention}, <a href='https://files.catbox.moe/dc6htz.jpg' target='_blank'>⚡</a>\n\nɪ'ᴍ {app.mention}\n──────────────────\n"
    
    TEXT += f"ᴄʀᴇᴀᴛᴏʀ ⌯ {owner.mention}\n"
    TEXT += f"ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟷𝟼 ʀx\n"
    TEXT += f"ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ⌯ 𝟹.𝟷𝟸.𝟶\n"
    TEXT += f"ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ ⌯ 𝟸.𝟶.𝟷𝟶𝟼"
    
    BUTTON = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ", url="https://t.me/{app.username}?startgroup=true"),
    ],
    ]    
    
    await message.reply_text(
        text=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        )
