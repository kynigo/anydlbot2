# (c) @PredatorHackerzZ

import asyncio
from sample_config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Son, You are Banned to use me. Contact my Dev [Support ](https://t.me/SIogan_98).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 1", url="https://t.me/DevAXD")], [InlineKeyboardButton(text=" 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 2", url="https://t.me/world_wide_movies")],
                                                    [InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 3 ", url="https://t.me/wwm_seriess")],[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 4 ", url="https://t.me/UnitedMallus")],[InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋 5 ", url="https://t.me/WWM_support")]]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my Dev [Support ](https://t.me/SIogan_98).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
