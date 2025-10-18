#⟶̽ जय श्री ༢།म >𝟑🙏🚩

import asyncio
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config
from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info("🛠️ Initializing RiteshMusic Bot...")
        super().__init__(
            name="DeadlineTech",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}".strip()
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"<b>✅ Bot Started Successfully!</b>\n\n"
                    f"<b>Name:</b> {self.name}\n"
                    f"<b>Username:</b> @{self.username}\n"
                    f"<b>User ID:</b> <code>{self.id}</code>"
                ),
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "❌ Unable to send message to the log group/channel. "
                "Ensure the bot is added and not banned."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Failed to access the log group/channel.\nReason: {type(ex).__name__}"
            )
            exit()

        try:
            member = await self.get_chat_member(config.LOGGER_ID, self.id)
            if member.status != ChatMemberStatus.ADMINISTRATOR:
                LOGGER(__name__).error(
                    "⚠️ Bot is not an admin in the log group/channel. Please promote it as admin."
                )
                exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"❌ Failed to fetch bot status in log group. Reason: {type(ex).__name__}"
            )
            exit()

        LOGGER(__name__).info(f"🎶 Bot is online and ready as {self.name} (@{self.username})")

    async def stop(self):
        LOGGER(__name__).info("🛑 Stopping RiteshMusic Bot...")
        await super().stop()
