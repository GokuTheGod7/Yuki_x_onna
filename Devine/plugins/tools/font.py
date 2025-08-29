from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Devine.utils.fonts import Fonts
from Devine import app
from Devine import app as pbot

@app.on_message(filters.command(["font", "fonts"]))
async def style_buttons(c, m, cb=False):
    buttons = [
        [
            InlineKeyboardButton("𝗦𝗮𝗻𝘀", callback_data="style+sans"),
            InlineKeyboardButton("𝙎𝙖𝙣𝙨", callback_data="style+slant_sans"),
            InlineKeyboardButton("𝖲𝖺𝗇𝗌", callback_data="style+sim"),
        ],
        [
            InlineKeyboardButton("𝘚𝘢𝘯𝘴", callback_data="style+slant"),
            InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
            InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒇", callback_data="style+bold_cool"),
        ],
        [
            InlineKeyboardButton("𝑆𝑒𝑟𝑖𝑓", callback_data="style+cool"),
            InlineKeyboardButton("𝓈𝒸𝓇𝒾𝓅𝓉", callback_data="style+script"),
            InlineKeyboardButton("𝓼𝓬𝓻𝓲𝓹𝓽", callback_data="style+script_bolt"),
        ],
        [
            InlineKeyboardButton("sᴍᴀʟʟ cᴀᴘs", callback_data="style+small_cap"),
            InlineKeyboardButton("🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅨", callback_data="style+circle_dark"),
            InlineKeyboardButton("Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data="style+circles"),
        ],
        [
            InlineKeyboardButton("𝕲𝖔𝖙𝖍𝖎𝖈", callback_data="style+gothic_bolt"),
            InlineKeyboardButton("𝔊𝔬𝔱𝔥𝔦𝔠", callback_data="style+gothic"),
            InlineKeyboardButton("ᵗⁱⁿʸ", callback_data="style+tiny"),
        ],
        [
            InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
            InlineKeyboardButton("ᑕOᗰIᑕ", callback_data="style+comic"),
            InlineKeyboardButton("🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data="style+special"),
        ],
        [
            InlineKeyboardButton("🅂🅀🅄🄰🅇🅴🅂", callback_data="style+squares"),
            InlineKeyboardButton("🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data="style+squares_bold"),
            InlineKeyboardButton("ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ", callback_data="style+andalucia"),
        ],
        [
            InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_reply"),
        ]
    ]
    
    if not cb:
        await m.reply_text(
            text=m.text.split(None, 1)[1],
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
        )
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@pbot.on_callback_query(filters.regex("^style"))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split("+")
    
    # Map styles to their respective font class methods
    style_map = {
        "typewriter": Fonts.typewriter,
        "outline": Fonts.outline,
        "serif": Fonts.serief,
        "bold_cool": Fonts.bold_cool,
        "cool": Fonts.cool,
        "small_cap": Fonts.smallcap,
        "script": Fonts.script,
        "script_bolt": Fonts.bold_script,
        "tiny": Fonts.tiny,
        "comic": Fonts.comic,
        "sans": Fonts.san,
        "slant_sans": Fonts.slant_san,
        "slant": Fonts.slant,
        "sim": Fonts.sim,
        "circles": Fonts.circles,
        "circle_dark": Fonts.dark_circle,
        "gothic": Fonts.gothic,
        "gothic_bolt": Fonts.bold_gothic,
        "cloud": Fonts.cloud,
        "happy": Fonts.happy,
        "sad": Fonts.sad,
        "special": Fonts.special,
        "squares": Fonts.square,
        "squares_bold": Fonts.dark_square,
        "andalucia": Fonts.andalucia,
        "manga": Fonts.manga,
        "stinky": Fonts.stinky,
        "bubbles": Fonts.bubbles,
        "underline": Fonts.underline,
        "ladybug": Fonts.ladybug,
        "rays": Fonts.rays,
        "birds": Fonts.birds,
        "slash": Fonts.slash,
        "stop": Fonts.stop,
        "skyline": Fonts.skyline,
        "arrows": Fonts.arrows,
        "qvnes": Fonts.rvnes,
        "strike": Fonts.strike,
        "frozen": Fonts.frozen
    }
    
    cls = style_map.get(style)
    if cls:
        new_text = cls(m.message.reply_to_message.text.split(None, 1)[1])
        try:
            await m.message.edit_text(new_text, reply_markup=m.message.reply_markup)
        except Exception as e:
            print(f"Error editing message: {e}")
