from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON =  ("https://telegra.ph/file   /66c0f8710ae9ec62a15d9.jpg"
        "https://telegra.ph/file/66c0f8710ae9ec62a15d9.jpg"
        "https://telegra.ph/file/7a53af4d6d163d4102cd1.jpg")

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [SERAFALL](t.me/SERAFALL_LEVIATHAN_BOT)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [SAHIL](tg://user?id=5218766034=)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**SERAFALL sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=5218766034"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://telegra.ph/file/7fc5166a6681753fbb8a2.jpg")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
