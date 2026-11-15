import discord
from discord.ext import commands

from utils.friends_db import load_friends, save_friends


class Friends(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whois(self, ctx, *, search_name: str):
        search = search_name.strip().lower()
        try:
            _, rows = load_friends()
        except FileNotFoundError:
            await ctx.reply("The friends database could not be found!")
            return

        try:
            for row in rows:
                name = row["name"].strip()
                username = row["username"].strip()
                displayname = row["displayname"].strip()

                if search in (name.lower(), username.lower(), displayname.lower()):
                    embed = discord.Embed(
                        title=name,
                        description=row["bio"].strip(),
                        color=discord.Color.blue(),
                    )
                    embed.add_field(name="Display name", value=displayname, inline=False)
                    embed.add_field(name="Username", value=username, inline=False)
                    await ctx.reply(embed=embed)
                    return
        except (KeyError, TypeError) as e:
            print(f"CSV formatting error: {e}")
            await ctx.reply("The friends database is formatted incorrectly!")
            return

        await ctx.reply(f"No friend named **{search_name.strip()}** was found!")

    @commands.command()
    async def changebio(self, ctx, *, args: str):
        usage = "Usage: `!changebio Name | New bio`"
        if "|" not in args:
            await ctx.reply(usage)
            return

        name, new_bio = (part.strip() for part in args.split("|", 1))
        if not name or not new_bio:
            await ctx.reply(usage)
            return

        try:
            fieldnames, rows = load_friends()
        except FileNotFoundError:
            await ctx.reply("The friends database could not be found!")
            return

        if not fieldnames or not {"name", "bio"}.issubset(fieldnames):
            await ctx.reply("Invalid friends database format!")
            return

        for row in rows:
            if row["name"].strip().lower() == name.lower():
                row["bio"] = new_bio
                save_friends(fieldnames, rows)
                await ctx.reply(f"Successfully updated **{name}**'s bio!")
                return

        await ctx.reply(f"No friend named **{name}** was found!")


async def setup(bot):
    await bot.add_cog(Friends(bot))
