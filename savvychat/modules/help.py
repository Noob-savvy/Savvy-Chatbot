from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from savvychat import savvychat as app

from config import SUPPORT_GRP
from savvychat.modules.helpers import (
    help_1
    help_2
    )
from savvychat.modules.helpers.help import *
from savvychat.modules.helpers import read




@app.on_message(filters.command(["help"]) & filters.private)
@app.on_callback_query(filters.regex("settings_back_helper"))
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            help_1.format(SUPPORT_GRP), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=help_1.format(SUPPORT_GRP),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group)

async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
          help_2, reply_markup=InlineKeyboardMarkup(keyboard)
          )


@app.on_callback_query(filters.regex("help_callback"))

async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb1":
        await CallbackQuery.edit_message_text(read.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(read.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(read.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(read.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(read.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(read.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(read.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(read.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(read.HELP_9, reply_markup=keyboard)
    elif cb == "hb10":
        await CallbackQuery.edit_message_text(read.HELP_10, reply_markup=keyboard)
    elif cb == "hb11":
        await CallbackQuery.edit_message_text(read.HELP_11, reply_markup=keyboard)
    elif cb == "hb12":
        await CallbackQuery.edit_message_text(read.HELP_12, reply_markup=keyboard)
    elif cb == "hb13":
        await CallbackQuery.edit_message_text(read.HELP_13, reply_markup=keyboard)
    elif cb == "hb14":
        await CallbackQuery.edit_message_text(read.HELP_14, reply_markup=keyboard)
    elif cb == "hb15":
        await CallbackQuery.edit_message_text(read.HELP_15, reply_markup=keyboard)
    elif cb == "hb16":
        await CallbackQuery.edit_message_text(read.HELP_16, reply_markup=keyboard)
    elif cb == "hb17":
        await CallbackQuery.edit_message_text(read.HELP_17, reply_markup=keyboard)
    elif cb == "hb18":
        await CallbackQuery.edit_message_text(read.HELP_18, reply_markup=keyboard)
    elif cb == "hb19":
        await CallbackQuery.edit_message_text(read.HELP_19, reply_markup=keyboard)
    elif cb == "hb20":
        await CallbackQuery.edit_message_text(read.HELP_20, reply_markup=keyboard)
    elif cb == "hb21":
        await CallbackQuery.edit_message_text(read.HELP_21, reply_markup=keyboard)
    elif cb == "hb22":
        await CallbackQuery.edit_message_text(read.HELP_22, reply_markup=keyboard)
    elif cb == "hb23":
        await CallbackQuery.edit_message_text(read.HELP_23, reply_markup=keyboard)
    elif cb == "hb24":
        await CallbackQuery.edit_message_text(read.HELP_24, reply_markup=keyboard)
