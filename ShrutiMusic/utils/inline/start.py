from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text="˹ᴄʟᴏɴᴇ ᴍᴜꜱɪᴄ˼", url="https://t.me/Sitaramusic_bot"),
            InlineKeyboardButton(text="˹ᴍᴏᴠɪᴇ ʙᴏᴛ˼", url="https://t.me/Nishumoviebot")
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="˹ᴄʟᴏɴᴇ ᴍᴜꜱɪᴄ˼", url="https://t.me/DEVA_MUSICBOT"),
            InlineKeyboardButton(text="˹ᴍᴏᴠɪᴇ ʙᴏᴛ˼", url="https://t.me/ShiningMovie_Bot")
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
    ]
    return buttons
