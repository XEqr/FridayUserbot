"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""

import asyncio
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/22535f8051a58af113586.jpg"
pm_caption = "`PAYDAY IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**Payday OS** : `2.0`\n"
pm_caption += "**Current Sat** : `#man`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
