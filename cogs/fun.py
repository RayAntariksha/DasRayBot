import random

import pyjokes
from discord.ext import commands

import config


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gali = self._load_gali()

    @staticmethod
    def _load_gali():
        with open(config.GALI_FILE, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    @commands.command()
    async def galide(self, ctx):
        await ctx.send(random.choice(self.gali))

    @commands.command()
    async def joke(self, ctx):
        await ctx.send(pyjokes.get_joke(category="neutral"))


async def setup(bot):
    await bot.add_cog(Fun(bot))
