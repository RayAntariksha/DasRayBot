import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Configure bot intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Bot is ready!")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Bot Information",
        description="A simple Discord bot built with discord.py.",
        color=discord.Color.blurple()
    )

    embed.add_field(name="Bot Name", value=bot.user.name)
    embed.add_field(name="Prefix", value="!")
    embed.add_field(name="Library", value="discord.py")

    await ctx.send(embed=embed)



@bot.command()
async def checkperms(ctx):
    member = ctx.guild.me
    perms = ctx.channel.permissions_for(member)

    print("\n===== BOT PERMISSION CHECK =====")
    print(f"Server: {ctx.guild.name} ({ctx.guild.id})")
    print(f"Channel: {ctx.channel.name} ({ctx.channel.id})")
    print(f"Bot: {member} ({member.id})")
    print(f"View Channel: {perms.view_channel}")
    print(f"Send Messages: {perms.send_messages}")
    print(f"Send in Threads: {perms.send_messages_in_threads}")
    print(f"Embed Links: {perms.embed_links}")
    print(f"Read History: {perms.read_message_history}")
    print("================================\n")

# Run bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file!")

bot.run(TOKEN)
