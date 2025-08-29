from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        # Initialize assistant clients
        self.one = Client(
            name="Devineassistant1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="Devineassistant2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="Devineassistant3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="Devineassistant4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="Devineassistant5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")

        if config.STRING1:
            try:
                await self.one.start()
                await self.one.join_chat("As_cosmos")
                await self.one.join_chat("HXH_NETWORK")
                assistants.append(1)
                await self.one.send_message("@zenitsu_xsupport", "<b>𝟷'sᴛ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                self.one.id = self.one.me.id
                self.one.name = self.one.me.mention
                self.one.username = self.one.me.username
                assistantids.append(self.one.id)
                LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
            except Exception as e:
                LOGGER(__name__).warning(f"Warning: Failed to start Assistant 1 - {str(e)}")

        if config.STRING2:
            try:
                await self.two.start()
                await self.two.join_chat("as_cosmos")
                await self.two.join_chat("hxh_network")
                assistants.append(2)
                await self.two.send_message("@zenitsu_xsupport", "<b>𝟸ɴᴅ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                self.two.id = self.two.me.id
                self.two.name = self.two.me.mention
                self.two.username = self.two.me.username
                assistantids.append(self.two.id)
                LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
            except Exception as e:
                LOGGER(__name__).warning(f"Warning: Failed to start Assistant 2 - {str(e)}")
                
        if config.STRING3:
            try:
                await self.three.start()
                await self.three.join_chat("as_cosmos")
                await self.three.join_chat("hxh_network")
                assistants.append(3)
                await self.three.send_message("@zenitsu_xsupport", "<b>𝟹ʀᴅ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                self.three.id = self.three.me.id
                self.three.name = self.three.me.mention
                self.three.username = self.three.me.username
                assistantids.append(self.three.id)
                LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")
            except Exception as e:
                LOGGER(__name__).warning(f"Warning: Failed to start Assistant 3 - {str(e)}")
                
        if config.STRING4:
            try:
                await self.four.start()
                await self.four.join_chat("as_cosmos")
                await self.four.join_chat("hxh_network")
                assistants.append(4)
                await self.four.send_message("@zenitsu_xsupport", "<b>𝟺ᴛʜ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                self.four.id = self.four.me.id
                self.four.name = self.four.me.mention
                self.four.username = self.four.me.username
                assistantids.append(self.four.id)
                LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")
            except Exception as e:
                LOGGER(__name__).warning(f"Warning: Failed to start Assistant 4 - {str(e)}")

        if config.STRING5:
            try:
                await self.five.start()
                await self.five.join_chat("as_cosmos")
                await self.five.join_chat("hxh_network")
                assistants.append(5)
                await self.five.send_message("@zenitsu_xsupport", "<b>𝟻ᴛʜ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                self.five.id = self.five.me.id
                self.five.name = self.five.me.mention
                self.five.username = self.five.me.username
                assistantids.append(self.five.id)
                LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")
            except Exception as e:
                LOGGER(__name__).warning(f"Warning: Failed to start Assistant 5 - {str(e)}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).warning(f"Warning: Failed to stop one or more assistants - {str(e)}")
