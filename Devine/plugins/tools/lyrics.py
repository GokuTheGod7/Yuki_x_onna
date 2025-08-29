import re
from pyrogram import Client, filters
from pyrogram.types import Message

from Devine import app
from config import BANNED_USERS

import lyricsgenius as lg

# Initialize the Genius API client with your API key
GENIUS_API_KEY = "_n604o_cEemM85tf6W0LkzVVItj8kjCijqKc4b1nlT96lX2evhoqHz6E4FX3MGhf"  # Replace with your Genius API key
genius = lg.Genius(GENIUS_API_KEY, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
genius.verbose = False

@app.on_message(filters.command(["lyrics"]) & ~BANNED_USERS)
async def lrsearch(client: Client, message: Message):
    # Ensure the user provided a song name
    if len(message.command) < 2:
        return await message.reply_text("Please provide a song name to search lyrics.")

    # Extract the song title from the command
    title = message.text.split(None, 1)[1]
    msg = await message.reply_text(f"💞 Searching for lyrics of **{title}**...")

    try:
        # Search for the song using the Genius API
        song = genius.search_song(title, get_full_info=False)
        if not song:
            return await msg.edit(f"❌ Sorry, no lyrics found for **{title}**.")

        # Clean up the lyrics
        lyrics = song.lyrics
        if "Embed" in lyrics:
            lyrics = re.sub(r"\d*Embed", "", lyrics)

        # Truncate long lyrics to avoid spamming
        if len(lyrics) > 4000:
            lyrics = lyrics[:3997] + "..."

        # Send the lyrics directly in the group chat
        await msg.edit(f"🎶 **Lyrics for {title}:**\n\n{lyrics}")

    except Exception as e:
        # Handle errors and notify the user
        await msg.edit(f"⚠️ An error occurred while fetching the lyrics: {e}")
