from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from models import MODELS

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
