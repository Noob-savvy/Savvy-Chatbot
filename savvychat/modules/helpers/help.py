from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from savvychat import savvychat as app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="⦿ ʙᴀᴄᴋ ⦿",
            callback_data=f"close",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴘɪɴɢ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ᴄʜᴀᴛ-ʙᴏᴛ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ɪᴅ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀᴛ-ɢᴘᴛ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ᴀɪ ɪᴍɢ ɢᴇɴ",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="ᴍᴀᴛʜ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ɢʀᴏᴜᴘ ᴅᴀᴛᴀ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ɢʀᴏᴜᴘ ɪɴғᴏ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ɪᴍᴀɢᴇs",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ᴊᴏᴋᴇ",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="sᴛᴀᴛs",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ᴛᴇʟᴇɢʀᴀᴘʜ",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ɢʀᴀᴘʜ.ᴏʀɢ",
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text="ᴛʀᴀɴsʟᴀᴛᴇ",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="ᴡʀɪᴛᴇ",
                    callback_data="help_callback hb15",
    
                ),
            ],
            [

               InlineKeyboardButton(
                    text="sᴏɴɢ",
                    callback_data="help_callback hb16",
               ),
               InlineKeyboardButton(
                    text="ʙᴀʀᴅ",
                    callback_data="help_callback hb17",
               ),
               InlineKeyboardButton(
                    text="ʙʟᴀᴄᴋ ʙᴏx",
                    callback_data="help_callback hb18",
               ),
            ],
            [
               InlineKeyboardButton(
                    text="ᴠɪᴅᴇᴏ",
                    callback_data="help_callback hb19",
               ),
                InlineKeyboardButton(
                    text="ᴄᴏsᴘʟᴀʏ",
                    callback_data="help_callback hb20",
                ),
                InlineKeyboardButton(
                    text="ɢᴀᴍᴇs",
                    callback_data="help_callback hb21",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʀᴇᴇʟ",
                    callback_data="help_callback hb22",
                ),
                InlineKeyboardButton(
                    text="ʙʀᴏᴀᴅᴄᴀsᴛ",
                    callback_data="help_callback hb23",
                ),
                InlineKeyboardButton(
                    text="ᴡᴀɪғᴜ",
                    callback_data="help_callback hb24",
                ),
               
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="⦿ ʙᴀᴄᴋ ⦿",
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
                text="⦿ ʜᴇʟᴘ ⦿",
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
