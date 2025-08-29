from Devine.core.bot import Devine as devine
from Devine.core.dir import dirr
from Devine.core.git import git
from Devine.core.userbot import Userbot
from Devine.misc import dbb, heroku
from Devine.server import start_flask


from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

start_flask()

app = devine()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
