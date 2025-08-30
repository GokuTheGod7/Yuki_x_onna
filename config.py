import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 24542160

API_HASH = "143ef5efcaf0f2b259dcd0ea2cfaf336"

BOT_TOKEN = "8096745814:AAFZ2M7mpkKPMvyIqpUsoF1DbG1S4cJef4I"

BOT_ID = 8096745814

BOT_USERNAME = "Yuki_xprobot"

OWNER_USERNAME = "OG_Goku_God_7"

BOT_NAME = "• Yυᴋɪ Oɴɴᴀ ✘ Mᴜsɪᴄ ♪"

ASSUSERNAME = "@Onna_Assistant"

MONGO_DB_URI = getenv("MONGO_DB_URI ","mongodb+srv://Saib:saib2005@cluster0.qck8hxs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID ", "-1002035748224")

DISASTER_LOG = -1002035748224

OWNER_ID = 7793156995

SPECIAL_USER = 6266348511

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/GokuTheGod7/Yuki_x_onna"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/eternal_bot_updates"

SUPPORT_CHAT = "https://t.me/et_bot_updates"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = "BQF2e9AAE1cz_cTrpCUli3yIrjUpbZH7w1fJk6gfy7_IHll6KdPc-A2PdI7bM0Z1ZGOWp_1WCJBgIafkGX33bLj7b4ejkJ5u3Pn4nhCc2I9h1AQMt5ifQXZrGzDjy4xRESupUq-tafjN8PZmUk7Ui3-VheWUyO_rtb7_qG3gF8E_sQQ1SVJU4l85tv00e0k2_qaUnng1eLzKMw0sLmGf3xbfy6YKut-C69Pf_V1_gfFFfdaua8rXCmDb_SFPw_Wq-7hf_Zex7py54OY8Mqnuos2KFPv9fOigt1W-0Lst5lCI6Dhn8MrYzseBZKbG_FlPeLUhZ0ypox8R-owMrjxVpxMsplRYCQAAAAHTUNvuAA"
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://files.catbox.moe/u8507f.mp4"
PLAYLIST_IMG_URL = "https://graph.org/file/509972c72fde0bcea6909-188ae866613d73009e.jpg"
STATS_IMG_URL = "https://graph.org/file/b6a83738eef8bc212eb82-c5dcb24326f4eea4db.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/94e6ca90e11e31e5a3ea0-5cac62458aad508530.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/dc6htz.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eu11dc.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eu11dc.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eu11dc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/sg2uf3.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/qnq089.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eu11dc.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
