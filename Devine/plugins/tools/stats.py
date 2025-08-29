import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from Devine import app
from Devine.core.userbot import assistants
from Devine.misc import SUDOERS, mongodb
from Devine.plugins import ALL_MODULES
from Devine.utils.database import get_served_chats, get_served_users, set_assistant_new, force_add_served_chat, add_served_chat , get_sudoers
from Devine.utils.decorators.language import language, languageCB
from Devine.utils.inline.stats import back_stats_buttons, stats_buttons
from config import filter, OWNER_ID

@app.on_message(filters.command("forceadd"))
async def forceadd_handler(client, message: Message):
    chat_id = message.chat.id
    
    await add_served_chat(chat_id)

    await message.reply(f"Chat {chat_id} has been successfully added to the database.")

@app.on_message(filters.command("ssistant"))
async def forceassistant_handler(client, message: Message):
    chat_id = message.chat.id
    assistant_number = 1
    await set_assistant_new(chat_id, assistant_number)
    await message.reply(f"Chat {chat_id} has been successfully assigned to Assistant {assistant_number}.")
    
@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~filter)
@language
async def stats_global(client, message: Message, _):
    if message.from_user.id != OWNER_ID:  # Only allow owner
        return await message.reply_text("You are not authorized to use this command.")
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
        disable_web_page_preview=False,  # Enable page preview
    )


@app.on_callback_query(filters.regex("stats_back") & ~filter)
@languageCB
async def home_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id != OWNER_ID:  # Only allow owner
        return await CallbackQuery.answer("You are not authorized to use this command.", show_alert=True)
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    await CallbackQuery.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
        disable_web_page_preview=False,  # Enable page preview
    )


@app.on_callback_query(filters.regex("TopOverall") & ~filter)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id != OWNER_ID:  # Only allow owner
        return await CallbackQuery.answer("You are not authorized to use this command.", show_alert=True)
    await CallbackQuery.answer()
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(filter),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    await CallbackQuery.edit_message_text(
        text,
        reply_markup=upl,
        disable_web_page_preview=False,  # Enable page preview
    )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id != OWNER_ID:  # Only allow owner
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(filter),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    await CallbackQuery.edit_message_text(
        text,
        reply_markup=upl,
        disable_web_page_preview=False,  # Enable page preview
    )
