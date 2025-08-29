from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Devine import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"settingsback_helper")]
    second = [
        InlineKeyboardButton(
            text="ʙᴀᴄᴋ",
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴍɪɴ",
                callback_data="help_callback hb1",
            ),
            InlineKeyboardButton(
                text="ᴀᴜᴛʜ",
                callback_data="help_callback hb2",
            ),
            InlineKeyboardButton(
                text="ᴄ-ᴘʟᴀʏ",
                callback_data="help_callback hb3",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʟᴏᴏᴘ",
                callback_data="help_callback hb4",
            ),
            InlineKeyboardButton(
                text="ᴘʟᴀʏ",
                callback_data="help_callback hb5",
            ),
            InlineKeyboardButton(
                text="ᴘɪɴɢ",
                callback_data="help_callback hb6",
            ),
        ],
        [
            InlineKeyboardButton(
                text="sʜᴜғғʟᴇ",
                callback_data="help_callback hb7",
            ),
            InlineKeyboardButton(
                text="sᴇᴇᴋ",
                callback_data="help_callback hb8",
            ),
            InlineKeyboardButton(
                text="sᴘᴇᴇᴅ",
                callback_data="help_callback hb9",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢᴀᴍᴇs",
                callback_data="help_callback hb10",
            ),
            InlineKeyboardButton(
                text="ᴛᴇxᴛ ᴇᴅɪᴛᴏʀ",
                callback_data="help_callback hb11",
            ),
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ ᴅᴀᴛᴀ",
                callback_data="help_callback hb12",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴀꜱꜱᴡᴏʀᴅ",
                callback_data="help_callback hb13",
            ),
            InlineKeyboardButton(
                text="sᴀɴɢᴍᴇᴛᴀ",
                callback_data="help_callback hb14",
            ),
            InlineKeyboardButton(
                text="ᴡʀɪᴛᴇ",
                callback_data="help_callback hb15",
                ),
            ],
            mark,
        ]
    )
    return upl  # Indent this line to be part of the function

def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl

def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
