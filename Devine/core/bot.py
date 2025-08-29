from pyrogram import Client, errors
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
from ..logging import LOGGER

class Devine(Client):
    def __init__(self):
        LOGGER(__name__).info("Devine Music Starting...")
        super().__init__(
            name="Devine",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        try:
            await super().start()
            self.id = self.me.id
            self.name = f"{self.me.first_name} {(self.me.last_name or '')}"
            self.username = self.me.username
            self.mention = self.me.mention

            keyboard = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("ᴄʀᴇᴀᴛᴏʀ", user_id=config.OWNER_ID)
                ],
                [
                    InlineKeyboardButton("ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/hxh_network"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/zenitsu_bot_support"),
                ]
            ])

            try:
                # Use the public channel username instead of chat_id
                await self.send_message(
                    chat_id="@zenitsu_xsupport",
                    text=(
                        f"<b>{self.mention} ɪs ᴀʟɪᴠᴇ <a href='https://files.catbox.moe/y4xape.jpg' target='_blank'>💖</a></b>\n\n"
                        f"<b>• ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟷 ʀx</code>\n"
                        f"<b>• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>𝟹.𝟷𝟶.𝟷𝟷</code>\n"
                        f"<b>• ᴘʏᴛʜᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟶.𝟷𝟶𝟼</code>"
                    ),
                    reply_markup=keyboard
                )
            except (errors.ChannelInvalid, errors.PeerIdInvalid) as e:
                LOGGER(__name__).warning(
                    f"Warning: Bot has failed to access the log channel. Error: {str(e)}. Make sure your bot is added to the log group/channel."
                )
            except Exception as ex:
                LOGGER(__name__).warning(
                    f"Warning: Bot has failed to send a message to the log group/channel. Error: {str(ex)}"
                )

            LOGGER(__name__).info(f"Bot Started as {self.name}")

        except Exception as e:
            LOGGER(__name__).error(f"Error during bot startup: {str(e)}")
            exit()

    async def stop(self):
        try:
            await super().stop()
            LOGGER(__name__).info("Bot stopped successfully.")
        except Exception as e:
            LOGGER(__name__).warning(f"Warning: Failed to stop the bot. Error: {str(e)}")
