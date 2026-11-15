import discord
from discord.ext import commands

import config


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def playsound(self, ctx, *, sound_name: str):
        path = (config.AUDIO_DIR / f"{sound_name}.mp3").resolve()

        # Block names like "../../secret" from escaping the audio folder
        if config.AUDIO_DIR.resolve() not in path.parents or not path.is_file():
            await ctx.reply(
                "Audio file not found! Try `!soundlist` to see available files."
            )
            return

        try:
            await ctx.reply(file=discord.File(path, filename=path.name))
        except discord.Forbidden:
            print("Missing permissions to send audio!")
        except discord.HTTPException as e:
            print(f"Discord API error: {e}")

    @commands.command()
    async def soundlist(self, ctx):
        names = sorted(p.stem for p in config.AUDIO_DIR.glob("*.mp3"))
        body = "\n".join(names) if names else "(none)"
        await ctx.send(f"Available audio files:\n```{body}```")


async def setup(bot):
    await bot.add_cog(Audio(bot))
