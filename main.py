import os
import random

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
    print(f"View Channel:, {perms.view_channel}")
    print(f"Send Messages:, {perms.send_messages}")
    print(f"Attach Files:, {perms.attach_files}")
    print("================================\n")

# To anyone reading this, please don't read the array below. It is just a joke.
# I am warning you, DON'T READ THE ARRAY BELOW. YOU WILL BE RESPONSIBLE FOR IT.
gali = [
        "gandu", "madarchod", "bhosdike", "chutiya", "harami", "randi",
        "bhenchod", "lodu", "lund", "chodu", "gali kere ditam be?",
        "Sala bokka choda tor dudh er kosom tor moto leura choda ami deksi na"
        ]


@bot.command()
async def gali_de(ctx):
    await ctx.send(random.choice(gali))


# audio stuff
@bot.command()
async def fahh(ctx):
    try:
        file = discord.File("./assets/audio/fahh.mp3", filename="fahh.mp3")
        await ctx.reply(file=file)

    except discord.Forbidden:
        print("Missing permissions to send audio!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")

# Run bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file!")

bot.run(TOKEN)
