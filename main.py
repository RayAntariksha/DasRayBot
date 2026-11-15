import discord
from discord.ext import commands

import config

COGS = [
    "cogs.general",
    "cogs.admin",
    "cogs.fun",
    "cogs.audio",
    "cogs.friends",
]


class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=config.PREFIX, intents=intents)

    async def setup_hook(self):
        for cog in COGS:
            await self.load_extension(cog)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        print("Bot is ready!")


def main():
    if not config.TOKEN:
        raise ValueError("DISCORD_TOKEN not found in .env file!")
    MyBot().run(config.TOKEN)


if __name__ == "__main__":
    main()
