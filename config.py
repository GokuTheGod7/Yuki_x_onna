import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 20046177

API_HASH = "83d15f2956be4b4b927acded8bdf780f"

BOT_TOKEN = "7063450080:AAEiv69nDlkvzmN-oyTmVUCTzoMmAvwSNGE"

BOT_ID = 8151120625

BOT_USERNAME = "Zenitsu_music_xbot"

OWNER_USERNAME = "Untouchable_Heart2205"

BOT_NAME = "˹ᴢᴇɴɪᴛsᴜ ꭙ Mᴜsɪᴄ˼"

ASSUSERNAME = "Erika_assistant"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Nezuko12:Nezuko12@cluster0.xchck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", -1002116643591))

DISASTER_LOG = -1001997798206

OWNER_ID = 7121987650

SPECIAL_USER = 6305653111

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/hxh_bot_support"

SUPPORT_CHAT = "https://t.me/zenitsu_bot_support"

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

STRING1 = getenv("STRING1", "BQGOTy8ARCCt9RMtVykcvkX3peph1J1NW3g1lsdpXvSRZ93Ip1QfRPS1tHO2tMzgYOgb30gvKHHa3_rqucqc51rKCeDJV6xlxC_j0S4hC1VYi7y2IEIVj5RMuX4yP28gQFMMUJa85pnwhUqGazgI1pG1Twv-00j3U7-YIhpjV9kYh0WeSmlTkoB8GOJs44dESNyqg0lzjWqExgwefkkisQUNyUZBGe5GGfZFMqs2-ExQ_GZ7soYyxZJN1piB0i1TNdxt62OOVbZQqcHiKLI4CAI_-tAnvRQezbos-Zgn5S7mQvDfgMPeeTkJFXKOTWPqv2XUaX1JdV2Ocsq_SQmYebBRTi7bXQAAAAG3J9YQAA")
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

START_IMG_URL =  "https://files.catbox.moe/eu11dc.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/sg2uf3.jpg"
STATS_IMG_URL = "https://files.catbox.moe/eu11dc.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/qnq089.jpg"
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
