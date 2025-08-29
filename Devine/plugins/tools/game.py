import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Devine import app  

@app.on_message(filters.command("truth"))
async def truth(client: Client, message: Message):
    truth = requests.get("https://api.truthordarebot.xyz/v1/truth").json()["question"]
    await message.reply_text(truth)


@app.on_message(filters.command("dare"))
async def dare(client: Client, message: Message):
    dare = requests.get("https://api.truthordarebot.xyz/v1/dare").json()["question"]
    await message.reply_text(dare)
