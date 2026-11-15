import discord
from discord.ext import commands

import config


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author.mention}!")

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="Bot Information",
            description="A simple Discord bot built with discord.py.",
            color=discord.Color.blurple(),
        )
        embed.add_field(name="Bot Name", value=self.bot.user.name)
        embed.add_field(name="Prefix", value=config.PREFIX)
        embed.add_field(name="Library", value="discord.py")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
