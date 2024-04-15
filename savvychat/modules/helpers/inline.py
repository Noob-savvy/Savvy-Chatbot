from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from models import MODELS
from config import SUPPORT_GRP, UPDATE_CHNL
from savvychat import OWNER
from savvychat import savvychat

DEV_OP = [
    [
        InlineKeyboardButton(text="❀ ᴏᴡɴᴇʀ ❀", user_id=OWNER),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{savvychat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
       # InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="❀ ᴀʙᴏᴜᴛ ❀", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="❀ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ❀",
            url=f"https://t.me/{savvychat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄʟᴏsᴇ ⦿",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="❀ ᴄʜᴀᴛʙᴏᴛ ❀", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="❀ ᴛᴏᴏʟs ❀", callback_data="TOOLS_DATA"),
    ],
    [
       
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


GPT_BTN = [
   [
        InlineKeyboardButton(
            text="❀ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ❀",
            url=f"https://t.me/{savvychat.username}?startgroup=true",
        ),
    ],
      [
        InlineKeyboardButton(text="❀ ᴏᴡɴᴇʀ ❀", user_id=OWNER),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
      
]


S_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="❀ ᴄʟᴏsᴇ ❀", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{savvychat.username}?start=help"
        ),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="❀ sᴜᴘᴘᴏʀᴛ ❀", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="❀ ᴏᴡɴᴇʀ ❀", user_id=OWNER),
     #   InlineKeyboardButton(text="❄️ sᴏᴜʀᴄᴇ ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="❀ ᴜᴘᴅᴀᴛᴇs ❀", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP = """
● Send a Prompt , Reply /generate to the Prompt to start Image Generation
"""

CLOSE_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Back", callback_data="cbclose"),
        ]
    ]
)


BACK = [InlineKeyboardButton("BACK", callback_data="back")]


SETTINGS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Choose Model", callback_data="choose_model"),
            InlineKeyboardButton("Change Steps", callback_data="change_steps"),
        ],
        [
            InlineKeyboardButton("Change Seed", callback_data="change_seed"),
            InlineKeyboardButton(
                "Change Image Count", callback_data="change_image_count"
            ),
        ],
        [InlineKeyboardButton("Save Settings", callback_data="save_settings")],
    ]
)

MODELS_BUTTON = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(model, callback_data=f"select_model_{index}")]
        for index, model in enumerate(MODELS)
    ]
    + [[InlineKeyboardButton("Back", callback_data="cb_back_settings")]]
)


STEPS_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-steps"),
            InlineKeyboardButton("+", callback_data="+steps"),
        ],
        [InlineKeyboardButton("Back", callback_data="cb_back_settings")],
    ]
)
IMAGE_COUNT_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-image"),
            InlineKeyboardButton("+", callback_data="+image"),
        ],
        [InlineKeyboardButton("Back", callback_data="cb_back_settings")],
    ]
)
