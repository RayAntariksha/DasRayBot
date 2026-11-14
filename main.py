import csv
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
async def galide(ctx):
    await ctx.send(random.choice(gali))


# audio stuff

@bot.command()
async def playsound(ctx, *, sound_name: str):
    try:
        path = f"./assets/audio/{sound_name}.mp3"

        file = discord.File(path, filename=f"{sound_name}.mp3")
        await ctx.reply(file=file)

    except FileNotFoundError:
        await ctx.reply("Audio file not found!")

    except discord.Forbidden:
        print("Missing permissions to send audio!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")


# Who is it?


@bot.command()
async def whois(ctx, *, search_name: str):
    try:
        with open("./assets/friends.csv", "r", encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["name"].strip().lower() == search_name.strip().lower():
                    embed = discord.Embed(
                        title=row["name"],
                        description=row["bio"],
                        color=discord.Color.blue()
                    )

                    embed.add_field(
                        name="Username",
                        value=row["username"],
                        inline=False
                    )
                if row["username"].strip().lower() == search_name.strip().lower():
                    embed = discord.Embed(
                        title=row["name"],
                        description=row["bio"],
                        color=discord.Color.blue()
                    )

                    embed.add_field(
                        name="Username",
                        value=row["username"],
                        inline=False
                    )

                    await ctx.reply(embed=embed)
                    return

        await ctx.reply(f"No friend named **{search_name}** was found!")

    except FileNotFoundError:
        await ctx.reply("The friends database could not be found!")

    except discord.Forbidden:
        print("Missing permissions to send messages!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")

    except (KeyError, TypeError) as e:
        print(f"CSV formatting error: {e}")

# Run bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file!")

bot.run(TOKEN)
