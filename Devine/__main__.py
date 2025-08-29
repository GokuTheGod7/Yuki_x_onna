import asyncio
import importlib
import subprocess
import sys
from time import sleep
from pyrogram import idle, filters
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Devine import LOGGER, app, userbot
from Devine.core.call import devine
from Devine.misc import sudo
from Devine.plugins import ALL_MODULES
from Devine.utils.database import get_banned_users, get_gbanned
from config import filter

SPECIALGRADE = ['6600178606', '5268691896']

async def init():
    try:
        if (
            not config.STRING1
            and not config.STRING2
            and not config.STRING3
            and not config.STRING4
            and not config.STRING5
        ):
            LOGGER(__name__).warning("Warning: Assistant variables are empty.")
    except Exception as e:
        LOGGER(__name__).warning(f"Warning: {str(e)}")
    
    await sudo()
    
    try:
        users = await get_gbanned()
        for user_id in users:
            filter.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Warning: Could not get global banned users - {str(e)}")
    
    try:
        users = await get_banned_users()
        for user_id in users:
            filter.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Warning: Could not get banned users - {str(e)}")
    
    try:
        await app.start()
    except Exception as e:
        LOGGER(__name__).warning(f"Warning: Failed to start app - {str(e)}")
    
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Devine.plugins" + all_module)
        except Exception as e:
            LOGGER(__name__).warning(f"Warning: Could not load module {all_module} - {str(e)}")
    
    LOGGER("Devine.plugins").info("Plugins loaded.")
    
    await userbot.start()
    await devine.start()
    
    try:
        await devine.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Devine").warning("Warning: Turn on VC of log channel.")
    except Exception as e:
        LOGGER("Devine").warning(f"Warning: Failed to start stream - {str(e)}")
    
    await devine.decorators()
    LOGGER("Devine").info("Powered by @hxh_network")

    try:
        await userbot.one.send_message("@zenitsu_xsupport", "<b>Assistant and Bot started.</b>")
        await userbot.two.send_message("@zenitsu_xsupport", "<b>Assistant 2 started successfully.</b>")
        await userbot.three.send_message("@zenitsu_xsupport", "<b>Assistant 3 started successfully.</b>")
        await userbot.four.send_message("@zenitsu_xsupport", "<b>Assistant 4 started successfully.</b>")
        await userbot.five.send_message("@zenitsu_xsupport", "<b>Assistant 5 started successfully.</b>")
    except Exception as e:
        LOGGER("Devine").warning(f"Warning: Failed to send message to @test6930ej - {str(e)}")

    await idle()
    
    try:
        await app.stop()
        await userbot.stop()
    except Exception as e:
        LOGGER("Devine").warning(f"Warning: Failed to stop bot - {str(e)}")
    LOGGER("Devine").info("Stopping bot...")

@app.on_message(filters.command("pull"))
async def git_pull_command(client, message):
    if str(message.from_user.id) not in SPECIALGRADE:
        await message.reply("You are not authorized to use this command.")
        return

    await message.reply("Pulling from the repo... please wait.")

    try:
        result = subprocess.run(
            ["git", "pull", "https://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@github.com/paradox-zenu/test", "master"],
            capture_output=True, text=True, check=True, timeout=60  # 60 seconds timeout
        )

        if "Already up to date" in result.stdout:
            return await message.reply("✅ Repo is already up to date.")
        elif result.returncode == 0:
            await message.reply(f"✅ Git pull successful! Updating the bot now...\n\n`{result.stdout}`")
            await restart_bot(message)
        else:
            await message.reply("❌ Git pull failed. Please check the logs.")
            return

    except subprocess.CalledProcessError as e:
        await message.reply(f"❌ Git pull failed with error:\n`{e.stderr}`")
    except subprocess.TimeoutExpired:
        await message.reply("❌ Git pull timed out. Please check your connection and try again.")
    except Exception as e:
        await message.reply(f"❌ Unexpected error occurred: {str(e)}")

async def restart_bot(message):
    await message.reply("`Restarting the bot...`")

    try:
        args = [sys.executable, "-m", "Devine"]
        subprocess.Popen(args)
        sys.exit()
    except Exception as e:
        await message.reply(f"❌ Failed to restart the bot. Error: {str(e)}")
        return

@app.on_message(filters.command("bot"))
async def status_check_command(client, message):
    if str(message.from_user.id) not in SPECIALGRADE:
        await message.reply("You are not authorized to use this command.")
        return

    await message.reply("✅ Bot is up and running!")

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(init())
    except Exception as e:
        LOGGER(__name__).warning(f"Warning: Main initialization failed - {str(e)}")
