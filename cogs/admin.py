from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def checkperms(self, ctx):
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
        print(f"Attach Files: {perms.attach_files}")
        print("================================\n")


async def setup(bot):
    await bot.add_cog(Admin(bot))
