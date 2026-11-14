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
    print("================================\n")

gali=["gandu", "madarchod", "bhosdike", "chutiya", "harami", "randi", "bhenchod", "lodu", "lund", "chodu"]

@bot.command()
async def gali_de(ctx):
    await ctx.send(random.choice(gali))

@bot.command()
async def who_is(ctx, *, msg):
    name = msg.split()[0]
    if name.lower() == "tanay":
        await ctx.send(f"{name} is sin theta paglu/ tantheta")
    elif name.lower() == "antariksha":
        await ctx.send(f"{name} is Universal Riksha")
    elif name.lower() == "deepraj":
        await ctx.send(f"{name} is our Bhabi Ji")
    elif name.lower() == "anshuman":
        await ctx.send(f"{name} is Duduman/ Antman")
    elif name.lower() == "somnath":
        await ctx.send(f"{name} is Chomu")
    elif name.lower() == "abhishek":
        await ctx.send(f"{name} is Kalu Bhai")
    elif name.lower() == "shubhrajyoti":
        await ctx.send(f"{name} is Wak/ Loti") 
    elif name.lower() == "abhinab":
        await ctx.send(f"{name} is Haddi")
    elif name.lower() == "seymas":
        await ctx.send(f"{name} is Sap/ chhoimas")
    elif name.lower() == "jakob":
        await ctx.send(f"{name} is Hizra/ Alpha Male")
    elif name.lower() == "soumik":
        await ctx.send(f"{name} is Auntu")  
    elif name.lower() == "samrat": 
        await ctx.send(f"{name} is raitta")
    elif name.lower() == "roshan": 
        await ctx.send(f"{name} is the GOAT")
    elif name.lower() == "modi": 
        await ctx.send(f"{name} is modihhh")       
    else:
        await ctx.send(f"idk who tf that is")  

# Run bot
if not TOKEN:
    raise ValueError("DISCORD_TOKEN not found in .env file!")

bot.run(TOKEN)
