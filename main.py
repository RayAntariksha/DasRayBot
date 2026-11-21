import csv
import os
import random
from zoneinfo import ZoneInfo
import discord
from datetime import datetime, timezone
from discord.ext import commands, tasks
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MEMBER_COUNT = "./assets/count.csv"
TOKEN = os.getenv("DISCORD_TOKEN")

# Configure bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("")
    print("  ____             ____             ____        ")
    print(" |  _ \\  __ _ ___ |  _ \\  __ _  ___/ __ \\ _ __  ")
    print(" | | | |/ _` / __|| |_) |/ _` |/ _ \\ / _` | '_ \\ ")
    print(" | |_| | (_| \\__ \\|  _ <| (_| | (_) | (_| | |_) |")
    print(" |____/ \\__,_|___/|_| \\_\\\\__,_|\\___/ \\__,_| .__/ ")
    print("                                          |_|    ")
    print("")
    print("Bot is ready!")

    if not log_online_users.is_running():
        log_online_users.start()


@bot.command()
async def online(ctx):
    online_members = [
        member.display_name
        for member in ctx.guild.members
        if member.status != discord.Status.offline
    ]
    await ctx.send(
        f"**Online Members ({len(online_members)}):**\n" + ", ".join(online_members)
    )


# Create the CSV file with headers if it doesn't exist
if not os.path.exists(MEMBER_COUNT):
    with open(MEMBER_COUNT, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Time", "Server", "Online Count", "Online Members"])


@tasks.loop(minutes=1)
async def log_online_users():
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    with open(MEMBER_COUNT, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for guild in bot.guilds:
            # Exclude bots and offline members
            online_members = [
                member.display_name
                for member in guild.members
                if member.status != discord.Status.offline and not member.bot
            ]

            count = len(online_members)

            writer.writerow(
                [
                    now.date(),
                    now.strftime("%H:%M:%S"),
                    guild.name,
                    count,
                    ", ".join(online_members),
                ]
            )

    print(f"Logged online users at {now.strftime('%H:%M:%S')}")


@log_online_users.before_loop
async def before_log_online_users():
    await bot.wait_until_ready()


# The Owner can download the CSV file with !download_logs
@bot.command()
@commands.is_owner()
async def download_logs(ctx):
    await ctx.send(file=discord.File(MEMBER_COUNT))
#hello riksha

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
        color=discord.Color.blurple(),
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
    "gandu",
    "madarchod",
    "bhosdike",
    "chutiya",
    "harami",
    "randi",
    "bhenchod",
    "lodu",
    "lund",
    "chodu",
    "gali kere ditam be?",
    "Sala bokka choda tor dudh er kosom tor moto leura choda ami deksi na",
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
        await ctx.reply(
            "Audio file not found! Try using !soundlist to see available sounds"
        )

    except discord.Forbidden:
        print("Missing permissions to send audio!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")


@bot.command()
async def meme(ctx, *, meme_name: str):
    try:
        path = f"./assets/memes/{meme_name}.jpg"

        file = discord.File(path, filename=f"{meme_name}.jpg")
        await ctx.reply(file=file)

    except FileNotFoundError:
        await ctx.reply("Meme not found! Try using !memelist to see available memes")

    except discord.Forbidden:
        print("Missing permissions to send audio!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")


@bot.command()
async def memelist(ctx):
    audio_files = os.listdir("./assets/memes")
    response = "```"
    for files in audio_files:
        response = response + files.split(".")[0] + "\n"
    response = response + "```"
    await ctx.send(f"Available audio files: \n {response}")


# Who is it?
@bot.command()
async def whois(ctx, *, search_name: str):
    try:
        with open(
            "./assets/friends.csv",
            "r",
            encoding="utf-8",
            newline="",
        ) as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)

            search_name = search_name.strip().lower()

            for row in reader:

                name = row["name"].strip()
                username = row["username"].strip()
                displayname = row["displayname"].strip()

                if search_name in (name.lower(), username.lower(), displayname.lower()):
                    embed = discord.Embed(
                        title=name,
                        description=row["bio"].strip(),
                        color=discord.Color.blue(),
                    )
                    embed.add_field(
                        name="Display name", value=displayname, inline=False
                    )
                    embed.add_field(name="Username", value=username, inline=False)
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


@bot.command()
async def changebio(ctx, *, args: str):
    try:
        name, new_bio = args.split("|", 1)

        name = name.strip()
        new_bio = new_bio.strip()

        if not name or not new_bio:
            await ctx.reply("Usage: `!changebio Name | New bio`")
            return

        path = "./assets/friends.csv"

        with open(path, "r", encoding="utf-8", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames
            rows = list(reader)

        if not fieldnames or not {"name", "bio"}.issubset(fieldnames):
            await ctx.reply("Invalid friends database format!")
            return

        for row in rows:
            if row["name"].strip().lower() == name.lower():
                row["bio"] = new_bio

                with open(path, "w", encoding="utf-8", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)

                await ctx.reply(f"Successfully updated **{name}**'s bio!")
                return

        await ctx.reply(f"No friend named **{name}** was found!")

    except ValueError:
        await ctx.reply("Usage: `!changebio Name | New bio`")

    except FileNotFoundError:
        await ctx.reply("The friends database could not be found!")

    except discord.Forbidden:
        print("Missing permissions to send messages!")

    except discord.HTTPException as e:
        print(f"Discord API error: {e}")

    except (KeyError, TypeError) as e:
        print(f"CSV formatting error: {e}")


@bot.command()
async def soundlist(ctx):
    audio_files = os.listdir("./assets/audio")
    response = "```"
    for files in audio_files:
        response = response + files.split(".")[0] + "\n"
    response = response + "```"
    await ctx.send(f"Available audio files: \n {response}")

coin=["Heads", "Tails"]

@bot.command()
async def coinflip(ctx):
    result = random.choice(coin)
    await ctx.send(f"The coin landed on: **{result}**")

@bot.command()
async def diceroll(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"The dice rolled: **{result}**")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def delete(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Deleted {len(deleted) - 1} messages.", delete_after=3)

# Run bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file!")

bot.run(TOKEN)
